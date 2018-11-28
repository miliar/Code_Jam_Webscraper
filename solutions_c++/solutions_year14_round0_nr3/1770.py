
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

struct result {
    bool a[5][5];
    int x, y;
} ans[6][6][25];

bool a[5][5];
int b[5][5];

bool check(bool a[][5], int b[][5], int n, int m, int x, int y) {
    int q[25][2];
    bool v[5][5];
    memset(v, false, sizeof(v));
    int h = 0, t = 1;
    q[0][0] = x;
    q[0][1] = y;
    v[x][y] = true;
    while (h < t) {
        int i = q[h][0], j = q[h][1];
        h ++;
        if (b[i][j] == 0) {
            for (int dx = -1; dx <= 1; dx ++) {
                for (int dy = -1; dy <= 1; dy ++) {
                    int ii = i + dx;
                    int jj = j + dy;
                    if (0 <= ii && ii < n && 0 <= jj && jj < m && ! v[ii][jj]) {
                        q[t][0] = ii;
                        q[t][1] = jj;
                        t ++;
                        v[ii][jj] = true;
                    }
                }
            }
        }
    }
    bool flag = true;
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++) {
            if (! a[i][j] && ! v[i][j]) {
                flag = false;
            }
        }
    }
    return flag;
}

void solve(int n, int m, int k) {
    for (int s = 0; s < (1 << (n * m)) - 1; s ++) {
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j ++) {
                if ((s & (1 << i * m + j)) == 0) {
                    a[i][j] = false;
                } else {
                    a[i][j] = true;
                }
            }
        }
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j ++) {
                b[i][j] = 0;
                for (int dx = -1; dx <= 1; dx ++) {
                    for (int dy = -1; dy <= 1; dy ++) {
                        int x = i + dx;
                        int y = j + dy;
                        if (0 <= x && x < n && 0 <= y && y < m && a[x][y]) {
                            b[i][j] ++;
                        }
                    }
                }
            }
        }
        int cnt = __builtin_popcount(s);
        if (k != -1 && cnt != k) {
            continue;
        }
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < m; j ++) {
                if (a[i][j]) continue;
                if (check(a, b, n, m, i, j)) {
                    memcpy(ans[n][m][cnt].a, a, sizeof(a));
                    ans[n][m][cnt].x = i;
                    ans[n][m][cnt].y = j;
                }
            }
        }
    }
}

int main() {
    //freopen("input.txt", "r", stdin);

    //solve(4, 5, 13);

    for (int n = 1; n <= 5; n ++) {
        for (int m = 1; m <= 5; m ++) {
            for (int i = 0; i < n * m; i ++) {
                ans[n][m][i].x = -1;
            }
            solve(n, m, -1);
            fprintf(stderr, "%d %d\n", n, m);
        }
    }

    int T;
    scanf("%d", &T);
    for (int no = 0; no < T; no ++) {
        printf("Case #%d:\n", no + 1);
        int r, c, m;
        scanf("%d%d%d", &r, &c, &m);
        if (ans[r][c][m].x == -1) {
            printf("Impossible\n");
        } else {
            for (int i = 0; i < r; i ++) {
                for (int j = 0; j < c; j ++) {
                    if (i == ans[r][c][m].x && j == ans[r][c][m].y) {
                        putchar('c');
                    } else if (ans[r][c][m].a[i][j]) {
                        putchar('*');
                    } else {
                        putchar('.');
                    }
                }
                putchar('\n');
            }
        }
    }


    return 0;
}