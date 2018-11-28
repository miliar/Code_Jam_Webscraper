//
//  main.cpp
//  A
//
//  Created by IwfWcf on 13-6-1.
//  Copyright (c) 2013年 IwfWcf. All rights reserved.
//

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<stack>
#define MOD 1000002013
#define N 2010

using namespace std;

typedef long long LL;

struct node
{
    int t, p, num;
};

inline int cal(LL n, int k, int num)
{
    if (k == 0) return 0;
    return (n + n + 1 - k) * k / 2 % MOD * num % MOD;
}

inline bool cmp(node a, node b)
{
    if (a.p != b.p) return a.p < b.p;
    return a.t < b.t;
}

node a[N];

int main()
{
	freopen("/Users/IwfWcf/Desktop/A/input.txt", "r", stdin);
	freopen("/Users/IwfWcf/Desktop/A/output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        int n, m, total = 0;
        scanf("%d%d", &n, &m);
        LL ans1 = 0, ans2 = 0;
        for (int i = 0; i < m; i++) {
            int o, e, p;
            scanf("%d%d%d", &o, &e, &p);
            ans1 += cal(n, e - o, p), ans1 %= MOD;
            a[total].t = 0, a[total].num = p, a[total++].p = o;
            a[total].t = 1, a[total].num = p, a[total++].p = e;
        }
        sort(a, a + total, cmp);
        stack<int> S;
        for (int i = 0; i < total; i++)
            if (!a[i].t) S.push(i);
            else {
                while (a[i].num) {
                    int now = S.top(), num = min(a[i].num, a[now].num);
                    ans2 += cal(n, a[i].p - a[now].p, num), ans2 %= MOD;
                    a[i].num -= num, a[now].num -= num;
                    if (!a[now].num) S.pop();
                }
            }
        printf("Case #%d: %d\n", cases, (ans1 - ans2 + MOD) % MOD);
    }
    return 0;
}