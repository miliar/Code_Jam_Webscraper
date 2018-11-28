#include <bits/stdc++.h>

using namespace std;

struct Edge {
    int fr, to;
    int cap, flow;
    Edge() {}
    Edge(int fr, int to, int cap) : fr(fr), to(to), cap(cap) {
        flow = 0;
    }
};

struct Graph {
    vector<vector<int> > g;
    vector<Edge> e;
    int n;
    explicit Graph(int n) : n(n) {
        g.assign(n, vector<int>());
    }

    void addEdge(int fr, int to, int cap) {
        g[fr].push_back(e.size());
        e.push_back(Edge(fr, to, cap));
        g[to].push_back(e.size());
        e.push_back(Edge(to, fr, 0));
    }

    int maxFlow(int s, int t) {
        int flow = 0;

        while (1) {
            vector<char> d(n, 0);
            d[s] = 1;
            vector<int> p(n, -1);
            queue<int> q;
            q.push(s);
            while (!q.empty()) {
                int v = q.front();
                q.pop();

                for (int ed : g[v]) {
                    Edge &edge = e[ed];
                    if (!d[edge.to] && edge.cap - edge.flow > 0) {
                        d[edge.to] = 1;
                        q.push(edge.to);
                        p[edge.to] = ed;
                    }
                }
            }


            if (d[t] == 0) {
                break;
            }

            int addFlow = 1;
            for (int v = t; v != s; v = e[p[v]].fr) {
                e[p[v]].flow += addFlow;
                e[p[v] ^ 1].flow -= addFlow;
            }
            flow += addFlow;
        }
        return flow;
    }
};

inline void solve(int test) {
    int n, m;
    cin >> n >> m;
    int b;
    cin >> b;
    char used[n][m];
    memset(used, 0, sizeof(used));
    for (int i = 0; i < b; ++i) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        for (int j = x1; j <= x2; ++j) {
            for (int k = y1; k <= y2; ++k) {
                used[j][k] = 1;
            }
        }
    }

    Graph g(2 * n * m + 2);
    int s = 2 * n * m;
    int t = 2 * n * m + 1;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (used[i][j]) {
                continue;
            }
            int v = 2 * (i * m + j);
            int v2 = v + 1;
            g.addEdge(v, v2, 1);
        }
    }

    int dx[] = {1, 0, -1, 0};
    int dy[] = {0, 1, 0, -1};

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (used[i][j]) {
                continue;
            }
            int v = 2 * (i * m + j) + 1;
            for (int k = 0; k < 4; ++k) {
                int tox = i + dx[k];
                int toy = j + dy[k];
                if (tox >= 0 && tox < n && toy >= 0 && toy < m) {
                    if (!used[tox][toy]) {
                        int v2 = 2 * (tox * m + toy);
                        g.addEdge(v, v2, 1);
                    }
                }
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        int v = 2 * (i * m);
        g.addEdge(s, v, 1);
    }
    for (int i = 0; i < n; ++i) {
        int v = 2 * (i * m + m - 1) + 1;
        g.addEdge(v, t, 1);
    }
    int ans = g.maxFlow(s, t);
    cout << "Case #" << test << ": " << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("out", "w", stdout);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cerr << i << endl;
        solve(i + 1);
    }

    return 0;
}
