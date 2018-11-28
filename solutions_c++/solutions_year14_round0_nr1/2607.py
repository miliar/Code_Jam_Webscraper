#include <stdio.h>
int s1[5][5];
int s2[5][5];
int main(){
    //freopen("fun.in","r",stdin);
    freopen("fun.out","w",stdout);
    int t;
    int a,b,ans,w;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d",&a);
        for(int j=1;j<=4;j++)
            for(int k=1;k<=4;k++)
                scanf("%d",&s1[j][k]);
        scanf("%d",&b);
        for(int j=1;j<=4;j++)
            for(int k=1;k<=4;k++)
                scanf("%d",&s2[j][k]);
        ans=0;
        for(int j=1;j<=4;j++)
            for(int k=1;k<=4;k++)
                if(s1[a][j]==s2[b][k]){
                    ans++;
                    w=k;
                }
        if(ans==0)
            printf("Case #%d: Volunteer cheated!\n",i);
        else if(ans==1)
            printf("Case #%d: %d\n",i,s2[b][w]);
        else
            printf("Case #%d: Bad magician!\n",i);
    }
    return 0;
}
