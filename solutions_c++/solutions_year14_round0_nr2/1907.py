#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{
    int t;
    double c,f,x;
    freopen("B-large.in","r",stdin);
      freopen("out.txt","w",stdout);

    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);

        double ans=x/2.0;
        double cost=c/2.0;
        double range=2.0+f;
        while(cost+x/(range)<ans)
        {
            ans=cost+x/range;
            cost+=(c/range);
            range+=f;
        }
        printf("Case #%d: %.7lf\n",cs,ans);
    }
return 0;
}
