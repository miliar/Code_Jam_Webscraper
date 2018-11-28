#include <cstdio>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for (int n = 1; n<=t; n++) {
        // Variable declarations
        char board[4][5];
        int rowsum[4] = {0, 0, 0, 0};
        int colsum[4] = {0, 0, 0, 0};
        int diagnolsum[2] = {0, 0};
        int isfull = 1;
        int k;
        // Finding out various sums
        for (int i=0; i<4; i++) {
            scanf("%s", board[i]);
            for (int j=0; j<4; j++) {
                rowsum[i] += (int)board[i][j];
                colsum[j] += (int)board[i][j];
                if (board[i][j] == '.') isfull = 0;
            }
            // printf("rowsum[%d]: %d ", i, rowsum[i]);
            diagnolsum[0] += (int)board[i][i];
            diagnolsum[1] += (int)board[i][3-i];
        }
        // printf("\n");
        // Displaying sums
        // for (int i=0; i<4; i++)
        //     printf("rowsum[%d]: %d ", i, rowsum[i]);
        // printf("\n");
        // for (int i=0; i<4; i++)
        //     printf("colsum[%d]: %d ", i, colsum[i]);
        // printf("\n");
        // printf("diagnolsum[0]:%d diagnolsum[1]:%d\n", diagnolsum[0], diagnolsum[1]);
        // Checking diagnols
        if (diagnolsum[0] == 352 || diagnolsum[0] == 348 || diagnolsum[1] == 352 || diagnolsum[1] == 348) {
            printf("Case #%d: X won\n", n);
            continue;
        } else if (diagnolsum[0] == 321 || diagnolsum[0] == 316 || diagnolsum[1] == 321 || diagnolsum[1] == 316) {
            printf("Case #%d: O won\n", n);
            continue;
        }
        // Checking rows & colums
        for (k=0; k<4; k++) {
            if (rowsum[k] == 352 || rowsum[k] == 348 || colsum[k] == 352 || colsum[k] == 348) {
                printf("Case #%d: X won\n", n);
                break;
            }
            if (rowsum[k] == 321 || rowsum[k] == 316 || colsum[k] == 321 || colsum[k] == 316) {
                printf("Case #%d: O won\n", n);
                break;
            }
        }
        // Check if end
        if (k != 4) continue;
        // Check Draw or Game completed
        if (isfull == 1)
            printf("Case #%d: Draw\n", n);
        else
            printf("Case #%d: Game has not completed\n", n);
    }
    return 0;
}