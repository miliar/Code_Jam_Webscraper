#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstdlib>

const int MAXN = 1000;

int x0[MAXN], y0[MAXN], x1[MAXN], y1[MAXN];

int head[MAXN + 2], L;

struct Edge {
    int to, next, len;
} edge[10000000];


void init(int n) {
    std :: fill(head, head + n, -1);
    L = 0;
}

void add_edge(int u, int v, int len) {
    edge[L].to = v;
    edge[L].len = len;
    edge[L].next = head[u];
    head[u] = L ++;
}

int getdis(int a, int b, int c, int d) {
    if (a > c) {
        std :: swap(a, c);
        std :: swap(b, d);
    }
    if (b >= c - 1)
        return 0;
    else
        return c - 1 - b;
}

int dis[MAXN + 2];
bool inque[MAXN + 2];

void spfa(int s) {
    dis[s] = 0;
    std :: queue <int> que;
    que.push(s);
    while (!que.empty()) {
        int u = que.front();
        inque[u] = false;
        que.pop();
        for (int i = head[u]; i != -1; i = edge[i].next) {
            int v = edge[i].to;
            if (dis[v] > dis[u] + edge[i].len) {
                dis[v] = dis[u] + edge[i].len;
                if (!inque[v]) {
                    inque[v] = true;
                    que.push(v);
                }
            }
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        int w, h, b;
        scanf("%d%d%d", &w, &h, &b);
        if (0 == b) {
            printf("Case #%d: %d\n", cas, w);
        } else {
            for (int i = 0; i < b; ++ i) {
                scanf("%d%d%d%d", &x0[i], &y0[i], &x1[i], &y1[i]);
                continue;
                x0[i] = rand() % w;
                x1[i] = rand() % w;
                if (x0 > x1)
                    std :: swap(x0[i], x1[i]);
                y0[i] = (long long) rand() * rand() % h;
                y1[i] = (long long) rand() * rand() % h;
                if (y0 > y1)
                    std :: swap(y0[i], y1[i]);
            }
            init(b + 2);
            for (int i = 0; i < b; ++ i) {
                add_edge(b, i, x0[i]);
                add_edge(i, b + 1, w - x1[i] - 1);
                for (int j = 0; j < i; ++ j) {
                    int disx = getdis(x0[i], x1[i], x0[j], x1[j]);
                    int disy = getdis(y0[i], y1[i], y0[j], y1[j]);
                    add_edge(i, j, std :: max(disx, disy));
                    add_edge(j, i, std :: max(disx, disy));
                }
            }
            std :: fill(dis, dis + b + 2, 0x3f3f3f3f);
            spfa(b);
            printf("Case #%d: %d\n", cas, dis[b + 1]);
        }
    }
    return 0;
}
