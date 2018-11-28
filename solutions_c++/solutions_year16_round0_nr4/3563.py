#include <stdio.h>
#include <string.h>
#define LL long long

int main()
{
    int i,m,n,t;
    freopen("d.in","r",stdin);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        LL k,c,s;
        printf("Case #%d: ",i);
        scanf("%lld %lld %lld",&k,&c,&s);
        if(k==s)
        {
            LL j;
            c--;
            if(c==0) 
            {
                for(j=1;j<=k;j++)
                    printf("%lld ",j);
                puts("");
            }
            else
            {
                LL p=1;
                while(c--)  p=p*k;
                for(j=1;j<=k;j++)
                    printf("%lld ",p*(j-1)+1);
                puts("");
            }
        }
    }
    fclose(stdin);
    return 0;
}
