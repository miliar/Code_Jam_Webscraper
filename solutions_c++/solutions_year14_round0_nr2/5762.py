#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
long long ans;
double c,f,x;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas<=t;cas++)
    {
        double ans=1e18;
        scanf("%lf%lf%lf",&c,&f,&x);
        for(int i=0;i<2200;i++)
        {
           double a=2.0;
           double ret=0.0;
           int tmp=i;
           while(tmp--)
           {
               ret+=c/a;
               a+=f;
           }
           double res=ret+x/a;
           if(res<ans)
           {
               ans=res;
           }
        }
        printf("Case #%d: %.7f\n",cas,ans);
    }
    return 0;
}
