#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        int ans[2] = {0};
        int board[2][4][4] = {0};
        for (int j = 0; j < 2; ++j) {
            cin >> ans[j];
            for (int m = 0; m < 4; ++m) {
                for(int n = 0; n < 4; ++n) {
                    cin >> board[j][m][n];
                }
            }
        }
        int *row1 = board[0][ans[0]-1];
        int *row2 = board[1][ans[1]-1];
        sort(row1, row1+4);
        sort(row2, row2+4);
        vector<int> result;
        set_intersection(row1, row1+4, row2, row2+4, back_inserter(result));
        if (result.empty()) {
            printf("Volunteer cheated!\n");
        } else if (result.size() > 1) {
            printf("Bad magician!\n");
        } else {
            printf("%d\n", result[0]);
        }
    }
    return 0;
}
