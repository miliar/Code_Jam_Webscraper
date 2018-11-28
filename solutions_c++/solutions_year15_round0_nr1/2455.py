#include<stdio.h>
int main()
{
    //freopen("A.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,i,j,standing=0, invite = 0, totalinvite = 0, n, t_standing = 0;
    char str[1002];

    scanf("%d",&T);
    for(i=1; i<=T; i++)
    {
        scanf("%d %s",&n,str);
        standing=0;
        invite=0;
        totalinvite=0;
        t_standing = 0;
        if(n<=0){
            printf("Case #%d: %d\n",i,totalinvite);
        }
        else{
            for(j=0; j<=n; j++){
                if(standing < j){
                        invite = j-standing;
                        totalinvite = totalinvite + invite;
                    }
                    t_standing = ((int)str[j] - 48 )+ standing+ invite;
                    standing = t_standing;
                    invite=0;
                }
            printf("Case #%d: %d\n",i,totalinvite);
       }
    }
     return 0;
}
