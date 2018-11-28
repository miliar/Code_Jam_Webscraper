#include <stdio.h>

typedef unsigned int uint;

int main() {

    int T;

    int row1, row2;

    int cards[5][5];
    int cards2[5][5];

    scanf("%d", &T);

    for (uint t = 1; t <= T; ++t) {
        scanf("%d", &row1);

        for (uint row = 1; row <= 4; ++row)
            for (uint col = 1; col <= 4; ++col)
                scanf("%d", &cards[row][col]);

        scanf("%d", &row2);

        for (uint row = 1; row <= 4; ++row)
            for (uint col = 1; col <= 4; ++col)
                scanf("%d", &cards2[row][col]);

        int numRet = 0;
        int ret;

        for (uint col1 = 1; col1 <= 4; ++col1)
            for (uint col2 = 1; col2 <= 4; ++col2)
                if (cards[row1][col1] == cards2[row2][col2]) {
                    ++numRet;
                    ret = cards[row1][col1];
                }

        if (numRet == 0)
            printf("Case #%d: Volunteer cheated!\n", t);
        else if (numRet == 1)
            printf("Case #%d: %d\n", t, ret);
        else
            printf("Case #%d: Bad magician!\n", t);
    }
    return 0;
}
