#include <iostream>
#include <cstdio>
#include <cstring>

#define MAXV 40010
#define MAXE 1000010
#define INF 0x3F3F3F3F

using namespace std;

struct Edge {
    int u, v, flow, cost, next;
} edge[MAXE];

int head[MAXV], nEdge;
int dis[MAXV], cur[MAXV], que[MAXV * 10], front, rear;
bool vis[MAXV];

inline void init() {
	memset(head, -1, sizeof(head));
	nEdge = 0;
}

inline void addEdge(int a, int b, int f, int c) {
    edge[nEdge].u = a; edge[nEdge].v = b;
    edge[nEdge].flow = f;
    edge[nEdge].cost = c;
    edge[nEdge].next = head[a];
    head[a] = nEdge++;
    edge[nEdge].u = b; edge[nEdge].v = a;
    edge[nEdge].flow = 0;
    edge[nEdge].cost = -c;
    edge[nEdge].next = head[b];
    head[b] = nEdge++;
}

int dfs(int x, int dst, int pre) {
    int i, y, curFlow = pre, d;

    if (x == dst) return pre;
    for (vis[x] = true, i = cur[x]; ~i; i = edge[i].next) {
        if (edge[i].flow && !edge[i].cost && !vis[y = edge[i].v]) {
            cur[x] = i;
            d = dfs(y, dst, min(curFlow, edge[i].flow));
            edge[i].flow -= d; edge[i ^ 1].flow += d;
            if (!(curFlow -= d)) break;
        }
    }
    if (!curFlow) vis[x] = false;

    return pre - curFlow;
}

bool spfa(int v, int src, int dst) {
    int i, x, y;

    memset(dis, 0x3F, sizeof(dis));
    memset(vis, 0, sizeof(vis));
    front = rear = v;
    dis[src] = 0; vis[que[rear++] = src] = true;
    while (front < rear) {
        vis[x = que[front++]] = false;
        for (i = head[x]; ~i; i = edge[i].next) {
            if (edge[i].flow && dis[y = edge[i].v] > dis[x] + edge[i].cost) {
                dis[y] = dis[x] + edge[i].cost;
                if (!vis[y]) {
                    if (front < rear && dis[y] < dis[que[front]]) que[--front] = y;
                    else que[rear++] = y;
                    vis[y] = true;
                }
            }
        }
    }

    return dis[dst] < INF;
}

int minCostMaxFlow(int v, int src, int dst, int &netCost) {
    int i, d = 0, curFlow, totalFlow = 0;

    for (netCost = 0; spfa(v, src, dst); ) {
        //d += dis[dst];								// 最小费用最大流
        if ((d += dis[dst]) >= 0) break;			// 最小费用可行流
        for (i = 0; i < nEdge; ++i) edge[i].cost += dis[edge[i].u] - dis[edge[i].v];
        memcpy(cur, head, sizeof(head));
        memset(vis, 0, sizeof(vis));
        curFlow = dfs(src, dst, INF);
        totalFlow += curFlow; netCost += d * curFlow;
    }

    return totalFlow;
}

#define _A(x) ((x) * 3)
#define _B(x) ((x) * 3 + 1)
#define _C(x) ((x) * 3 + 2)

int val[MAXV];

int main() {
    int t, ct = 0, e, n, r, v, src, dst, i, ans;

    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        init();
        scanf("%d %d %d", &e, &r, &n);
        for (i = 0; i < n; ++i) scanf("%d", &val[i]);
        v = 3 * n + 2; src = 3 * n; dst = 3 * n + 1;
        for (i = 0; i < n; ++i) {
            addEdge(_A(i), _B(i), e, -val[i]);
            addEdge(_A(i), _C(i), e, 0);
            addEdge(src, _C(i), r, 0);
            addEdge(_B(i), dst, e, 0);
            if (i < n - 1) addEdge(_C(i), _A(i + 1), e, 0);
        }
        addEdge(src, _A(0), e, 0);
        addEdge(_C(n - 1), dst, e, 0);
        minCostMaxFlow(v, src, dst, ans);

        printf("Case #%d: %d\n", ++ct, -ans);
    }

    return 0;
}
