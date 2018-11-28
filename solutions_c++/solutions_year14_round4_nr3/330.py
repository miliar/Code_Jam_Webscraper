#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)

struct Flow {
    struct Edge {
        int end;
        int capacity;
        int flow;
        Edge(int end, int capacity, int flow):
            end(end), capacity(capacity), flow(flow)
        { }
    };

    vector<vector<int>> graph;
    vector<Edge> edges;

    void addEdge(int from, int to, int capacity) {
        size_t mx = max(from, to);
        while (graph.size() <= mx) {
            graph.emplace_back();
        }
        graph[from].push_back(edges.size());
        edges.emplace_back(to, capacity, 0);
        graph[to].push_back(edges.size());
        edges.emplace_back(from, 0, 0);
    }

    int run(int source, int sink) {
        const int INF = 2147483647;
        int n = (int) graph.size();

        vector<int> dij(n);
        vector<int> prev(n);
        vector<int> q;
        q.reserve(n);

        int totalFlow = 0;

        while (true) {
            dij.assign(n, INF);
            prev.assign(n, -1);

            dij[source] = 0;

/*            auto upd = true;
            while (upd) {
                upd = false;
                for (auto i = 0; i < n; i++) {
                    for (auto ei : graph[i]) {
                        auto& edge = edges[ei];
                        if (edge.capacity <= edge.flow) continue;
                        auto dist = dij[i];
                        if (dist == INF) continue;
                        auto end = edge.end;
                        if (dij[end] > dist) {
                            upd = true;
                            dij[end] = newDist;
                            prev[end] = ei;
                        }
                    }
                }
            }*/

            q.clear();
            q.push_back(source);
            int qb = 0;
            while (qb < (int) q.size()) {
                int v = q[qb++];
                for (auto ei : graph[v]) {
                    auto& edge = edges[ei];
                    if (edge.capacity <= edge.flow) continue;
                    auto end = edge.end;
                    if (prev[end] == -1) {
                        prev[end] = ei;
                        q.push_back(end);
                    }
                }
            }

            if (prev[sink] == -1) break;

            auto cur = sink;
            int push = INF;
            while (cur != source) {
                auto ei = prev[cur];
                auto& edge = edges[ei];
                push = min(push, edge.capacity - edge.flow);
                cur = edges[ei ^ 1].end;
            }
            cur = sink;
            while (cur != source) {
                auto ei = prev[cur];
                edges[ei].flow += push;
                auto& revEdge = edges[ei ^ 1];
                revEdge.flow -= push;
                cur = revEdge.end;
            }

            totalFlow += push;
        }

        return totalFlow;
    }
};

const int DX[] = {1, 0, -1, 0};
const int DY[] = {0, 1, 0, -1};

int n, m;
char board[104][504];

int enc(int x, int y) { return 2 * (x + y*n) + 1; }

void debug(const Flow& f) {
    forn(i, (int) f.graph.size()) {
        auto& v = f.graph[i];
        for (auto ei : v) {
            auto& edge = f.edges[ei];
            printf("%d -> %d, cap %d flow %d\n", i, edge.end, edge.capacity, edge.flow);
        }
    }
}

int main() {
    int __;
    scanf("%d", &__);
    forn(_, __) {
        int bs;
        scanf("%d%d%d", &n, &m, &bs);
        memset(board, 0, sizeof board);
        forn(i, bs) {
            int x1, y1, x2, y2;
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for (int x = x1; x <= x2; x++)
                for (int y = y1; y <= y2; y++)
                    board[x][y] = 1;
        }
// forn(i, n) { forn(j, m) printf("%c", board[i][j] ? 'X' : '.'); puts(""); }
        Flow f;
        forn(x, n) forn(y, m) {
            if (board[x][y]) continue;
            f.addEdge(enc(x, y), enc(x, y) + 1, 1);
            forn(d, 4) {
                int xx = x + DX[d], yy = y + DY[d];
                if (!(0 <= xx && xx < n && 0 <= yy && yy < m)) continue;
                if (board[xx][yy]) continue;
                f.addEdge(enc(x, y) + 1, enc(xx, yy), 1);
            }
        }
        auto sink = enc(n-1, m-1) + 2;
        forn(x, n) {
            f.addEdge(0, enc(x, 0), 1);
            f.addEdge(enc(x, m - 1) + 1, sink, 1);
        }
        auto res = f.run(0, sink);
        // debug(f);
        printf("Case #%d: %d\n", _+1, res);
        if (res == 100) printf("%d %d %d\n", n, m, bs);
    }
    return 0;
}
