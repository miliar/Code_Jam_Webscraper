#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

struct node {
    int x, y, w;
} p[100010];

int t, n, m, h[110][110];
bool vis[110][2];

bool cmp(const node &x, const node &y) {
    return x.w < y.w;
}

int getmax(int x, int j) {
    int ans = -1;
    if (j == 0) {
        for (int i = 0; i < m; i ++ )
            if (!vis[i][1])
                ans = max(ans, h[x][i]);
    }
    else {
        for (int i = 0; i < n; i ++ )
            if (!vis[i][0])
                ans = max(ans, h[i][x]);
    }
    return ans;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ca ++ ) {
        scanf("%d%d", &n, &m);
        int cnt = 0;
        for (int i = 0; i < n; i ++ )
            for (int j = 0; j < m; j ++ ) {
                scanf("%d", &h[i][j]);
                p[cnt].x = i;
                p[cnt].y = j;
                p[cnt].w = h[i][j];
                cnt ++ ;
            }
        memset(vis, 0, sizeof(vis));
        sort(p, p + cnt, cmp);
        bool flag = true;
        for (int i = 0; i < cnt; i ++ )
            if (!vis[p[i].x][0] && !vis[p[i].y][1]) {
                    int w = getmax(p[i].x, 0);
                    if (w == p[i].w) {
                        vis[p[i].x][0] = true;
                        continue;
                    }
                    w = getmax(p[i].y, 1);
                    if (w == p[i].w) {
                        vis[p[i].y][1] = true;
                        continue;
                    }
                    flag = false;
                    break;
            }
        printf("Case #%d: ", ca);
        if (flag) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
