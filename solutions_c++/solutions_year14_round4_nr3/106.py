#include <set>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cassert>
using namespace std;

const int maxn = 1024;
int G[maxn][maxn];

struct Block {
    int x0, y0, x1, y1;
    void input() { scanf("%d%d%d%d", &x0, &y0, &x1, &y1);  }
    int dist(const Block& b) {
        return max(dist_seg(x0, x1, b.x0, b.x1), dist_seg(y0, y1, b.y0, b.y1)) - 1;
    }

    int dist_seg(int a, int b, int c, int d) {
        if (b < c || d < a) {
            if (a < c) {
                return c - b;
            }  else {
                return a - d;
            }
        } else { // have common part
            return 0;
        }
    }
        
} blocks[maxn];

int dist[maxn];
bool vis[maxn];

int solve() {
    memset(G, 100, sizeof(G)); // fill a big number
    memset(dist, 100, sizeof(dist));
    memset(vis, 0, sizeof(vis));

    int n, w, h;
    scanf("%d%d%d", &w, &h, &n);
    for (int i = 0; i < n; ++i) {
        blocks[i].input();
    }

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int d = blocks[i].dist(blocks[j]);
            G[i][j] = G[j][i] = d;
        }
    }

    int s = n, t = n + 1;
    for (int i = 0; i < n; ++i) {
        G[i][s] = G[s][i] = blocks[i].x0;
        G[i][t] = G[t][i] = w - 1 - blocks[i].x1;
        G[i][i] = 0;
    }
    G[s][t] = G[t][s] = w;
    G[s][s] = G[t][t] = 0;

    n += 2;

    
    /*for (int i = 0; i < n; ++i)  {
        for (int j = 0; j < n; ++j) {
            printf("%d ", G[i][j]);
        }
        printf("\n");
        }*/


    // dijk
    dist[s] = 0;
    while (true) {
        int k = -1;
        int mind = -1;
        for (int i = 0; i < n; ++i)
            if (!vis[i])
                if (k == -1 || mind > dist[i]) {
                    k = i;
                    mind = dist[i];
                }
        if (k == -1) break;
        vis[k] = true;
        for (int i = 0; i < n; ++i)
            if (!vis[i]) {
                int nd = mind + G[k][i];
                if (nd < dist[i]) dist[i] = nd;
                if (nd < 0) {
                    fprintf(stderr, "nd=%d G[k][i]=%d\n", nd, G[k][i]);                   
                }
            }
    }
    

    return dist[t];
}

int main() {
    freopen("C-large.in", "r", stdin);
    int T;
    scanf("%d", &T);
    for (int i  = 1; i <= T; ++i)  {
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}
