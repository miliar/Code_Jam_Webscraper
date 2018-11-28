#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char pancakes[100];
int length;

int flip () {
    for (int i = length - 1; i >= 0; i--) {
        if (pancakes[i] == '+') {
            length--;
        }
        else break;
    }
    for (int i = 0; i < length; i++) {
        if (pancakes[i] == '-') {
            pancakes[i] = '+';
        }
        else if (pancakes[i] == '+') {
            pancakes[i] = '-';
        }
    }
    if (length > 0) {
        return 1;
    }
    else return 0;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int a = 1; a <= t; a++) {
        memset(pancakes, 0, 100);
        cin >> pancakes;
        length = strlen(pancakes);
        int count = 0;
        while (flip()) {
            count++;
        }
        printf("Case #%d: %d\n", a, count);
    }
    return 0;
}
