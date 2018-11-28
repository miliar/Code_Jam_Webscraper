#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <random>
#include <iostream>
#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
#endif

using namespace std;
typedef pair<int, int> ii;


int nTest;
int n, m;

long long getDivisor(long long x){
    for (long long i = 2; i <= (long long)sqrt(x); i++){
        if (x % i == 0) return i;
    }
    return 1;
}

long long fromBase(int base, long long i){
    long long t = 1;
    long long res = 0;
    for (int j = 0; j < n * 2 + 2; j++){

        res += t * ((i >> j) & 1);

        t *= base;
    }
    return res;
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("c.inp", "r", stdin);
    freopen("c.out", "w", stdout);
#endif

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d:\n", test);
        scanf("%d %d", &n, &m);
        n /= 2;
        n--;
        for (int i = 0; i < (1 << n); i++){
            if (i >= m) break;

            // long long x = (1 << n) | i;
            // long long y = 0;
            // for (int j = 0; j < n + 1; j++) y = (y << 1) | ((x >> j) & 1);
            // x <<= n + 1;
            // x |= y;
            // for (int j = 0; j < n * 2 + 2; j++) printf("%lld", (x >> j) & 1);
            // printf(" ");
            // x = fromBase(4, x);
            // printf("%lld ", x % 5);

            printf("1");
            for (int j = 0; j < n; j++) printf("%d", (i >> (n - 1 - j)) & 1);
            for (int j = 0; j < n; j++) printf("%d", (i >> j) & 1);
            printf("1 ");
            printf("3 2 5 2 7 2 3 2 11\n");
        }
    }
    

    return 0;
}