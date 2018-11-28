#include <cstdio>

using namespace std;
int t;
double a,b,c,suma,nr;
int main()
{
    freopen("cookie.in","r",stdin);
    freopen("cookie.out","w",stdout);
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        scanf("%lf%lf%lf",&a,&b,&c);
        suma=a/2;
        nr=2;
        while(suma+c/(b+nr)<suma+(c-a)/nr)
        {
            nr=b+nr;
            suma=suma+a/nr;
        }
        suma=suma+(c-a)/nr;
        printf("Case #%d: %.7lf\n",k,suma);
    }
    return 0;
}
