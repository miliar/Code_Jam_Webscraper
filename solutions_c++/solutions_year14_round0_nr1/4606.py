#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
using namespace std;

int T, rowa, rowb, a[5][5], b[5][5];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for (int tst = 1; tst <= T; tst ++){
        scanf("%d",&rowa);
        for (int i = 1; i <= 4; i ++)
          for (int j = 1; j <= 4; j ++) scanf("%d",&a[i][j]);
        scanf("%d",&rowb);
        for (int i = 1; i <= 4; i ++)
          for (int j = 1; j <= 4; j ++)
            scanf("%d",&b[i][j]);
        int cho = 0;
        for (int j = 1; j <= 4; j ++)
            for (int k = 1; k <= 4; k ++)
               if (a[rowa][j] == b[rowb][k]){
                   if (cho == 0) cho = a[rowa][j];
                   else if (cho > 0) cho = - 1;
               } 
        printf("Case #%d: ",tst);
        if (cho == -1) printf("Bad magician!\n");
        if (cho == 0) printf("Volunteer cheated!\n");
        if (cho > 0) printf("%d\n",cho);
    }
    return 0;
} 
