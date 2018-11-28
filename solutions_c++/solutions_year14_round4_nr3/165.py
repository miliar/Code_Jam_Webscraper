/**
 * Copyright (c) 2014 Authors. All rights reserved.
 * 
 * FileName: C.cpp
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

const int maxn = 1000 + 5;

int w, h, n;
int xl[maxn], xr[maxn], yl[maxn], yr[maxn];
int dis[maxn];
bool vis[maxn];

int calc(int u, int v)
{
        if (u == v) return 0;
        if (xr[u] < xl[v] || xr[v] < xl[u]) {
                if (yr[u] < yl[v] || yr[v] < yl[u]) {
                        int dx = max(xl[u], xl[v]) - min(xr[u], xr[v]) - 1;
                        int dy = max(yl[u], yl[v]) - min(yr[u], yr[v]) - 1;
                        return max(dx, dy);
                } else {
                        return max(xl[u], xl[v]) - min(xr[u], xr[v]) - 1;
                }
        } else {
                return max(yl[u], yl[v]) - min(yr[u], yr[v]) - 1;
        }
}

void spfa()
{
        queue<int> que;
        memset(dis, 0x3f, sizeof(dis));
        memset(vis, false, sizeof(vis));
        dis[0] = 0; vis[0] = true; que.push(0);
        while (!que.empty()) {
                int u = que.front(); que.pop(); vis[u] = false;
                REP(v,n+2) {
                        int w = calc(u, v);
                        if (dis[u] + w < dis[v]) {
                                dis[v] = dis[u] + w;
                                if (!vis[v]) {
                                        vis[v] = true;
                                        que.push(v);
                                }
                        }
                }
        }
}

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        while (T--) {
                scanf("%d%d%d", &w, &h, &n);
                FOR(i,1,n) scanf("%d%d%d%d", &xl[i], &yl[i], &xr[i], &yr[i]);
                xl[0] = -1; yl[0] = -1;
                xr[0] = -1; yr[0] = h + 1;
                xl[n+1] = w; yl[n+1] = -1;
                xr[n+1] = w; yr[n+1] = h + 1;
                spfa();
                printf("Case #%d: %d\n", ++cas, dis[n+1]);
        }

        return 0;
}
