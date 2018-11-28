#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
int t,i,j,n,val[5][5],ans,check[20];
bool cheat,badMagick,ok;
int main()
{
    freopen("f.in","r",stdin);
    freopen("f.out","w",stdout);

    int Case=1;

    scanf("%d",&t);
    while(t--){
        memset(check,0,sizeof(check));
        ok = badMagick = cheat = 0;
        //
        scanf("%d",&ans);
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                scanf("%d",&val[i][j]);
            }
        }
        //
        for(j=1;j<=4;j++){
            check[val[ans][j]]++;
        }
        //
        scanf("%d",&ans);
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                scanf("%d",&val[i][j]);
            }
        }
        //
        for(j=1;j<=4;j++){
            check[val[ans][j]]++;
        }
        //
        for(i=1;i<=16;i++){
            if(check[i]==2){
                if(ok) badMagick = 1;
                else{
                    ok = 1;
                    ans = i;
                }
            }
        }

        if(badMagick) printf("Case #%d: Bad magician!\n",Case++);
        else if(ok) printf("Case #%d: %d\n",Case++,ans);
        else printf("Case #%d: Volunteer cheated!\n",Case++);

    }

    return 0;
}
