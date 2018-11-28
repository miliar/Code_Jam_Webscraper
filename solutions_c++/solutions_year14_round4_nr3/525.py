#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAXC = 555, MAXN = 111111, MAXM = 1111111, INF = 1000000000, dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};

bool u[MAXC][MAXC];
int cs, tot, s, t, id[MAXC][MAXC], d[MAXN], q[MAXN], g[MAXN], h[MAXN], p[MAXM], c[MAXM], nxt[MAXM];

inline void addedge(int x, int y, int z) {
    p[tot] = y, c[tot] = z, nxt[tot] = h[x], h[x] = tot++;
    p[tot] = x, c[tot] = 0, nxt[tot] = h[y], h[y] = tot++;
}

inline bool bfs() {
    memset(d, -1, sizeof d);
    int r = d[q[0] = s] = 0;
    for (int l = 0; l <= r; ++l)
        for (int k = h[q[l]]; ~k; k = nxt[k])
            if (c[k] && !~d[p[k]])
                d[q[++r] = p[k]] = d[q[l]] + 1;
    return ~d[t];
}

int dfs(int x, int ext) {
    if (x == t)
        return ext;
    int flow, ret = 0;
    for (int &k = g[x]; ~k; k = nxt[k])
        if (c[k] && d[p[k]] == d[x] + 1 && (flow = dfs(p[k], min(c[k], ext)))) {
            ret += flow, c[k] -= flow, c[k ^ 1] += flow;
            if (!(ext -= flow))
                return ret;
        }
    return ret;
}

inline void work() {
    int n, m, b;
    scanf("%d%d%d", &n, &m, &b);
    int e = n * m, idx = tot = 0, ans = 0;
    for (int i = 0; i <= n + 1; ++i)
        for (int j = 0; j <= m + 1; ++j)
            u[i][j] = true;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j) {
            u[i][j] = false;
            id[i][j] = ++idx;
        }
    while (b--) {
        int x1, y1, x2, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        for (int i = x1 + 1; i <= x2 + 1; ++i)
            for (int j = y1 + 1; j <= y2 + 1; ++j)
                u[i][j] = true;
    }
    s = 0, t = e + e + 1;
    memset(h, -1, sizeof h);
    for (int i = 1; i <= n; ++i) {
        if (!u[i][1])
            addedge(s, id[i][1], 1);
        if (!u[i][m])
            addedge(id[i][m] + e, t, 1);
    }
    for (int i = 1; i <= e; ++i)
        addedge(i, i + e, 1);
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            if (!u[i][j])
                for (int k = 0; k < 4; ++k) {
                    int x = i + dx[k], y = j + dy[k];
                    if (!u[x][y])
                        addedge(id[i][j] + e, id[x][y], 1);
                }
    while (bfs()) {
        memcpy(g, h, sizeof h);
        ans += dfs(s, INF);
    }
    printf("Case #%d: %d\n", ++cs, ans);
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--)
        work();
    return 0;
}
