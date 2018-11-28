#include<cstdio>
#include<iostream>
#include<vector>
#include<set>
#include<algorithm>

using namespace std;

int main(void)
{
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);

    int tests;

    scanf("%d", &tests);

    for (int test=1;test<=tests;++test) {
        int grid1[4][4], grid2[4][4], answer1, answer2, mask[20] = {0};

        set<int> row;
        scanf("%d", &answer1);
        for(int i=0;i<4;++i) {
            for(int j=0;j<4;++j) {
                scanf("%d", &grid1[i][j]);
                if (i + 1 == answer1) {
                    mask[grid1[i][j]] = 1;
                }
            }
        }

        scanf("%d", &answer2);
        int count = 0, guess;
        for(int i=0;i<4;++i) {
            for(int j=0;j<4;++j) {
                scanf("%d", &grid2[i][j]);
                if (i + 1 == answer2) {
                    count += mask[grid2[i][j]];
                    if (mask[grid2[i][j]]) {
                        guess = grid2[i][j];
                    }
                }
            }
        }

        if (count == 1) {
            printf("Case #%d: %d\n", test, guess);
        } else if (count == 0 ) {
            printf("Case #%d: Volunteer cheated!\n", test);
        } else {
            printf("Case #%d: Bad magician!\n", test);
        }

    }
    return 0;
}
