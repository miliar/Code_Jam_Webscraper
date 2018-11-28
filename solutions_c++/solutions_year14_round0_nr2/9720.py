#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,ii,i,j;
    double C,F,X,cookies,rate,time,ans;
    scanf("%d",&t);
    for(ii=1;ii<=t;ii++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
        ans=X;
        for(i=0;i<=X;i++)
        {
            cookies=0;
            rate=2;
            time=0;
            for(j=0;j<i;j++)
            {
                time+=C/rate;
                rate+=F;
            }
            time+=X/rate;
            ans=min(ans,time);
        }
        printf("Case #%d: %.7lf\n",ii,ans);
    }
}
