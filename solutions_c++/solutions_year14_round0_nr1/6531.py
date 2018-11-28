#include <stdio.h>

int main() {
    freopen("x.txt", "r", stdin);
    freopen("w.txt", "w", stdout);

    int cas;
    scanf("%d", &cas);
    for (int re = 1; re <= cas; re++) {
        int b[20] = {0};
        for (int r = 1; r <= 2; r++) {
            int k, m;
            scanf("%d", &k);
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    scanf("%d", &m);
                    if (i + 1 == k) {
                        b[m]++;
                    }
                }
            }

        }
        int ans = -1;
        for (int i = 1; i <= 16; i++) {
            if (b[i] == 2) {
                if (ans == -1) {
                    ans = i;
                } else {
                    ans = -2;
                }
            }
        }
        if (ans == -1) {
            printf("Case #%d: Volunteer cheated!\n", re);
        } else if (ans == -2){
            printf("Case #%d: Bad magician!\n", re);
        } else {
            printf("Case #%d: %d\n", re, ans);
        }
    }
}
