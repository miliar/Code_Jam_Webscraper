#include <bits/stdc++.h>
using namespace std;

int n;
int use1[100], use2[100];
int g[100][100], g2[100][100];

bool dfs(int st, int ed) {
    if (st == ed) {
        return true;
    }
    for (int i = 0; i < n; i++) {
        if (!use1[i]) {
            use1[i] = 1;
            bool sol = false;
            for (int j = 0; j < n; j++) {
                if (!use2[j] && g2[i][j]) {
                    sol = true;
                    use2[j] = 1;
                    if (!dfs(st + 1, ed)) {
                        return false;
                    }
                    use2[j] = 0;
                }
            }
            if (sol == false) {
                return false;
            }
            use1[i] = 0;
        }
    }
    return true;
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            char s[110];
            scanf("%s", s);
            for (int j = 0; j < n; j++) {
                if (s[j] == '1') {
                    g[i][j] = 1;
                } else {
                    g[i][j] = 0;
                }
            }
        }
        int res = 100000;
        for (int i = 0; i < 1 << (n * n); i++) {
            int tmp = __builtin_popcount(i);
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    g2[j][k] = g[j][k];
                    int id = j * n + k;
                    if (i & (1 << id)) {
                        g2[j][k] = 1;
                    }
                }
            }
            memset(use1, 0, sizeof(use1));
            memset(use2, 0, sizeof(use2));
            if (dfs(0, n)) {
                res = min(res, tmp);
            }
        }
        printf("Case #%d: %d\n", cas, res);
        fprintf(stderr, "Case #%d: %d\n", cas, res);
    }
    return 0;
}