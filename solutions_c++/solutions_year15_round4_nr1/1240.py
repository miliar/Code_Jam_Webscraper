#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
using namespace std;
typedef long long LL;

int fx[] = {0, -1, 0, 1};
int fy[] = {-1, 0, 1, 0};
char op[] = "<^>v";

const int MAXN = 110;

char mat[MAXN][MAXN];
int n, m, T;

int getres(int r, int c) {
    if(mat[r][c] == '.') return 0;

    int f = strchr(op, mat[r][c]) - op, i = r + fx[f], j = c + fy[f];
    while(mat[i][j] == '.') i += fx[f], j += fy[f];
    if(mat[i][j]) return 0;

    for(f = 0; f < 4; ++f) {
        i = r + fx[f], j = c + fy[f];
        while(mat[i][j] == '.') i += fx[f], j += fy[f];
        if(mat[i][j]) return 1;
    }
    return -1;
}

int solve() {
    int res = 0;
    for(int i = 1; i <= n; ++i) {
        for(int j = 1; j <= m; ++j) {
            int t = getres(i, j);
            if(t == -1) return -1;
            res += t;
        }
    }
    return res;
}

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        scanf("%d%d", &n, &m);
        memset(mat, 0, sizeof(mat));
        for(int i = 1; i <= n; ++i)
            scanf("%s", mat[i] + 1);
        printf("Case #%d: ", t);
        int res = solve();
        if(res >= 0) printf("%d\n", res);
        else puts("IMPOSSIBLE");
    }
}
