#define _N 1010

#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

struct Edge {
    int id, next;
} edge[_N * 2];

int head[_N], nEdge, nV;
int f[_N], g[_N];
bool vis[_N];

void init() {
    memset(head, -1, sizeof(head));
    nEdge = 0;
}

void addEdge(int a, int b) {
    edge[nEdge].id = b;
    edge[nEdge].next = head[a];
    head[a] = nEdge++;
}

int fs[_N][_N], gs[_N][_N];

void dfs(int x) {
    vis[x] = true;
    g[x] = 0;
    int cnt = 0;
    for (int i = head[x]; i != -1; i = edge[i].next) {
        if (vis[edge[i].id]) continue;
        dfs(edge[i].id);
        g[x] += g[edge[i].id];
        fs[x][cnt] = f[edge[i].id];
        gs[x][cnt++] = g[edge[i].id];
    }

    f[x] = g[x];
    for (int i = 0; i < cnt; ++i) {
        for (int j = 0; j < i; ++j) {
            f[x] = min(f[x], fs[x][i] + fs[x][j] + g[x] - gs[x][i] - gs[x][j]);
        }
    }
    g[x]++;
}

int tryRoot(int r) {
    memset(vis, 0, sizeof(vis));
    dfs(r);
    return f[r];
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;

    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++cas) {
        scanf("%d", &nV);
        int a, b;
        init();
        for (int i = 1; i < nV; ++i) {
            scanf("%d%d", &a, &b);
            addEdge(a, b);
            addEdge(b, a);
        }

        int ret = nV;
        for (int i = 1; i <= nV; ++i) {
            int ans = tryRoot(i);

//            printf("try root = %d, ans = %d\n", i, ans);
            ret = min(ret, ans);
        }
        printf("Case #%d: %d\n", cas, ret);
    }

    return 0;
}
