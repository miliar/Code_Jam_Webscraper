#include <cstdio>
int arr[17];
int main() {
    int tests;
    scanf("%d", &tests);
    for (int t = 1; t <= tests; t++) {
        for (int i = 1; i <= 16; i++) {
            arr[i] = 0;
        }
        for (int k = 0; k < 2; k++) {
            int row, num;
            scanf("%d", &row);
            for (int i = 1; i <= 4; i++) {
                for (int j = 1; j <= 4; j++) {
                    scanf("%d", &num);
                    if (i == row) {
                        arr[num]++;
                    }
                }
            }
        }
        int hwm = 0;
        int ans = -1;

        for (int i = 1; i <= 16; i++) {
            if (arr[i] == 2) {
                hwm++;
                ans = i;
            }
        }
        printf("Case #%d: ", t);
        if (hwm > 1) {
            printf("Bad magician!\n");
        } else if (hwm == 1) {
            printf("%d\n", ans);
        } else {
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
