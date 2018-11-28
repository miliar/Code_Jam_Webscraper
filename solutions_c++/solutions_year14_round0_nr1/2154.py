#include <cstdio>
int main()
{
    int T, Case = 1, r1, r2;
    int n;
    int row[4];
    freopen("A-small-attempt0.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);

    scanf("%d", &T);
    while (T--) {
        scanf("%d", &r1);
        --r1;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &n);
                if (i == r1)
                    row[j] = n;
            }
        scanf("%d", &r2);
        --r2;
        int nOfans = 0, ans;
        for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j) {
            scanf("%d", &n);
            if (i == r2) {
                for (int k = 0; k < 4; ++k)
                if (n == row[k]) {
                    ans = n;
                    ++nOfans;
                }
            }
        }
        printf("Case #%d: ", Case++);
        if (nOfans == 0) puts("Volunteer cheated!");
        else if (nOfans == 1) printf("%d\n", ans);
        else puts("Bad magician!");
    }
}
