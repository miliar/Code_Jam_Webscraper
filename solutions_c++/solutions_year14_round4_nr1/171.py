/**
 * Copyright (c) 2014 Authors. All rights reserved.
 * 
 * FileName: A.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2014-05-31
 */
#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for (int i = 0; i < (n); ++i)
#define FOR(i,s,t) for (int i = (s); i <= (t); ++i)
#define FOREACH(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 10000 + 5;

int n, x;
int s[maxn], match[maxn];
bool vis[maxn];

bool aug(int u)
{
        REP(v,n) if (s[u] + s[v] <= x) {
                if (vis[v]) continue; vis[v] = true;
                if (match[v] == -1 || aug(match[v])) {
                        match[v] = u;
                        return true;
                }
        }
        return false;
}

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        while (T--) {
                scanf("%d%d", &n, &x);
                REP(i,n) scanf("%d", &s[i]);
                int cnt = 0;
                memset(match, -1, sizeof(match));
                for (int i = 0; i < n; ++i) {
                        memset(vis, false, sizeof(vis));
                        if (aug(i)) ++cnt;
                }
                printf("Case #%d: %d\n", ++cas, n - cnt / 2);
        }

        return 0;
}
