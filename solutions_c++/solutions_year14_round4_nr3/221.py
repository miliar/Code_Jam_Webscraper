#include <iostream>
#include <cstdio>
#include <cstring>

#define MAXV 100010
#define MAXE 2000010
#define INF 0x3F3F3F3F

using namespace std;

template<typename F = int>
struct MaxFlow {
    struct Edge {
        int u, v, nxt;
        F flow;
        Edge() {}
        Edge(int _u, int _v, int n, const F &f) :
            u(_u), v(_v), nxt(n), flow(f) {}
    } edge[MAXE];

    int head[MAXV], nV, nE;
    int dis[MAXV], pre[MAXV], cur[MAXV], cnt[MAXV], que[MAXV], front, rear;
    F his[MAXV];

    void init(int v) {
        memset(head, -1, sizeof(head));
        nV = v; nE = 0;
    }

    void addEdge(int a, int b, const F &f) {
        edge[nE] = Edge(a, b, head[a], f); head[a] = nE++;
        edge[nE] = Edge(b, a, head[b], 0); head[b] = nE++;
    }

    bool bfs(int src, int dst) {
        int i, x, y;

        memset(dis, 0x3F, sizeof(dis));
        memset(cnt, 0, sizeof(cnt));
        front = rear = 0;
        ++cnt[dis[src] = 0]; que[rear++] = src;
        while (front < rear) {
            for (i = head[x = que[front++]]; ~i; i = edge[i].nxt) {
                if (edge[i ^ 1].flow && dis[y = edge[i].v] > dis[x] + 1) {
                    ++cnt[dis[y] = dis[x] + 1]; que[rear++] = y;
                }
            }
        }

        return dis[dst] < nV;
    }

    F sap(int src, int dst) {
        int x, y, i, m;
        F curFlow = INF, totFlow = 0;
        bool tag;

        if (!bfs(dst, src)) return 0;
        memcpy(cur, head, sizeof(cur));
        for (x = src; dis[src] < nV; ) {
            his[x] = curFlow; tag = false;
            for (i = cur[x]; ~i; i = edge[i].nxt) {
                if (edge[i].flow && dis[y = edge[i].v] == dis[x] - 1) {
                    tag = true; pre[y] = cur[x] = i;
                    curFlow = min(curFlow, edge[i].flow);
                    if ((x = y) == dst) {
                        for (totFlow += curFlow; x != src; x = edge[pre[x]].u) {
                            edge[pre[x]].flow -= curFlow;
                            edge[pre[x] ^ 1].flow += curFlow;
                        }
                        curFlow = INF;
                    }
                    break;
                }
            }
            if (!tag) {
                for (m = nV, i = head[x]; ~i; i = edge[i].nxt) {
                    if (edge[i].flow && dis[y = edge[i].v] < m) {
                        m = dis[y]; cur[x] = i;
                    }
                }
                if (!(--cnt[dis[x]])) break;
                ++cnt[dis[x] = m + 1];
                if (x != src) curFlow = his[x = edge[pre[x]].u];
            }
        }

        return totFlow;
    }
};

MaxFlow<> graph;

int mat[512][512];

#define LL(x) ((x) << 1)
#define RR(x) (((x) << 1) | 1)

void visit(int x1, int y1, int x2, int y2) {
    int i, j;

    for (i = y1; i <= y2; ++i) {
        for (j = x1; j <= x2; ++j) {

            //printf("i = %d, j = %d\n", i, j);

            mat[i][j] = 1;
        }
    }
}

int main() {
    int t, ct = 0, w, h, b, i, j, x1, y1, x2, y2, v, src, dst;

    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        memset(mat, 0, sizeof(mat));
        scanf("%d%d%d", &w, &h, &b);
        v = w * h * 2 + 2; src = v - 2; dst = v - 1;
        graph.init(v);
        for (i = 0; i < b; ++i) {
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            //printf("i = %d, b = %d, w = %d, h = %d, [%d, %d], [%d, %d]\n", i, b, w, h, x1, y1, x2, y2);
            visit(x1, y1, x2, y2);
        }
        for (i = 0; i < w; ++i) {
            graph.addEdge(src, LL(i), 1);
            graph.addEdge(RR((h - 1) * w + i), dst, 1);
        }
        for (i = 0; i < h; ++i) {
            for (j = 0; j < w; ++j) {
                if (mat[i][j]) continue;
                graph.addEdge(LL(i * w + j), RR(i * w + j), 1);
                if (i > 0 && !mat[i - 1][j]) graph.addEdge(RR(i * w + j), LL((i - 1) * w + j), 1);
                if (i < h - 1 && !mat[i + 1][j]) graph.addEdge(RR(i * w + j), LL((i + 1) * w + j), 1);
                if (j > 0 && !mat[i][j - 1]) graph.addEdge(RR(i * w + j), LL(i * w + j - 1), 1);
                if (j < w - 1 && !mat[i][j + 1]) graph.addEdge(RR(i * w + j), LL(i * w + j + 1), 1);
            }
        }

        printf("Case #%d: %d\n", ++ct, graph.sap(src, dst));
    }

    return 0;
}
