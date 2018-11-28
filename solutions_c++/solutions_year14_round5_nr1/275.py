#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <queue>
#include <stack>
#define zero(x) (((x)>0?(x):-(x))<eps)
//#include <bits/stdc++.h>
#define mem(a,b) memset((a),(b),sizeof((a)))
#define lld long long
#define INF 0x3f3f3f3f

using namespace std;

long long num[1000009];
long long n, p, q, r, s;

long long cal(long long a, long long b, long long c) {
    return num[n] - max(max(a, b), c);
}

int MAIN() {
    scanf("%lld%lld%lld%lld%lld", &n, &p, &q, &r, &s);
    num[0] = 0;
    for(int i = 1; i <= n; i++) {
//            putchar('.');
        num[i] = ((i - 1) * p + q) % r + s;
//        printf("%lld ", num[i]);
        num[i] += num[i - 1];
    }
    long long ans = 0;
    int p = 0;
    for(int i = 1; i <= n; i++) {
        ans = max(ans, cal(num[p], num[i] - num[p], num[n] - num[i]));
        while(num[p] * 2 < num[i]) {
            p++;
            ans = max(ans, cal(num[p], num[i] - num[p], num[n] - num[i]));
        }
        p--;
    }
    printf("%.15f\n", (double)ans / (double)num[n]);
    return 0;
}


int main() {
#ifdef LOCAL_TEST
    freopen("F:/ACMData.txt","r",stdin);
    freopen("F:/out1.txt","w",stdout);
#endif
    int cases;
    scanf("%d", &cases);
    int cc = 1;
    while(cases--) {
        printf("Case #%d: ", cc++);
        MAIN();
    }
    return 0;
}
