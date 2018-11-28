/**
 * Copyright (c) 2013 Authors. All rights reserved.
 * 
 * FileName: B.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2013-04-13
 */
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef pair<int, int> Point;

const int INF = 0x3f3f3f3f;
const int MAXN = 100 + 5;

int n, m;
int g[MAXN][MAXN], tmp[MAXN][MAXN];
vector<Point> v;

void init()
{
        v.clear();
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i)
                for (int j = 0; j < m; ++j) {
                        scanf("%d", &g[i][j]);
                        tmp[i][j] = INF;
                        v.push_back(make_pair(-g[i][j], i * m + j));
                }
        sort(v.begin(), v.end());
}

bool solve()
{
        bool ok;

        for (int idx = 0; idx < v.size(); ++idx) {
                int x = v[idx].second / m;
                int y = v[idx].second % m;

                if (g[x][y] > tmp[x][y])
                        return false;

                ok = true;
                for (int j = 0; j < m; ++j)
                        ok &= (g[x][j] <= g[x][y]);
                if (ok) {
                        for (int j = 0; j < m; ++j)
                                tmp[x][j] = g[x][y];
                        continue;
                }

                ok = true;
                for (int i = 0; i < n; ++i)
                        ok &= (g[i][y] <= g[x][y]);
                if (ok) {
                        for (int i = 0; i < n; ++i)
                                tmp[i][y] = g[x][y];
                        continue;
                }

                return false;
        }

        return true;
}

int main()
{
        //freopen("B-large.in", "r", stdin);
        //freopen("B-large.out", "w", stdout);

        int T, cas = 0;

        scanf("%d", &T);

        while (T--) {
                init();
                printf("Case #%d: %s\n", ++cas, solve()? "YES": "NO");
        }

        return 0;
}
