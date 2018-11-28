/* 
 * File:   main.cpp
 * Author: Yiting
 *
 * Created on April 13, 2013, 8:52 AM
 */

#include <cstdlib>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
int n, a, b, res;

FILE *fin = fopen("test.in", "rb");
FILE *fout = fopen("test.out", "wb");

bool is_palindrome(int n) {
    int i;
    char buf[50];
    int len = sprintf(buf, "%d", n);
    for (i = 0; i * 2 + 1 < len; i++)
        if (buf[i] != buf[len - 1 - i])
            return false;
    return true;
}

int reverse(int n) {
    int result = 0;
    while (n > 0) {
        result = result * 10 + (n % 10);
        n /= 10;
    }
    return result;
}

bool isP_(int r) {
    double x = sqrt((double) r);
    int y = (int) sqrt((double) r);
    if (x == y && is_palindrome(y)) return true;
    return false;
}

void calc(int a, int b) {
    int i;
    int base = 1;
    while (base * base * 10 < a)
        base *= 10;
    while (true) {
        for (i = base; i < base * 10; i++) {
            int r = i * base + (reverse(i) % base);
            if (r > b)
                return;
            if (r >= a && isP_(r)) {
                res++;
            }
        }
        for (i = base; i < base * 10; i++) {
            int r = i * base * 10 + reverse(i);
            if (r > b)
                return;
            if (r >= a && isP_(r)) {
                res++;
            }
        }
        base *= 10;
    }
}

int main() {
    int c = 1;
    fscanf(fin, "%d", &n);
    while (fscanf(fin, "%d %d", &a, &b) == 2) {
        res = 0;
        calc(a, b);
        fprintf(fout, "Case #%d: %d\n", c, res);
        c++;
    }
    return 0;
}

