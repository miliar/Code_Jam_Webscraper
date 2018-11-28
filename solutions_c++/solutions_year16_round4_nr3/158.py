#include <bits/stdc++.h>
using namespace std;
const int MAXN  = 20;
int g[MAXN][MAXN][4], p[100], a[100], b[100], m[100], R, C, TC;
int par(int x) {
    if (p[x] == x) return x;
    else return p[x] = par(p[x]);
}
void merge(int x, int y) {
    x = par(x), y = par(y);
    if (x == y) return;
    p[x] = y;
}
int main () {
    scanf("%d", &TC);
    for (int T = 1; T <= TC; ++T) {
        scanf("%d%d", &R, &C);
        for (int i = 0; i < R+C; ++i) scanf("%d%d", &a[i], &b[i]);
        
        memset(g, -1, sizeof g);
        int cnt = 0;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (i) g[i][j][0] = g[i-1][j][2];
                if (j) g[i][j][1] = g[i][j-1][3];
                for (int k = 0; k < 4; ++k) {
                    if (g[i][j][k] == -1) g[i][j][k] = cnt++;
                }
            }
        }
        int c1 = 0;
        for (int i = 0; i < C; ++i) m[++c1] = g[0][i][0];
        for (int i = 0; i < R; ++i) m[++c1] = g[i][C-1][3];
        for (int i = C-1; i >= 0; --i) m[++c1] = g[R-1][i][2];
        for (int i = R-1; i >= 0; --i) m[++c1] = g[i][0][1];
        //printf("C1 = %d, R = %d, C = %d\n", c1, R, C);
        for (int i = 0; i < R+C; ++i) a[i] = m[a[i]], b[i] = m[b[i]];
        
        //printf("%d borders created.", cnt);
        bool ok = 0;
        printf("Case #%d:\n", T);
        for (int bs = 0; bs < (1<<(R*C)); ++bs) {
            for (int i = 0; i < cnt; ++i) p[i] = i;
            for (int i = 0; i < R; ++i) {
                for (int j = 0; j < C; ++j) {
                    int z = i*C + j;
                    if (bs & (1<<z)) merge(g[i][j][0], g[i][j][1]), merge(g[i][j][2], g[i][j][3]);
                    else merge(g[i][j][0], g[i][j][3]), merge(g[i][j][1], g[i][j][2]);
                }
            }
            bool fail = 0;
            for (int i = 0; i < R+C && !fail; ++i) {
                //printf("pair %d %d\n", a[i], b[i]);
                for (int j = 0; j < R+C && !fail; ++j) {
                    if (i == j) continue;
                    if (par(a[i]) == par(a[j])) fail = 1;
                    if (par(b[i]) == par(b[j])) fail = 1;
                }
                if (par(a[i]) != par(b[i])) fail = 1;
            }
            if (!fail) {
                ok = 1;
                for (int i = 0; i < R; ++i) {
                    for (int j = 0; j < C; ++j) {
                        int z = i*C + j;
                        if (bs & (1<<z)) printf("/");
                        else printf("\\");
                    }
                    puts("");
                }
                break;
            }
        }
        if (!ok) printf("IMPOSSIBLE\n");
    }
}