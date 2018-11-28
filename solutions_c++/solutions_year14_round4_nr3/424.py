#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

const int INF = 1 << 28;

const int dx[] = {1, 0, -1,  0};
const int dy[] = {0, 1,  0, -1};

int fst[200500];
int nxt[9000800];
int end[9000800];
int cap[9000800];
int edges = 0;

inline void addEdge(int u, int v, int c, bool rev = true) {
    if (rev) {
        addEdge(u, v, c, false);
        addEdge(v, u, 0, false);
    } else {
        nxt[edges] = fst[u];
        end[edges] = v;
        cap[edges] = c;
        fst[u] = edges++;
    }
}

int step;
int was[250500];
bool dfs(int v, int dst, int &amin) {
    if (v == dst) {
        return true;
    }
    was[v] = step;
    for (int i = fst[v]; i != -1; i = nxt[i]) {
        int to = end[i];
        if (cap[i] > 0 && was[to] != step) {
            int cmin = min(amin, cap[i]);
            if (dfs(to, dst, cmin)) {
                amin = cmin;
                cap[i] -= cmin;
                cap[i ^ 1] += cmin;
                return true;
            }
        }
    }
    return false;
}

int w, h;
bool a[505][505];
inline int get(int x, int y) {
    return x * h + y;
}

int main() {
    int nt;
    assert(scanf("%d", &nt) == 1);
    for (int tt = 1; tt <= nt; tt++) {
        fprintf(stderr, "test %d\n", tt);
        int b;
        assert(scanf("%d%d%d", &w, &h, &b) == 3);
        for (int x = 0; x < w; x++) {
            for (int y = 0; y < h; y++) {
                a[x][y] = 0;
            }
        }
        for (int i = 0; i < b; i++) {
            int x0, y0, x1, y1;
            assert(scanf("%d%d%d%d", &x0, &y0, &x1, &y1) == 4);
            for (int x = x0; x <= x1; x++) {
                for (int y = y0; y <= y1; y++) {
                    a[x][y] = 1;
                }
            }
        }
        int source = 2 * w * h;
        int sink = source + 1;
        edges = 0;
        for (int i = 0; i < sink + 1; i++) {
            fst[i] = -1;
        }
        for (int x = 0; x < w; x++) {
            if (!a[x][0]) {
                addEdge(source, get(x, 0), 1);
            }
            if (!a[x][h - 1]) {
                addEdge(get(x, h - 1) + w * h, sink, 1);
            }
        }
        for (int x = 0; x < w; x++) {
            for (int y = 0; y < h; y++) {
                if (a[x][y]) {
                    continue;
                }
                int u = get(x, y);
                addEdge(u, u + w * h, 1);
                for (int dir = 0; dir < 4; dir++) {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    if (0 <= nx && nx < w && 0 <= ny && ny < h && !a[nx][ny]) {
                        int v = get(nx, ny);
                        addEdge(u + w * h, v, 1);
                    }
                }
            }
        }
        int ans = 0;
        step++;
        for (int mdst = INF; dfs(source, sink, mdst); mdst = INF) {
            step++;
            ans += mdst;
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
