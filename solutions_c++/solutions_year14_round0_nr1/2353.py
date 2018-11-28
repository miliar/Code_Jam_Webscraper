#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int ans[2];
    int c[2][4][4];
    for (int rt = 1; rt <= T; ++ rt) {
        for (int i = 0; i < 2; ++ i) {
            scanf("%d", &ans[i]);
            ans[i] --;
            for (int j = 0; j < 4; ++ j) {
                for (int k = 0; k < 4; ++ k) {
                    scanf("%d", &c[i][j][k]);
                }
            }
        }

        int ccnt = 0;
        int ansc = 0;
        for (int i = 0; i < 4; ++ i)
            for (int j = 0; j < 4; ++ j) {
                if (c[0][ans[0]][i] == c[1][ans[1]][j]) {
                    ccnt ++;
                    ansc = c[0][ans[0]][i];
                }
            }
        printf("Case #%d: ", rt);
        if (ccnt == 0) {
            printf("Volunteer cheated!\n");
        } else if (ccnt > 1) {
            printf("Bad magician!\n");
        } else {
            printf("%d\n", ansc);
        }
    }
    return 0;
}
