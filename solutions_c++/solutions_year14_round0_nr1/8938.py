#include <stdio.h>

int valid[17];

int main()
{
    freopen("test.txt", "r", stdin);
    freopen("result.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int Case = 1; Case <= T; Case++) {
        for (int i = 1; i <= 16; i++) valid[i] = 0;
        int ans;
        scanf("%d", &ans);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                int t;
                scanf("%d", &t);
                if (ans == i)
                    valid[t]++;
            }
        }
        scanf("%d", &ans);
        for (int i = 1; i <= 4; i++) {
            for (int j = 1; j <= 4; j++) {
                int t;
                scanf("%d", &t);
                if (ans == i)
                    valid[t]++;
            }
        }
        int cnt = 0;
        for (int i = 1; i <= 16; i++) {
            if (valid[i] == 2)
                cnt++;
        }

        printf("Case #%d: ", Case);
        if (cnt == 0) {
            printf("Volunteer cheated!\n");
        }
        else if (cnt > 1) {
            printf("Bad magician!\n");
        }
        else {
            for (int i = 1; i <= 16; i++) {
                if (valid[i] == 2)
                    printf("%d\n", i);
            }
        }
    }
}
