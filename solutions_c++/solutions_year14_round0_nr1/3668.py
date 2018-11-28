#include <cstdio>

void jizz() {
    int x[2];
    int arr[2][4][4];

    for (int i = 0; i < 2; ++i) {
        scanf("%d", &x[i]); x[i] -= 1;

        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
                scanf("%d", &arr[i][j][k]);
    }

    int ans = -1, ans_cnt = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j)
            if (arr[0][x[0]][i] == arr[1][x[1]][j])
                ans = arr[0][x[0]][i], ans_cnt += 1;
    }

    if (ans_cnt == 1) printf("%d\n", ans);
    else if (ans_cnt == 0) puts("Volunteer cheated!");
    else puts("Bad magician!");
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        jizz();
    }

    return 0;
}
