#include<cstdio>
#include<cmath>

using namespace std;

bool palcheck(long long a)
{
    long long x[14],y[14],i,c=0,flag=1,z=a;
    for(i=0;i<14;i++)
    {
        x[i]=0;
        y[i]=0;
    }
    while(z!=0)
    {
        z=z/10;
        c++;
    }
    i=0;
    while(a!=0)
    {
        x[i]=a%10;
        y[c-1-i]=a%10;
        i++;
        a=a/10;
    }
    for(i=0;i<14;i++)
    {
        if(x[i]!=y[i])
        {
            flag=0;
            break;
        }
    }
    return flag;
}

main()
{
    freopen("C. Fair and Square.in","r",stdin);
    freopen("C. Fair and Square.out","w",stdout);
    long long t,a,b,i,j,x,y,c;
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {
        c=0;
        scanf("%lld%lld",&a,&b);
        x=(int)ceil(sqrt(a));
        y=(int)floor(sqrt(b));
        for(j=x;j<=y;j++)
        {
            if(palcheck(j))
            {
                if(palcheck(j*j))
                {
                    c++;
                }
            }
        }
        printf("Case #%lld: %lld",i,c);
        if(i!=t)
        {
            printf("\n");
        }
    }
    return 0;
}
