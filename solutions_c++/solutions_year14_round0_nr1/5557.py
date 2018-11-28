#include <cstdio>
#include <iostream>
using namespace std;
int main() {
    freopen("gcj1a.in","r",stdin);
    freopen("magic_trick.out","w",stdout);

    int tc, row1, row2, ar1[4][4], ar2[4][4], k = 1;
    scanf("%d",&tc);
    while (tc--) {
        scanf("%d",&row1);
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++)
                scanf("%d",&ar1[i][j]);
        }
        scanf("%d",&row2);
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++)
                scanf("%d",&ar2[i][j]);
        }
        int match = 0, temp, ans = -1;
        for (int i=0; i<4; i++) {
            temp = ar1[row1-1][i];
            for (int j=0; j<4; j++) {
                if (temp == ar2[row2-1][j]) {
                    match++;
                    ans = temp;
                }
            }
        }
        if (match == 1) {
            printf("Case #%d: %d\n",k,ans);
        } else if (match > 1) {
            printf("Case #%d: Bad magician!\n",k);
        } else if (match == 0) {
            printf("Case #%d: Volunteer cheated!\n",k);
        }
        k++;
    }
    return 0;
}
