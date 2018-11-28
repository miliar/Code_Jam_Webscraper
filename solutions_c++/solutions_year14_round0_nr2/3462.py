#include<cstdio>
#include<algorithm>
#include<climits>
using namespace std;
double i,j,k,l,m,n,a,b,mini=0,c,f,x,tim,g;
int cnt,t;
int main()
{
    freopen("m.in","r",stdin);
    freopen("k.out","w",stdout);
scanf("%d",&t);
while(t--)
{
scanf("%lf %lf %lf",&c,&f,&x);
cnt++;
l=f;

mini=x/2;

    k=c/2;
    //printf("k==%lf\n",k);
    f=f+2;
    tim=k;
   // printf("mini=%lf time==%lf f==%lf\n",mini,tim,f);
    while(1)
    {

        g=tim+x/f;
        if(mini<g)
        break;
        mini=min(mini,g);
        tim=tim+c/f;
        f=f+l;



       // printf("mini=%lf time==%lf f==%lf\n",mini,tim,f);
    }

printf("Case #%d: %.7lf\n",cnt,mini);
}
return 0;
}
