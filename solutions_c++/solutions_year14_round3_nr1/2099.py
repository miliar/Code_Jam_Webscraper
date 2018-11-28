#include <cstdio>
#include<bitset>
using namespace std;
long long a,b,sol,cm,n,i,aux;;
char c;
int cmmdc(int x,int y)
{
    while(y)
    {
        aux=x%y;
        x=y;
        y=aux;
    }
    return x;
}
bool put(int b)
{
    int a=1;
    while(a<b)
        a<<=1;
    if(a==b)
        return 0;
    return 1;
}
int main()
{
    freopen("gjamC.in","r",stdin);
    freopen("gjamC.out","w",stdout);
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        printf("Case #%d: ",i);
        scanf("%lld%c%lld",&a,&c,&b);
        if(a%b==0)
        {
            cm=cmmdc(a,b);
            a/=cm;
            b/=cm;
        }
        sol=0;
        if(a==0||put(b))
        {
            printf("impossible\n");continue;
        }
        while(a<b/2)
        {
            sol++;
            b>>=1;
        }
        printf("%d\n",sol+1);
    }

    return 0;
}
