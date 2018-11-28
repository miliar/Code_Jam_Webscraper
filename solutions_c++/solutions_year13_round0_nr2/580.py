#include <iostream>
#include <cstdio>
#include <cstring>

#define MAXV 256
#define MAXE 100010
#define INF 1024

using namespace std;

struct Edge {
    int ed, flow, next;
} edge[MAXE];

int head[MAXV], nEdge;
int d[MAXV], pre[MAXV], path[MAXV], his[MAXV], cur[MAXV], vh[MAXV];

inline void init() {
    memset(head, -1, sizeof(head));
    nEdge = 0;
}

inline void addEdge(int a, int b, int flow) {
    edge[nEdge].ed = b;
    edge[nEdge].flow = flow;
    edge[nEdge].next = head[a];
    head[a] = nEdge++;
    edge[nEdge].ed = a;
    edge[nEdge].flow = 0;
    edge[nEdge].next = head[b];
    head[b] = nEdge++;
}

int sap(int v, int src, int dst) {
    int x, y, i, m, nowFlow = INF, totalFlow = 0;
    bool flag;

    memset(d, 0, sizeof(d));
    memset(vh, 0, sizeof(vh));
    memcpy(cur, head, sizeof(cur));

    for (vh[0] = v, x = src; d[src] < v;) {
        his[x] = nowFlow; flag = false;
        for (i = cur[x]; ~i; i = edge[i].next) {
            if (edge[i].flow && d[x] == d[y = edge[i].ed] + 1) {
                flag = true;
                nowFlow = min(nowFlow, edge[i].flow);
                pre[y] = x; path[y] = cur[x] = i;
                if ((x = y) == dst) {
                    for (totalFlow += nowFlow; x != src; x = pre[x]) {
                        edge[path[x]].flow -= nowFlow;
                        edge[path[x] ^ 1].flow += nowFlow;
                    }
                    nowFlow = INF;
                }
                break;
            }
        }
        if (!flag) {
            for (m = v - 1, i = cur[x] = head[x]; ~i; i = edge[i].next) {
                if (edge[i].flow && d[y = edge[i].ed] < m) {
                    m = d[y]; cur[x] = i;
                }
            }
            if (!(--vh[d[x]])) break;
            ++vh[d[x] = m + 1];
            if (x != src) nowFlow = his[x = pre[x]];
        }
    }

    return totalFlow;
}

#include <algorithm>
#include <functional>

int mat[MAXV][MAXV], val[MAXE];
bool vis[2][MAXV];

bool check(int n, int m, int h) {
    int i, j, v = n + m + 2, src = n + m, dst = n + m + 1;

    init();
    for (i = 0; i < n; ++i) {
        for (j = 0; j < m; ++j) {
            if (mat[i][j] > h) {
                vis[0][i] = vis[1][j] = true;
            } else {
                addEdge(i, j + n, INF);
            }
        }
    }
    for (i = 0; i < n; ++i) {
        if (vis[0][i]) addEdge(src, i, INF);
        else addEdge(src, i, 1);
    }
    for (i = 0; i < m; ++i) {
        if (vis[1][i]) addEdge(i + n, dst, INF);
        else addEdge(i + n, dst, 1);
    }

    return sap(v, src, dst) < INF;
}

bool solve(int n, int m) {
    int i, j, cnt = 0;

    memset(vis, 0, sizeof(vis));
    for (i = 0; i < n; ++i) {
        for (j = 0; j < m; ++j) {
            val[cnt++] = mat[i][j];
        }
    }
    sort(val, val + cnt, greater<int>());
    cnt = unique(val, val + cnt) - val;
    for (i = 0; i < cnt; ++i) {
        if (!check(n, m, val[i])) return false;
    }

    return true;
}

int main() {
    int t, ct = 0, n, m, i, j;

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &n, &m);
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                scanf("%d", &mat[i][j]);
            }
        }
        printf("Case #%d: %s\n", ++ct, solve(n, m) ? "YES" : "NO");
    }

    return 0;
}
