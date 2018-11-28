#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
double c,f,x;
double cal(int cnt)
{
    double se=2.0,ans=0;
    for(int i=0;i<cnt;i++)
        ans+=c/(se+i*f);
    return ans+x/(cnt*f+se);
}
int main()
{
    int ncase,i,j,tt=0;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&ncase);
    while(ncase--)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        double ll=0,rr=200000;
        double ans=1e100;
        while(ll+1e-6<=rr)
        {
            double mid1=ll+(rr-ll)/3;
            double mid2=rr-(rr-ll)/3;
            double v1=cal((int)mid1);
            double v2=cal((int)mid2);
            ans=min(ans,min(v1,v2));
            if(v2>v1)
                rr=mid2;
            else
                ll=mid1;
        }
        printf("Case #%d: %.7lf\n",++tt,ans);
    }
}
