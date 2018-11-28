#include<stdio.h>
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    //freopen("A-small-attempt2.out","w",stdout);

    long long flag,n,m,ar[4][4],br[4][4],t,i,res,j,k;
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {
          flag=0;
        scanf("%lld",&n);
        for(j=0;j<4;j++)
        for(k=0;k<4;k++)
            scanf("%lld",&ar[j][k]);

        scanf("%lld",&m);

        for(j=0;j<4;j++)
        for(k=0;k<4;k++)
            scanf("%lld",&br[j][k]);


        res=0;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(ar[n-1][j]==br[m-1][k])
                {
                    res=ar[n-1][j];
                    if(flag==1)
                        flag=2;
                    else if(flag==0)
                        flag=1;
                }
            }
        }
        if(flag==0)
            printf("Case #%lld: Volunteer cheated!\n",i);
        if(flag==1)
            printf("Case #%lld: %lld\n",i,res);
        if(flag==2)
            printf("Case #%lld: Bad magician!\n",i);
    }

    return 0;
}


