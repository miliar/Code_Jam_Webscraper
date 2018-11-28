#include <bits/stdc++.h>
using namespace std;

const int MAXN = 17;
int R, C;
bool dir[MAXN][MAXN];
int a[MAXN], b[MAXN];
bool vis[MAXN][MAXN][2];

bool valid(int x, int y, int p) {
    return x >= 0 && x < R && y >= 0 && y < C;
}

int getx(int ind) {
    if (ind <= C) return 0;
    if (ind <= C+R) return ind-C-1;
    if (ind <= C+R+C) return R-1;
    return 2*(R+C)-ind;
}
int gety(int ind) {
    if (ind <= C) return ind-1;
    if (ind <= C+R) return C-1;
    if (ind <= C+R+C) return (C+R+C)-ind;
    return 0;
}
int getp(int ind) {
    if (ind <= C) return 1;
    if (ind <= C+R) {
        int x = getx(ind);
        int y = gety(ind);
        return !dir[x][y];
    }
    if (ind <= C+R+C) return 0;
    int x = getx(ind);
    int y = gety(ind);
    return dir[x][y];
}

bool works() {
    memset(vis, 0, sizeof(vis));
    for (int i=0; i<R+C; i++) {
        int x = getx(a[i]);
        int y = gety(a[i]);
        int p = getp(a[i]);
        while (!vis[x][y][p]) {
            vis[x][y][p] = true;
            int nx = (p ? x-1 : x+1), ny = y, np = !p;
            if (valid(nx, ny, np) && !vis[nx][ny][np]) {
                x = nx;
                y = ny;
                p = np;
                continue;
            }
            nx = x;
            ny = ((dir[x][y]==p) ? y-1 : y+1);
            np = ((dir[x][y]^dir[nx][ny]) ? p : !p);
            if (valid(nx, ny, np) && !vis[nx][ny][np]) {
                x = nx;
                y = ny;
                p = np;
                continue;
            }
        }
        if (x != getx(b[i]) || y != gety(b[i]) || p != getp(b[i]))
            return false;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int kases; cin >> kases;
    for (int kase=1; kase<=kases; kase++) {
        cout << "Case #" << kase << ":\n";
        cin >> R >> C;
        for (int i=0; i<R+C; i++) {
            cin >> a[i] >> b[i];
        }
        bool good = false;
        for (int i=0; i<(1 << (R*C)); i++) {
            for (int j=0; j<R; j++) {
                for (int k=0; k<C; k++) {
                    if (i&(1 << (j*C + k)))
                        dir[j][k] = 1;
                    else
                        dir[j][k] = 0;
                }
            }
            if (works()) {
                good = true;
                for (int j=0; j<R; j++) {
                    for (int k=0; k<C; k++) {
                        cout << (dir[j][k] ? '/' : '\\');
                    }
                    cout << '\n';
                }
                break;
            }
        }
        if (!good) {
            cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}
