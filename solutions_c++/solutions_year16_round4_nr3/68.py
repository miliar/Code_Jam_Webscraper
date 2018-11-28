#include <bits/stdc++.h>
using namespace std;

int a[20][20][4];
int fa[10000], t_fa[10010];
int from[1000];
int use[1000];
int b[10000];

int find_fa(int x) {
    if (fa[x] == x) {
        return x;
    }
    return fa[x] = find_fa(fa[x]);
}

void get(int u, int v) {
    int ru = find_fa(u);
    int rv = find_fa(v);
    fa[ru] = rv;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int R, C;
        scanf("%d%d", &R, &C);
        int cnt = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                for (int k = 0; k < 4; k++) {
                    a[i][j][k] = cnt++;
                }
            }
        }
        for (int i = 0; i < cnt; i++) {
            fa[i] = i;
        }
        int tcnt = 0;
        for (int i = 0; i < C; i++) {
            from[tcnt++] = a[0][i][1];
        }
        for (int i = 0; i < R; i++) {
            from[tcnt++] = a[i][C - 1][2];
        }
        for (int i = C - 1; i >= 0; i--) {
            from[tcnt++] = a[R - 1][i][3];
        }
        for (int i = R - 1; i >= 0; i--) {
            from[tcnt++] = a[i][0][0];
        }
        // Row;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j + 1 < C; j++) {
                get(a[i][j][2], a[i][j + 1][0]);
            }
        }
        // Col
        for (int i = 0; i + 1 < R; i++) {
            for (int j = 0; j < C; j++) {
                get(a[i][j][3], a[i + 1][j][1]);
            }
        }
        for (int i = 0; i < (R + C) * 2; i++) {
            scanf("%d", &b[i]);
            b[i]--;
        }
        string res = "";
        for (int i = 0; i < (1 << (R * C)); i++) {
            //printf("i = %d\n", i);
            for (int j = 0; j < cnt; j++) {
                t_fa[j] = fa[j];
            }
            string tmp = "";
            for (int j = 0; j < R * C; j++) {
                int row = j / C, col = j % C;
                if (i & (1 << j)) { // This is a "/"
                    tmp += "/";
                    get(a[row][col][0], a[row][col][1]);
                    get(a[row][col][2], a[row][col][3]);
                } else { // This is a "\"
                    tmp += "\\";
                    get(a[row][col][0], a[row][col][3]);
                    get(a[row][col][1], a[row][col][2]);
                }
            }
            //printf("%s\n", tmp.c_str());

            memset(use, 0, sizeof(use));
            bool sol = true;
            for (int i = 0; i < (R + C) * 2; i += 2) {
                int r1 = find_fa(from[b[i]]);
                int r2 = find_fa(from[b[i + 1]]);
                //printf("%d %d\n", r1, r2);
                if (r1 != r2 || use[r1]) {
                    sol = false;
                }
                use[r1] = 1;
            }

            if (sol) {
                res = tmp;
                break;
            }
            for (int j = 0; j < cnt; j++) {
                fa[j] = t_fa[j];
            }
        }
        printf("Case #%d:\n", cas);
        fprintf(stderr, "Case #%d:\n", cas);
        if (res != "") {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    printf("%c", res[i * C + j]);
                    fprintf(stderr, "%c", res[i * C + j]);
                }
                puts("");
                fprintf(stderr, "\n");
            }
        } else {
            puts("IMPOSSIBLE");
            fprintf(stderr, "IMPOSSIBLE\n");
        }
    }
    return 0;
}