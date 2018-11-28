#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, x;
        int use[20];
        memset(use, 0, sizeof(use));
        scanf("%d", &n);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &x);
                if (i == n) use[x]++;
            }
        }
        scanf("%d", &n);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                scanf("%d", &x);
                if (i == n) use[x]++;
            }
        }
        int ans = 0;
        for (int i = 1; i <= 16; i++) {
            if (use[i] == 2) {
                if (ans > 0 || ans == -1) ans = -1;
                else ans = i;
            }
        }
        printf("Case #%d: ", cas);
        if (ans == 0) puts("Volunteer cheated!");
        else if (ans == -1) puts("Bad magician!");
        else printf("%d\n", ans);
    }
    return 0;
}
