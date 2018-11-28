/**
 * Copyright (c) 2015 Authors. All rights reserved.
 * 
 * FileName: A.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2015-05-30
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

const int maxn = 100 + 5;

int n, m;
char g[maxn][maxn];
int mp[256];
int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};

bool inside(int x, int y) { return 0 <= x && x < n && 0 <= y && y < m; }

bool check(int x, int y, int d)
{
        while (true) {
                x += dx[d]; y += dy[d];
                if (!inside(x, y)) break;
                if (g[x][y] != '.') return true;
        }
        return false;
}

int solve()
{
        int res = 0;
        rep(i,n) rep(j,m) if (g[i][j] != '.') {
                int d = mp[g[i][j]];
                if (check(i, j, d)) continue;
                bool found = false;
                rep(k,4) if (k != d && check(i, j, k)) {
                        found = true;
                        ++res;
                        break;
                }
                if (!found) return -1;
        }
        return res;
}

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        mp['^'] = 0; mp['v'] = 1; mp['<'] = 2; mp['>'] = 3;
        while (T--) {
                scanf("%d%d", &n, &m);
                rep(i,n) scanf("%s", g[i]);
                int res = solve();
                printf("Case #%d: ", ++cas);
                if (res == -1) puts("IMPOSSIBLE");
                else printf("%d\n", res);
        }

        return 0;
}
