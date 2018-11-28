#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
double ans;
double c,f,x,r,s;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    int ca=1;
    scanf("%d",&t);
    while(t--)
    {
        r=2.0;
        s=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        ans=x/2.0;
        while(s+c/r<ans)
        {
            s+=c/r;
            r+=f;
            ans=min(ans,s+x/r);
        }
        printf("Case #%d: %.7f\n",ca++,ans);
    }
    return 0;
}
