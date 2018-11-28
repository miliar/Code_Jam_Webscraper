#include<stdio.h>

int main() {
    int t, i, j, flag, cas, ans, a, b;
    int ar[6][6];
    int br[6][6];
    
    scanf("%d",&t);
    
    for (cas=1; cas<=t; cas++) {
        scanf("%d",&a);
        for (i=1; i<=4; i++) {
            for (j=1; j<=4; j++) {
                scanf("%d",&ar[i][j]);
            }
        }
        scanf("%d",&b);
        for (i=1; i<=4; i++) {
            for (j=1; j<=4; j++) {
                scanf("%d",&br[i][j]);
            }
        }
        
        flag = -1;
        for (i=1; i<=4; i++) {
            for (j=1; j<=4; j++) {
                if (ar[a][i] == br[b][j]) {
                   ans = ar[a][i];
                   flag++;
                   break;
                }
            }
        }
        
        if (flag == -1) {
           printf("Case #%d: Volunteer cheated!\n",cas);
        } else if (flag == 0) {
           printf("Case #%d: %d\n",cas,ans);
        } else {
           printf("Case #%d: Bad magician!\n",cas);
        }
    }
    return 0;
}
