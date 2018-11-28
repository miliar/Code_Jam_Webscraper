#include <stdio.h>
using namespace std;
long long n,r,t,i,j,contor=1,k1,k2,x=1,suma;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%lld",&n);
    for(i=1;i<=n;++i)
    {
        suma=0;
        contor=0;
        scanf("%lld %lld",&r,&t);
        for(j=r;;j+=2)
        {
            suma+=(j+1)*(j+1)-j*j;
            contor++;
            if(suma>t)
            {
                contor--;
                break;
            }
            if(suma==t)break;
        }
        printf("Case #%lld: %lld\n",x++,contor);
    }
    return 0;
}
