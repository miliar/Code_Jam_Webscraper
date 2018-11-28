#include<stdio.h>

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("outBsmallbad.txt","w",stdout);
    int a,b,k,t,s,m;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        s=0;
        scanf("%d %d %d",&a,&b,&k);
        for(int j=0;j<a;j++)
        {
            for(int z=0;z<b;z++)
            {
                if((j&z)<k) s++;
            }
        }
        printf("Case #%d: %d\n",i,s);
    }
    return 0;
}
