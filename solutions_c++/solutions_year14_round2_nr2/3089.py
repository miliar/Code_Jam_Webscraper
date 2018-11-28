#include<stdio.h>
int main()
{

    int a,b,k,t,ans,l,m,n,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {ans=0;
        scanf("%d%d%d",&a,&b,&k);
        for(l=0;l<a;l++)
        {
            for(m=0;m<b;m++)
            {
                n=l&m;
                if(n<k)
                    ans++;
            }
        }
            printf("Case #%d: %d\n",i,ans);
    }
}
