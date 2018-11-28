#include <cstdio>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int nn;
    scanf("%d",&nn);
    for(int cs=1;cs<=nn;cs++)
    {
        int n;
        scanf("%d",&n);
        printf("Case #%d: ",cs);
        if(!n)
        {
            puts("INSOMNIA");
            continue;
        }
        bool a[10]={};
        for(int x=n;;x+=n)
        {
            int xx=x;
            for(;xx;xx/=10)a[xx%10]=true;
            for(;xx<10;xx++)if(!a[xx])break;
            if(xx==10)
            {
                printf("%d\n",x);
                break;
            }
        }
    }
    return 0;
}