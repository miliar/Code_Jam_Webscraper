#include <cstdio>
using namespace std;

const int ROW_NUM = 4;
int card[2][ROW_NUM][ROW_NUM];

int main() {
    freopen("A.txt", "r", stdin);
    
    int T;
    scanf("%d", &T);
    int ca;
    for (ca = 1; ca <= T; ++ca) {
        printf("Case #%d: ", ca);
        int row[2];
        scanf("%d", row);
        --row[0];
        int i, j;
        for (i = 0; i < ROW_NUM; ++i) {
            for (j = 0; j < ROW_NUM; ++j) {
                scanf("%d", &card[0][i][j]);
            }
        }
        scanf("%d", row + 1);
        --row[1];
        for (i = 0; i < ROW_NUM; ++i) {
            for (j = 0; j < ROW_NUM; ++j) {
                scanf("%d", &card[1][i][j]);
            }           
        }
        
        int cnt = 0;
        int res = 0;
        // check
        for (i = 0; i < ROW_NUM; ++i) {
            for (j = 0; j < ROW_NUM; ++j) {
                if (card[0][row[0]][i] == card[1][row[1]][j]) {
                    ++cnt;
                    res = card[0][row[0]][i];
                }
            }
        }
        
        if (cnt == 1) {
            printf("%d\n", res);
        } else if (cnt > 1) {
            printf("Bad magician!\n");
        } else {
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}