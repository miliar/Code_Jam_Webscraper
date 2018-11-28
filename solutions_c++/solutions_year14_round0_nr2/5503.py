#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
//const double eps=1e-8;
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int tt,ii,i,j;
    scanf("%d",&tt);
    for(ii=1;ii<=tt;ii++)
    {
        double c,f,x,ans,t=0,rate=2.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        ans=x/(2.0);
        for(i=1;i<int(x);i++)
        {
            t+=c/rate;
            rate+=f;
            ans=min(ans,t+x/rate);
        }
        printf("Case #%d: %.7f\n",ii,ans);
    }
    //system("pause");
    return 0;
}
