//
// Created by adinata on 09/04/16.
//

#include <iostream>
#include <cstdio>

using namespace std;

// Points 7 + 8
// create a boolean map of 10, that counts how many false to true happened.
// false to true happened if we found a number we haven't seen before
// to check a number, get N, multiplied by i, then mod 10 and div 10 until reach 0.
// Be Careful to not count last div 10 which results in 0.
// in case of 0, it will always 0, returns IMSONIA

bool checker[10];
int count;
int reset() {
    count = 0;
    for (int i=0; i<10; i++) {
        checker[i] = false;
    }
    return 0;
}
void print() {
    for (int i=0; i<10; i++) {
        printf("%d=%d\n", i, checker[i]);
    }
    printf("=========\n");
}
int update(int number) {
    int i;
    while (number > 0) {
        i = number % 10;
        if (!checker[i]) {
            count ++;
            checker[i] = true;
        }
        if (count >= 10) {
            return 1;
        }
        number /= 10;
    }
    return 0;
}
int T;
int main() {
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        reset();
        int number, n;
        scanf("%d", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", tc);
            continue;
        }
        int i = 1;
        number = n;
        while (update(number) != 1) {
            i++;
            number = n * i;
        }
        printf("Case #%d: %d\n", tc, number);
    }
    return 0;
}
