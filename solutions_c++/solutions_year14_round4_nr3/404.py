#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

#define foreach(it, s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define X first
#define Y second

const int MAX_N = 512;
const int MAX_M = 100001;
const int MOD = 1e9 + 7.5;
const double EPS = 1e-8;

const int INF = 0x3f3f3f3f;
const int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

struct SAP {
    static const int MAX_N = 110001;
    static const int MAX_M = 1010001;
    int n, cnt, S, T;
    int adj[MAX_M], next[MAX_M], f[MAX_M];
    int g[MAX_N], h[MAX_N], vh[MAX_N], last[MAX_N];

    void init(int _n) {
        n = _n;
        S = n + 1, T = S + 1;
        n += 2;
        cnt = 0;
        memset(g, 255, sizeof(g));
    }

    void ins(int x, int y, int limit) {
        adj[cnt] = y;
        f[cnt] = limit;
        next[cnt] = g[x];
        g[x] = cnt++;

        adj[cnt] = x;
        f[cnt] = 0;
        next[cnt] = g[y];
        g[y] = cnt++;
    }

    int dfs(int node, int add) {
        if (node == T) return add;
        int minh = n + 1, p = last[node];
        if (p == -1) return 0;
        do {
            if (f[p] > 0) {
                int y = adj[p];
                if (h[node] == h[y] + 1) {
                    int temp = dfs(y, min(add, f[p]));
                    if (temp > 0) {
                        f[p] -= temp;
                        f[p ^ 1] += temp;
                        last[node] = p;
                        return temp;
                    }
                }
                if (h[S] >= n) return 0;
                minh = min(minh, h[y] + 1);
            }
            p = next[p];
            if (p == -1) p = g[node];
        } while (p != last[node]);

        if (--vh[h[node]] == 0) h[S] = n + 1;
        ++vh[h[node] = minh];
        return 0;
    }

    int maxflow() {
        memset(vh, 0, sizeof(vh));
        memset(h, 0, sizeof(h));
        for (int i = 0; i <= n; i++) last[i] = g[i];
        if (last[S] == -1) return 0;
        vh[0] = n;
        int flow = 0;
        while (h[S] < n) flow += dfs(S, INF);
        return flow;
    }
} g;

int n, m;
bool Map[MAX_N][MAX_N];

void cover(int x1, int y1, int x2, int y2) {
    for (int i = x1; i <= x2; i++) for (int j = y1; j <= y2; j++) Map[i][j] = false;
}

void init() {
    int t;
    int x1, y1, x2, y2;
    cin >> m >> n >> t;
    memset(Map, 1, sizeof(Map));
    for (int i = 0; i < t; i++) {
        cin >> y1 >> x1 >> y2 >> x2;
        cover(x1, y1, x2, y2);
    }
}

bool inrange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

void solve(int ca) {
    for (int i = 0; i < n; i++){
       // for (int j = 0; j < m; j++) cout << Map[i][j]; cout << endl;
    }
    g.init(n * m * 2);
    int T = n * m;
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (Map[i][j]) {
        g.ins(i * m + j, i * m + j + T, 1);
        int t = 0;
        for (int k = 0; k < 4; k++) {
            int x = i + dir[k][0], y = j + dir[k][1];
            if (inrange(x, y) && Map[x][y]) {
                g.ins(i * m + j + T, x * m + y, 1);
            }
        }
    }

    for (int i = 0; i < m; i++) if (Map[0][i]) g.ins(g.S, i, 1);
    for (int i = 0; i < m; i++) if (Map[n - 1][i]) g.ins((n - 1) * m + i + T, g.T, 1);
    printf("Case #%d: %d\n", ca, g.maxflow());
}

int main(){
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    int ca;
    cin >> ca;
    for (int i = 0; i < ca; i++) {
        init();
        solve(i + 1);
    }
    return 0;
}
