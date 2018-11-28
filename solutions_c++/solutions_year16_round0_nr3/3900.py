#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int NUM = 1 << 17;
int N, J;
int su[NUM], len;
bool f[NUM];


long isPrime(long x) {
    for (int i = 0; i < len; i++) {
        if (su[i] * su[i] > x)
            break;
        if (x % su[i] == 0)
            return su[i];
    }
    return -1;
}


void print(long n) {
    if (n >> 1)
        print(n >> 1);
    printf("%d", n & 1);
}

bool check(int n) {
    long c[11];
    for (int base = 2; base <= 10; base++) {
        long x = 0;
        int y = n;
        long r = 1;
        while (y > 0) {
            if (y & 1) {
                x += r;
            }
            y >>= 1;
            r *= base;
        }
        long res = isPrime(x);
        if (res == -1)
            return false;
        c[base] = res;
    }
    print(n);
    for (int base = 2; base <= 10; base++)
        printf(" %d", c[base]);
    printf("\n");

}


void solve() {
    int n = 1 << (N - 4);
    while (J) {
        int t = (n << 1) + 1 + (1 << (N - 1));
        if (check(t)) {
            J--;
        }
        n++;
    }
}

void init() {
    for (int i = 2; i < NUM; i++) if (!f[i]) {
        su[len++] = i;
        for (int j = i + i; j < NUM; j += i) {
            f[j] = true;
        }
    }
}

int main() {
    init();
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d%d", &N, &J);
        printf("Case #%d:\n", i);
        solve();
    }
}
