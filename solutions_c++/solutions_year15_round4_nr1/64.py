#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

int dy[] = {-1, 0, 1, 0};
int dx[] = {0, -1, 0, 1};
string d = "^<v>.";

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        int h, w; scanf("%d %d", &h, &w);
        char g[105][105];
        FO(y,0,h) scanf(" %s", g[y]);
        int r = 0;
        FO(y,0,h) FO(x,0,w) {
            int dir = d.find(g[y][x]);
            if (dir == 4) continue;

            bool good[4] = {};
            FO(i,0,4) {
                for (int p = 1;; p++) {
                    int cy = y+p*dy[i];
                    int cx = x+p*dx[i];
                    if (cy<0 || cy>=h || cx<0 || cx>=w) break;
                    if (g[cy][cx] != '.') {
                        good[i] = true;
                        break;
                    }
                }
            }
            if (good[dir]) continue;
            bool f = false;
            FO(i,0,4) if (good[i]) {
                r++;
                f = true;
                break;
            }
            if (!f) r = 1e9;
        }
        if (r < 1e8) printf("Case #%d: %d\n", Z, r);
        else printf("Case #%d: IMPOSSIBLE\n", Z);
    }
}

