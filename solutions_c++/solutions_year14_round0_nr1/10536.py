#include<stdio.h>
#include <algorithm>
#include <iostream>
#include <set>
#include <string.h>
using namespace std;
int a[5][5],b[5][5],flag[17];
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int n,m,i,j,ans,t,k;
    while(scanf("%d",&t)!=EOF){
        for(k=1;k<=t;k++){
            memset(flag,0,sizeof(flag));
            scanf("%d",&n);
            for(i=1;i<=4;i++){
                for(j=1;j<=4;j++){
                    scanf("%d",&a[i][j]);
                }
            }
            for(i=1;i<=4;i++){
                flag[a[n][i]]=1;
            }
            scanf("%d",&m);
            for(i=1;i<=4;i++){
                for(j=1;j<=4;j++){
                    scanf("%d",&b[i][j]);
                }
            }
            int c=0;
            for(i=1;i<=4;i++){
                if(flag[b[m][i]]){
                    c++;
                    ans=b[m][i];
                }
            }
            printf("Case #%d: ",k);
            if(c==0){
                printf("Volunteer cheated!\n");
            }else if(c>1){
                printf("Bad magician!\n");
            }else{
                printf("%d\n",ans);
            }

        }
    }
    return 0;
}
