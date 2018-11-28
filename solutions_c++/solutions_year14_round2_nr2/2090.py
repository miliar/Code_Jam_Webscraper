#include <cstdio>
#include<iostream>

using namespace std;


int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    long long t,k,a,b,c,i,j,x,l;

    scanf("%lld",&t);

    for(k=1;k<=t;k++)
    {
        l=0;
        scanf("%lld %lld %lld",&a,&b,&c);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                x=i&j;
                if(x<c)
                    l++;
            }
        }
        printf("Case #%lld: %lld\n",k,l);
    }

    return 0;
}
