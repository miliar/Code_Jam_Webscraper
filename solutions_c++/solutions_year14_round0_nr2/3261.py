#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
double c,f,x;
double fun(double co)
{
    double p,pp,ppp,t;
    p=x/co;
    pp=c/co;
    ppp=x/(co+f);
    t=pp;
    if(p<(pp+ppp))
        return p;
    while(p>(pp+ppp))
    {
        //cout<<p<<" "<<pp<<" "<<ppp<<" "<<t<<endl;
        p=ppp;
        co=co+f;
        pp=c/co;
        ppp=x/(co+f);
        t=t+double(pp);
    }
    return (double)(t+p-pp);
}
int main()
{
    int t;
	scanf("%d",&t);
	int cas=0;
	double co,ans;
	while(t>0)
	{
		t-=1;cas+=1;
		cin>>c>>f>>x;
		if(x<=c)
        {
            printf("Case #%d: %.7llf\n",cas,(x/2));
            continue;
        }
        co=2;
        ans=fun(co);
        //cout<<ans<<endl;
        printf("Case #%d: %.7llf\n",cas,ans);
	}
    return 0;
}
