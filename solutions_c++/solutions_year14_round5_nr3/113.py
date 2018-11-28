#include <bits/stdc++.h>
using namespace std;

int use[2010], dp[20][1 << 15];
char s[20][20];
int tid[20], id[20];

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n;
        scanf("%d", &n);
        memset(use, -1, sizeof(use));
        int now = 0;
        for (int i = 0; i < n; i++) {
            scanf("%s%d", s[i], &tid[i]);
            if (tid[i] == 0) continue;
            if (use[tid[i]] == -1) {
                use[tid[i]] = now++;
            }
            id[i] = use[tid[i]];
        }
        now = 15;
        memset(dp, 0, sizeof(dp));
        for (int j = 0; j < (1 << now); j++) {
            dp[0][j] = 1;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < (1 << now); j++) {
                if (dp[i][j] == 0) continue;
                if (s[i][0] == 'E') {
                    if (tid[i] == 0) {
                        for (int k = 0; k < now; k++) {
                            if (!(j & (1 << k))) {
                                dp[i + 1][j ^ (1 << k)] = 1;
                            }
                        }
                    } else {
                        if (!(j & (1 << id[i]))) {
                            dp[i + 1][j ^ (1 << id[i])] = 1;
                        }
                    }
                } else {
                    if (tid[i] == 0) {
                        for (int k = 0; k < now; k++) {
                            if ((j & (1 << k))) {
                                dp[i + 1][j ^ (1 << k)] = 1;
                            }
                        }
                    } else {
                        if ((j & (1 << id[i]))) {
                            dp[i + 1][j ^ (1 << id[i])] = 1;
                        }
                    }
                }
            }
        }
        int ans = -1;
        for (int i = 0; i < (1 << now); i++) {
            if (dp[n][i] == 1) {
                int tmp = __builtin_popcount(i);
                if (ans == -1 || ans > tmp) ans = tmp;
            }
        }
        if (ans != -1)
            printf("Case #%d: %d\n", cas, ans);
        else
            printf("Case #%d: CRIME TIME\n", cas);
    }
    return 0;
}
