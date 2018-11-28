#include <stdio.h>
#include <stdlib.h>




int main(void)
{
    int Tcase, row1, row2;
    int m1[4][4], m2[4][4];
    int ans;

    scanf("%d", &Tcase);

    for (int i=1; i<=Tcase; i++) {
        scanf("%d", &row1);
        for (int j=0; j<4; j++) {
            scanf("%d %d %d %d", &m1[j][0], &m1[j][1], &m1[j][2], &m1[j][3]);
        }
        scanf("%d", &row2);
        for (int j=0; j<4; j++) {
            scanf("%d %d %d %d", &m2[j][0], &m2[j][1], &m2[j][2], &m2[j][3]);
        }

        ans = -1;
        row1 -= 1;
        row2 -= 1;
        int last, cur;

        for (int r1=0; r1<4; r1++) {
            last = m1[row1][r1];
            for (int r2=0; r2<4; r2++) {
                cur = m2[row2][r2];
                if ( last == cur ) {
                    if ( ans > 0 ) {
                        ans = -2;
                        goto end;
                    }
                    ans = cur;
                }
            }
        }
end:
        switch (ans) {
            case -1:
                printf("Case #%d: Volunteer cheated!\n", i);
                break;
            case -2:
                printf("Case #%d: Bad magician!\n", i);
                break;
            default:
                printf("Case #%d: %d\n", i, ans);
        }
    }


    return 0;
}
