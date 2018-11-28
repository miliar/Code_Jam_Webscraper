#include <cstdio>

int main() {
    int T;
    int row1, a[5][5];
    int row2, b[5][5];
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &row1);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                scanf("%d", &a[i][j]);
        scanf("%d", &row2);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                scanf("%d", &b[i][j]);
        int cnt = 0, ans;
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                if (a[row1][i] == b[row2][j])
                    ++cnt, ans = a[row1][i];
        printf("Case #%d: ", t);
        if (cnt == 1)
            printf("%d\n", ans);
        else if (cnt > 1)
            puts("Bad magician!");
        else
            puts("Volunteer cheated!");

    }
}
