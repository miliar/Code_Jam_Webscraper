#include <stdio.h>
int f[17];
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int n,i,j,x,k,l;
    scanf("%d",&l);
    for(k=1;k<=l;k++)
    {
    scanf("%d",&n);
    for(i=1;i<=4;i++)
    {
        if(i==n)
            for(j=1;j<=4;j++)
            {
                scanf("%d",&x);
                ++f[x];
            }
        else
        for(j=1;j<=4;j++)
            scanf("%d",&x);
    }
    scanf("%d",&n);
    for(i=1;i<=4;i++)
    {
        if(i==n)
            for(j=1;j<=4;j++)
            {
                scanf("%d",&x);
                ++f[x];
            }
        else
        for(j=1;j<=4;j++)
            scanf("%d",&x);
    }
    int sol=-1;
    bool fl=1;
    for(i=1;i<=17;i++)
    {
        if(f[i]==2 && sol==-1)
            sol=i;
        else
        if(f[i]==2 && sol!=-1)
        {
            printf("Case #%d: Bad magician!\n",k);
            fl=0;
            break;
        }
    }
    if(sol==-1)
        printf("Case #%d: Volunteer cheated!\n",k);
    else if(fl==1)
        printf("Case #%d: %d\n",k,sol);
    for(i=1;i<=16;i++)
        f[i]=0;
    }
    return 0;
}
