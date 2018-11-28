#include <cstdio>
#include <cstring>
#include <iostream>
#include <cassert>
using namespace std;

const int maxn = 1024;

struct Rectangle {
    int x1, y1, x2, y2;

    Rectangle() {}
    Rectangle(int x1, int y1, int x2, int y2): x1(x1), y1(y1), x2(x2), y2(y2) {}

    void in() {
        cin >> x1 >> y1 >> x2 >> y2;
    }
} block[maxn];

int g[maxn][maxn];
int dist[maxn];
int vis[maxn];

void solve() {
    int w, h, n;
    cin >> w >> h >> n;
    int nv = n + 2;
    int s = n, t = n + 1;
    for (int i = 0; i < n; ++i) {
        block[i].in();
    }
    for (int i = 0; i < nv; ++i) {
        for (int j = 0; j < nv; ++j) {
            g[i][j] = 1 << 28;
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int cost = max(0, max(block[j].x1 - block[i].x2 - 1, block[i].x1 - block[j].x2 - 1));
            cost = max(cost, max(0, max(block[j].y1 - block[i].y2 - 1, block[i].y1 - block[j].y2 - 1)));
            g[i][j] = g[j][i] = cost;
        }
        g[s][i] = g[i][s] = block[i].x1;
        g[i][t] = g[t][i] = w - 1 - block[i].x2;
    }
    g[s][t] = g[t][s] = w;
    /*
    for (int i = 0; i < nv; ++i) {
        for (int j = 0; j < nv; ++j) {
            cout << g[i][j] << ' ';
        }
        cout << endl;
    }
    */
    memset(vis, 0, sizeof(vis[0]) * nv);
    memset(dist, -1, sizeof(dist[0]) * nv);
    dist[s] = 0;
    for (int it = 0; it < nv; ++it) {
        int k = -1;
        for (int i = 0; i < nv; ++i) {
            if (dist[i] >= 0 && !vis[i] && (k == -1 || dist[i] < dist[k])) {
                k = i;
            }
        }
        assert(k != -1);
        //cout << k << ' ' << dist[k] << endl;
        if (k == t) {
            break;
        }
        vis[k] = 1;
        for (int i = 0; i < nv; ++i) {
            if (!vis[i] && (dist[i] == -1 || dist[k] + g[k][i] < dist[i])) {
                dist[i] = dist[k] + g[k][i];
            }
        }
    }

    printf("%d\n", dist[t]);
}

int main() {
    int T;
    cin >> T;
    for (int caseId = 1; caseId <= T; ++caseId) {
        printf("Case #%d: ", caseId);
        solve();
    }
}
