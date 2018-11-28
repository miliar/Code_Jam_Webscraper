//
//  main.cpp
//  D
//
//  Created by IwfWcf on 13-6-15.
//  Copyright (c) 2013年 IwfWcf. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <queue>
#define N 210

using namespace std;

char s[N];
double f[N], Num[1 << 20];

inline int count(int x)
{
    int ret = 0;
    while (x) {
        if (x & 1) ret++;
        x >>= 1;
    }
    return ret;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/IwfWcf/Desktop/D/input.txt", "r", stdin);
    freopen("/Users/IwfWcf/Desktop/D/output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        scanf("%s", s);
        int n = strlen(s);
        f[0] = 1;
        for (int i = 1; i <= n; i++) f[i] = f[i - 1] * n;
        int mask = 0;
        for (int i = 0; i < n; i++)
            if (s[i] == 'X') mask |= 1 << i;
        int c = count(mask), l = 1 << n;
        for (int i = 0; i < l; i++) Num[i] = 0;
        Num[mask] = 1;
        double ans = 0;
        queue<int> q;
        for (q.push(mask); !q.empty(); q.pop()) {
            int now = q.front(), cc = count(now);
            double num = Num[now];
            if (now == (1 << n) - 1) break;
            for (int i = 0; i < n;) {
                int j;
                for (j = i; 1; j = (j + 1) % n) {
                    mask = 1 << j;
                    if (!(mask & now)) break;
                }
                int k = j, d = (j - i + n) % n;
                for (j = i; j < n && d >= 0; j++, d--)
                    ans += (n - d) * (1 / f[cc - c + 1]) * num;
                if (k >= i) d = k - i + 1;
                else d = n - i;
                mask |= now;
                if (!Num[mask]) q.push(mask);
                Num[mask] += num * d;
                if (k < i) break;
                i = k + 1;
            }
        }
        printf("Case #%d: %.14lf\n", cases, ans);
    }
    return 0;
}

