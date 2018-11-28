#include <bits/stdc++.h>
using namespace std;

char s[110][110];
int a[110][110][4];
int wayx[10] = {-1, 0, 0, 1};
int wayy[10] = {0, -1, 1, 0};

int getId(char c) {
    if (c == '^') return 0;
    if (c == '<') return 1;
    if (c == '>') return 2;
    return 3;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%s", s[i]);
        }
        memset(a, 0, sizeof(a));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (s[i][j] != '.') {
                    for (int k = 0; k < 4; k++) {
                        int x = i + wayx[k], y = j + wayy[k];
                        bool sol = true;
                        while (x >= 0 && x < n && y >= 0 && y < m) {
                            if (s[x][y] != '.') {
                                sol = false;
                            }
                            x += wayx[k];
                            y += wayy[k];
                        }
                        if (sol == true) {
                            a[i][j][k] = 1;
                        }
                    }
                }
            }
        }
        bool sol = true;
        int res = 0;
        for (int i = 0; i < n && sol; i++) {
            for (int j = 0; j < m && sol; j++) {
                if (s[i][j] != '.') {
                    int cur = getId(s[i][j]);
                    if (a[i][j][cur] == 0) {
                        continue;
                    }
                    sol = false;
                    for (int k = 0; k < 4; k++) {
                        if (a[i][j][k] == 0) {
                            sol = true;
                        }
                    }
                    if (sol) {
                        res++;
                    }
                }
            }
        }
        printf("Case #%d: ", cas);
        if (!sol) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", res);
            fprintf(stderr, "%d\n", res);
        }
    }
    return 0;
}