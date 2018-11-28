/**
 * Copyright © 2016 Authors. All rights reserved.
 * 
 * FileName: D.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2016-05-28
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

const int maxn = 4 + 5;

int n, ret;
int g[maxn][maxn];

bool check()
{
        rep(i,n) {
                int cnt = 0;
                set<int> st;
                rep(j,n) if (g[i][j]) {
                        ++cnt;
                        rep(k,n) if (k != i && g[k][j]) st.insert(k);
                }
                if (st.size() >= cnt) return false;
        }
        return true;
}

void dfs(int i, int j, int now)
{
        if (i == n) {
                if (check()) ret = min(ret, now);
                return;
        }
        dfs(j == n - 1? i + 1: i, j == n - 1? 0: j + 1, now);
        if (!g[i][j]) {
                g[i][j] = 1;
                dfs(j == n - 1? i + 1: i, j == n - 1? 0: j + 1, now + 1);
                g[i][j] = 0;
        }
}

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        while (T--) {
                scanf("%d", &n);
                rep(i,n) rep(j,n) scanf("%1d", &g[i][j]);
                ret = inf;
                dfs(0, 0, 0);
                printf("Case #%d: %d\n", ++cas, ret);
        }

        return 0;
}
