#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int vis[20];
#define eps 1e-7
bool cmp(double a,double b)
{
    if(a-b<=eps) return true;
}
int main()
{
    int cas;
    int ca=1;
  //  freopen("B-large.in","r",stdin);
  //  freopen("out.out","w",stdout);
  scanf("%d",&cas);
    while(cas--)
    {
        double c,f,x;
        double nowget=2.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans=0;
        while(1)
        {
            double notbuy=x/nowget;
            double buy=c/nowget+x/(nowget+f);
            if(notbuy<=buy)
            {
                ans+=notbuy;
                break;
            }
            ans+=c/nowget;
            nowget+=f;

        }
        printf("Case #%d: %.7lf\n",ca++,ans);
    }
    return 0;
}
