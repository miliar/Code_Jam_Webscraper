#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    int T;
    cin >> T;
    int case_num = 1;
    while (case_num <= T) {
        int ans1, ans2;
        int grid1[4][4], grid2[4][4];
        scanf("%d", &ans1);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int temp;
                scanf("%d", &temp);
                grid1[i][j] = temp;
            }
        }
        scanf("%d", &ans2);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int temp;
                scanf("%d", &temp);
                grid2[i][j] = temp;
            }
        }

        int num_ans = 0;
        int match = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (grid1[ans1-1][i] == grid2[ans2-1][j]) {
                    num_ans ++;
                    match = grid1[ans1-1][i];
                }
            }
        }

        if (num_ans == 0) {
            printf("Case #%d: Volunteer cheated!\n", case_num);
        } else if (num_ans > 1) {
            printf("Case #%d: Bad magician!\n", case_num);
        } else {
            printf("Case #%d: %d\n", case_num, match);
        }

        case_num ++;
    }
    return 0;
}
