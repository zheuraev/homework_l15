from typing import Any
import collections
import re


# Решить задачи, выложить .py файл с решениями на github. В личный кабинет прикрепить .txt файл с ссылкой на репозиторий.


# Задача 1. Найти количество различных элементов массива. Пример: для [1 4 5 1 1 3] ответ 4.
def count_unique_elems(arr):
    return len(set(arr))


# Задача 2. Дан файл с логинами и паролями. Найдите топ10 самых популярных паролей.
# Ссылка на файл: https://yadi.sk/i/6ywJqzm93HGmy9
def get_10_popular_password(file: str) -> Any:
    arr = []
    with open(file, encoding='utf-8') as f:
        for line in f:
            password = line.split(';')[-1]
            password = password.rstrip("\n")
            arr.append(password)
    password_cnt = collections.Counter(arr)
    print(password_cnt.most_common(10))



#Час времени убил вот на это, пока не вспомнил что мы коллекцию проходили
# def get_10_popular_password(file: str) -> Any:
#     dict_pass = {}
#     with open(file, encoding='utf-8') as f:
#         for line in f:
#             password = line.split(';')[-1]
#             password = password.rstrip("\n")
#             if password not in dict_pass:
#                 dict_pass[password] = 1
#             else:
#                 dict_pass[password] += 1
#     sorted_values = sorted(dict_pass.values())
#     sorted_dict = {}
#     for i in sorted_values:
#         for k in dict_pass.keys():
#             if dict_pass[k] == i:
#                 sorted_dict[k] = dict_pass[k]


# Задача 3. Дана строка с ссылками. Заменить все ссылки на ***** (5 звёздочек).
# Примеры ссылок:
# www.site.com заменится на *****
# http://example.su заменится на *****
# vk.ru заменится на *****
# https://example.com/smth/else заменится на *****
# и т.д.
# Чем больше разных вариантов будет придумано, тем лучше, но без фанатизма.
# Для простоты, ограничьте набор доменов верхнего уровня (штуки 4-7 достаточно).
def censor_link(string: str) -> str:
    regular = re.compile('(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?')
    return regular.sub('*****', string)


# Здесь писать тесты для функций с решениями
def main():
    arr = [2, 3, 4, 4]
    print(count_unique_elems(arr))

    get_10_popular_password(file = 'pwd.txt')

    string = 'я зашел на www.vk.ru, но к сожалению попал на facebook.com. На этом пои попытки не закончились' \
             'и я отправился на https://www.youtube.com/ но он тоже меня подвел и вот я уже на сайте citilink https://www.citilink.ru/login/'
    print(censor_link(string))


if __name__ == '__main__':
    main()
