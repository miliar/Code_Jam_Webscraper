#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 32

using namespace std;

int mat[MAX][MAX], cnt[MAX];

int main() {
    int t, ct = 0, l, i, j, ans;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        memset(cnt, 0, sizeof(cnt));
        scanf("%d", &l);
        for (i = 1; i <= 4; ++i) {
            for (j = 1; j <= 4; ++j) {
                scanf("%d", &mat[i][j]);
            }
        }
        for (i = 1; i <= 4; ++i) ++cnt[mat[l][i]];
        scanf("%d", &l);
        for (i = 1; i <= 4; ++i) {
            for (j = 1; j <= 4; ++j) {
                scanf("%d", &mat[i][j]);
            }
        }
        for (i = 1; i <= 4; ++i) ++cnt[mat[l][i]];
        for (ans = 0, i = 1; i <= 16; ++i) {
            if (cnt[i] > 1) {
                if (ans) ans = -1;
                else ans = i;
            }
        }
        printf("Case #%d: ", ++ct);
        if (ans > 0) printf("%d\n", ans);
        else if (!ans) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }

    return 0;
}
