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
int n;
int digit[11];

int main(){
#ifndef ONLINE_JUDGE
    freopen("a.inp", "r", stdin);
    freopen("a.out", "w", stdout);
#endif

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        memset(digit, 0, sizeof(digit));

        scanf("%d", &n);
        if (n == 0) {
            printf("INSOMNIA\n");
            continue;
        }

        for (int i = 1; i <= 1000000; i++){
            long long t = (long long)i * (long long)n;
            while (t > 0) {
                digit[t % 10] = 1;
                t /= 10;
            }

            int sleep = 1;
            for (int i = 0; i < 10; i++) {
                if (digit[i] == 0) sleep = 0;
            }

            if (sleep) {
                printf("%d\n", i * n);
                break;
            }
        }
    }
    

    return 0;
}