#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 100003, maxm = maxn * 10, inf = 0x3f3f3f3f;
const int dx[] = {0, -1, 0, 1};
const int dy[] = {-1, 0, 1, 0};
int s, t, tt, h[maxn], to[maxm], nx[maxm], c[maxm], q[maxn], d[maxn];
bool g[100][500];
#define r1(i, j) (1 + (i) * m + (j))
#define r2(i, j) (1 + n * m + (i) * m + (j))
void add(int a, int b) {
    to[++tt] = b;
    c[tt] = 1;
    nx[tt] = h[a];
    h[a] = tt;
    to[++tt] = a;
    c[tt] = 0;
    nx[tt] = h[b];
    h[b] = tt;
}
bool bfs() {
    int l = 0, r = 1;
    for (int i = s ; i <= t ; ++i) d[i] = 0;
    q[0] = s;
    d[s] = 1;
    while (l < r) {
        int x = q[l++];
        for (int i = h[x] ; i ; i = nx[i]) {
            int y = to[i];
            if (d[y] || !c[i]) continue;
            d[y] = d[x] + 1;
            q[r++] = y;
            if (y == t) return true;
        }
    }
    return false;
}
int dfs(int x, int f) {
    if (x == t) return f;
    int k = f;
    for (int i = h[x] ; i ; i = nx[i]) {
        int y = to[i];
        if (d[y] != d[x] + 1 || !c[i]) continue;
        int z = dfs(y, min(c[i], k));
        k -= z;
        c[i] -= z;
        c[i ^ 1] += z;
        if (!k) return f;
    }
    if (k == f) d[x] = -1;
    return f - k;
}
int main() {
    int cas;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &cas);
    for (int c = 0 ; c < cas ; ++c) {
        int n, m, w, r = 0;
        scanf("%d%d%d", &n, &m, &w);
        for (int i = 0 ; i < n ; ++i)
            for (int j = 0 ; j < m ; ++j)
                g[i][j] = true;
        for (int i = 0 ; i < w ; ++i) {
            int x0, y0, x1, y1;
            scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
            for (int x = x0 ; x <= x1 ; ++x)
                for (int y = y0 ; y <= y1 ; ++y)
                    g[x][y] = false;
        }
        s = 1, t = n * m * 2 + 2, tt = 1;
        for (int i = s ; i <= t ; ++i) h[i] = 0;
        for (int i = 0 ; i < n ; ++i)
            for (int j = 0 ; j < m ; ++j)
                if (g[i][j]) {
                    add(r1(i, j), r2(i, j));
                    for (int k = 0 ; k < 4 ; ++k) {
                        int x = i + dx[k], y = j + dy[k];
                        if (0 <= x && x < n && 0 <= y && y < m && g[x][y]) add(r2(i, j), r1(x, y));
                    }
                }
        for (int i = 0 ; i < n ; ++i) {
            add(s, r1(i, 0));
            add(r2(i, m - 1), t);
        }
        while (bfs()) r += dfs(s, inf);
        printf("Case #%d: %d\n", c + 1, r);
    }
    return 0;
}
