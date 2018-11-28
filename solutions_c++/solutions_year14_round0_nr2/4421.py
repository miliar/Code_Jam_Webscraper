#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
const double eps=1e-8;
double c,x,f;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ca=1;ca<=t;ca++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		if(x-c<=eps)
			printf("Case #%d: %.7lf\n",ca,x/2.0);
		else
		{
			double a=2.0;
			double ans=0,t0=c/a,t1=x/a,t2=x/(a+f)+t0;
			while(t1>t2)
			{
				ans+=t0;
				a+=f;
				t0=c/a;
				t1=x/a;
				t2=x/(a+f)+t0;
			}
			ans+=t1;
			printf("Case #%d: %.7lf\n",ca,ans);
		}
	}
	return 0;
}
