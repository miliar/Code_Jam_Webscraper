#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

const int step[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int t, w, h, b;
bool vis[510][510];

/*Dinic*/
#define Maxm 1000005
#define Maxn 500005
#define INF 0x3f3f3f3f
struct edge {
    int u, v, c, next;
} e[Maxm];
int head[Maxn], cnt;
void init() {
    memset(head, -1, sizeof(head));
    cnt = 0;
}
void addedge(int s, int t, int v){
    e[cnt].u = s, e[cnt].v = t, e[cnt].c = v;
    e[cnt].next = head[s], head[s] = cnt ++ ;
    e[cnt].u = t, e[cnt].v = s, e[cnt].c = 0;
    e[cnt].next = head[t], head[t] = cnt ++ ;
}
int dis[Maxn], cur[Maxn], sta[Maxn], que[Maxn], pre[Maxn];
bool bfs(int s, int t, int n) {
    int front = 0, tail = 0;
    memset(dis, -1, sizeof(dis[0]) * (n + 1));
    dis[s] = 0;
    que[tail ++ ] = s;
    while (front < tail) {
        for (int i = head[que[front ++ ]]; i != -1; i = e[i].next)
            if (e[i].c > 0 && dis[e[i].v] == -1){
                dis[e[i].v] = dis[e[i].u] + 1;
                if (e[i].v == t)
                    return 1;
                que[tail ++ ] = e[i].v;
            }
    }
    return 0;
}
int dinic(int s, int t, int n) {
    int maxflow = 0, tp;
    while (bfs(s, t, n)) {
        for (int i = 0; i < n; i ++ )
            cur[i] = head[i];
        int u = s, tail = 0;
        while(cur[s] != -1){
            if(u == t){
                tp = INF;
                for (int i = tail - 1; i >= 0; i -- )
                    tp = min(tp, e[sta[i]].c);
                maxflow += tp;
                for (int i = tail - 1; i >= 0; i -- ){
                    e[sta[i]].c -= tp;
                    e[sta[i] ^ 1].c += tp;
                    if (e[sta[i]].c == 0)
                        tail = i;
                }
                u = e[sta[tail]].u;
            }
            else if (cur[u] != -1 && e[cur[u]].c > 0
                  && dis[u] + 1 == dis[e[cur[u]].v]) {
                sta[tail ++ ] = cur[u];
                u = e[cur[u]].v;
            }
            else {
                while (u != s && cur[u] == -1)
                    u = e[sta[ -- tail]].u;
                cur[u] = e[cur[u]].next;
            }
        }
    }
    return maxflow;
}

int getw(int x, int y, int s) {
    return x * h + y + 2 + w * h * s;
}

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ca ++ ) {
        scanf("%d%d%d", &w, &h, &b);
        memset(vis, 0, sizeof(vis));
        for (int i = 0; i < b; i ++ ) {
            int x0, y0, x1, y1;
            scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
            for (int x = x0; x <= x1; x ++ )
            for (int y = y0; y <= y1; y ++ )
                vis[x][y] = true;
        }
        init();
        int s = 0, t = 1;
        for (int i = 0; i < w; i ++ ) {
            if (!vis[i][0]) addedge(s, getw(i, 0, 0), 1);
            if (!vis[i][h - 1]) addedge(getw(i, h - 1, 1), t, 1);
        }
        for (int i = 0; i < w; i ++ )
        for (int j = 0; j < h; j ++ )
            if (!vis[i][j]) {
            for (int k = 0; k < 4; k ++ ) {
                int x = i + step[k][0];
                int y = j + step[k][1];
                if (x < 0 || y < 0 || x >= w || y >= h || vis[x][y]) continue;
                addedge(getw(i, j, 1), getw(x, y, 0), 1);
            }
            addedge(getw(i, j, 0), getw(i, j, 1), 1);
            }
        printf("Case #%d: %d\n", ca, dinic(s, t, w * h * 2 + 2));
    }
    return 0;
}
