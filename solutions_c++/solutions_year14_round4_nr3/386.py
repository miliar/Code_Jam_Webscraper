#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

const int maxn = 2000 + 5;
const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};

struct Edge
{
    int u, c, f, p;
    Edge(int u, int c, int p): u(u), f(0), c(c), p(p) {}
};

vector<Edge> G[maxn * maxn];
bool used[maxn * maxn];
bool a[maxn][maxn];

void addEdge(int v, int u, int c)
{
    G[v].push_back(Edge(u, c, (int)G[u].size()));
    G[u].push_back(Edge(v, 0, (int)G[v].size() - 1));
}

int dfs(int v, int f, int flow)
{
    used[v] = true;
    if (v == f) {
        return flow;
    }
    for (int i = 0; i < (int)G[v].size(); ++i) {
        if (!used[G[v][i].u] && G[v][i].c - G[v][i].f > 0) {
            int fl = dfs(G[v][i].u, f, min(flow, G[v][i].c - G[v][i].f));
            if (fl) {
                G[v][i].f += fl;
                G[G[v][i].u][G[v][i].p].f -= fl;
                return fl;
            }
        }
    }
    return 0;
}

void solve(int testNum)
{
    int n, m, b;
    cin >> n >> m >> b;
    for (int i = 0; i < 2 * n * m + 2; ++i) {
        G[i].clear();
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            a[i][j] = false;
        }
    }
    for (int i = 0; i < b; ++i) {
        int x0, y0, x1, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        for (int x = x0; x <= x1; ++x) {
            for (int y = y0; y <= y1; ++y) {
                a[x][y] = true;
            }
        }
    }
    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < m; ++y) {
            for (int i = 0; i < 4; ++i) {
                int sx = x + dx[i];
                int sy = y + dy[i];
                if (sx < 0 || sy < 0 || sx >= n || sy >= m) {
                    continue;
                }
                if (!a[x][y] && !a[sx][sy]) {
                    addEdge(n * m + x * m + y, sx * m + sy, 1);
                }
            }
        }
    }
    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < m; ++y) {
            addEdge(x * m + y, n * m + x * m + y, 1);
        }
    }

    int s = 2 * n * m;
    int f = s + 1;
    for (int i = 0; i < n; ++i) {
        addEdge(s, i * m, 1);
        addEdge(n * m + i * m + m - 1, f, 1);
    } 

    int res = 0;
    while (true) {
        memset(used, false, 2 * n * m + 5);
        int fl = dfs(s, f, 1);
        if (!fl) {
            break;
        }
        res += fl;
    }
    printf("Case #%d: %d\n", testNum, res);
    fflush(stdout);
}


int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }
    
    return 0;
}
