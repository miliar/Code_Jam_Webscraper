/**
 * Copyright (c) 2015 Authors. All rights reserved.
 * 
 * FileName: C.cpp
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

const int maxn = 10000 + 5;

int n, k;
char s[maxn];
int f[maxn];

int calc(int u, int v)
{
        int res = u ^ v;
        u &= 3; v &= 3;
        if (!u || !v) return res;
        if (v != u + 1 && !(u == 3 && v == 1)) res ^= 4;
        return res;
}

bool solve()
{
        n *= k;
        f[n] = 0;
        for (int i = n - 1; i >= 0; --i) f[i] = calc(s[i] - 'h', f[i+1]);
        int now = 0;
        rep(i,n) {
                now = calc(now, s[i] - 'h');
                if (now == 1) {
                        int tmp = 0;
                        for (int j = i + 1; j < n; ++j) {
                                tmp = calc(tmp, s[j] - 'h');
                                if (tmp == 2 && f[j+1] == 3) return true;
                        }
                }
        }
        return false;
}

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        while (T--) {
                scanf("%d%d%s", &n, &k, s);
                For(i,1,k-1) strncpy(s + n * i, s, n);
                printf("Case #%d: %s\n", ++cas, solve()? "YES": "NO");
        }

        return 0;
}
