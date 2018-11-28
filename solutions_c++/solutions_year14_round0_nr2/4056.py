#include<cstdio>
using namespace std;
int main()
{
   freopen("B-large.in","r",stdin);
    freopen("output-large.out","w",stdout);
    int t,i;
    scanf("%d",&t);
    double c,f,x,temp=0.0,r=2.0;
    for(i=1;i<=t;i++)
    {
        temp=0.0;
        r=2.0;
        scanf("%lf %lf %lf",&c,&f,&x);
        while((c/r+(x/(r+f)))<x/r)
        {
            temp+=c/r;
            r+=f;
        }
        temp+=x/r;
        printf("Case #%d: %.7lf\n",i,temp);
    }
    return 0;
}
