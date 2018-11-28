#include <cstdio>

int main()
{
    int cases;
    scanf("%d\n", &cases);
    for (int i = 0; i < cases; i++) {
        int r1;
        int r2;
        int b1[4][4];
        int b2[4][4];
        scanf("%d", &r1);
        r1--;
        for (int j = 0; j < 4; j++) {
            scanf("%d %d %d %d", &b1[j][0], &b1[j][1], &b1[j][2], &b1[j][3]);
        }
        scanf("%d", &r2);
        r2--;
        for (int j = 0; j < 4; j++) {
            scanf("%d %d %d %d", &b2[j][0], &b2[j][1], &b2[j][2], &b2[j][3]);
        }
        int count = 0;
        int num = -1;
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                if (b1[r1][j] == b2[r2][k]) {
                    num = b1[r1][j];
                    count++;
                }
            }
        }
        if (count == 0)
            printf("Case #%d: Volunteer cheated!\n", i+1);
        else if (count == 1)
            printf("Case #%d: %d\n", i+1, num);
        else
            printf("Case #%d: Bad magician!\n", i+1);
    }
}
