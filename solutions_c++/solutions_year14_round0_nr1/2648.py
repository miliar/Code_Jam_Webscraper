#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    int T;

    scanf("%d", &T);

    for (int t = 1;t <= T;t++) {

        int cards1[5][5];
        int cards2[17];

        for (int i = 0;i < 17;i++) {
            cards2[i] = 0;
        }

        int row;

        scanf("%d", &row);

        for (int i = 1;i <= 4;i++) {
            for (int j = 1;j <= 4;j++) {
                scanf("%d", &cards1[i][j]);
            }
        }

        for (int i = 1;i <= 4;i++)
            cards2[cards1[row][i]]++;

        scanf("%d", &row);

        for (int i = 1;i <= 4;i++) {
            for (int j = 1;j <= 4;j++) {
                scanf("%d", &cards1[i][j]);
            }
        }

        for (int i = 1;i <= 4;i++)
            cards2[cards1[row][i]]++;

        int count = 0;
        int last;

        for (int i = 1;i <= 16;i++) {
            if (cards2[i] == 2) {
                count++;
                last = i;
            }
        }

        if (count == 1) {
            printf("Case #%d: %d\n", t, last);
        } else if (count == 0) {
            printf("Case #%d: Volunteer cheated!\n", t);
        } else {
            printf("Case #%d: Bad magician!\n", t);
        }
    }

    return 0;
}
