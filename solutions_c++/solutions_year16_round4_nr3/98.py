#include <bits/stdc++.h>

using namespace std;

const int N = 128;
const int U = 0;
const int D = 1;
const int L = 2;
const int _R = 3;

struct Where {
    int x, y, z;

    Where(int x, int y, int z): x(x), y(y), z(z) {}

    Where() {}
};

bool g[N][N][4][4];
bool vis[N][N][4];
char mat[N][N];
int pairs[N * 4];
Where where[N * 4];
int R, C;

void dfs(int x, int y, int z) {
    if (x < 0 || y < 0 || x >= R || y >= C) return;
    if (vis[x][y][z]) return;
    vis[x][y][z] = true;
    for (int i = 0; i < 4; ++i) {
        if (g[x][y][z][i]) {
            dfs(x, y, i);
        }
    }
    if (z == U) dfs(x - 1, y, D);
    if (z == D) dfs(x + 1, y, U);
    if (z == L) dfs(x, y - 1, _R);
    if (z == _R) dfs(x, y + 1, L);
}

void solve() {
    cin >> R >> C;
    for (int i = 0; i < (R + C) * 2; ++i) {
        cin >> pairs[i];
    }
    int cnt = 1;
    for (int i = 0; i < C; ++i) where[cnt++] = Where(0, i, U);
    for (int i = 0; i < R; ++i) where[cnt++] = Where(i, C - 1, _R);
    for (int i = C - 1; i >= 0; --i) where[cnt++] = Where(R - 1, i, D);
    for (int i = R - 1; i >= 0; --i) where[cnt++] = Where(i, 0, L);
    /*
    for (int i = 1; i <= 2 * (R + C); ++i) {
        cout << where[i].x << ' ' << where[i].y << ' ' << where[i].z << endl;
    }
    */
    for (int mask = 0; mask < 1 << R * C; ++mask) {//cerr << mask << endl;
        int pos = 0;
        memset(g, 0, sizeof g);
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (mask >> pos & 1) {
                    mat[i][j] = '/';
                    g[i][j][U][L] = true;
                    g[i][j][L][U] = true;
                    g[i][j][D][_R] = true;
                    g[i][j][_R][D] = true;
                } else {
                    mat[i][j] = '\\';
                    g[i][j][U][_R] = true;
                    g[i][j][_R][U] = true;
                    g[i][j][D][L] = true;
                    g[i][j][L][D] = true;
                }
                pos++;
            }
        }
        bool ok = true;
        for (int i = 0; i < (R + C) * 2; i += 2) {
            memset(vis, false, sizeof vis);
            dfs(where[pairs[i]].x, where[pairs[i]].y, where[pairs[i]].z);
            if (!vis[where[pairs[i + 1]].x][where[pairs[i + 1]].y][where[pairs[i + 1]].z]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            for (int i = 0; i < R; ++i) {
                for (int j = 0; j < C; ++j) {
                    cout << mat[i][j];
                }
                cout << endl;
            }
            return;
        }
    }
    cout << "IMPOSSIBLE" << endl;
}

int main() {
    int testCount;
    cin >> testCount;
    for (int testId = 1; testId <= testCount; ++testId) {
        printf("Case #%d:\n", testId);
        solve();
        fflush(stdout);
        fprintf(stderr, "%d = %.15f\n", testId, clock() / (double) CLOCKS_PER_SEC);
    }
}

