/**
 * Copyright (c) 2015 Authors. All rights reserved.
 * 
 * FileName: A.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2015-04-12
 */
#include <bits/stdc++.h>

using namespace std;

#define rep(i,n) for (int i = 0; i < (n); ++i)
#define For(i,s,t) for (int i = (s); i <= (t); ++i)
#define foreach(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 1000 + 5;

int n;
char s[maxn];

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        while (T--) {
                scanf("%d%s", &n, s);
                int now = 0, res = 0;
                For(i,0,n) {
                        if (now < i) res += i - now, now = i;
                        now += s[i] - '0';
                }
                printf("Case #%d: %d\n", ++cas, res);
        }

        return 0;
}
