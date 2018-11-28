#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	long double c,f,x,t2,t1,cookies,t3,cps,ans;
	for(int i=1;i<=t;i++)
	{
		cookies=0.0;
		ans=0.0;
		cps=2.0;
		t2=0.0;
		t1=0.0;
		t3=0.0;
		cin>>c>>f>>x;
		//printf("%.7Lf %.7Lf %.7Lf\n",c,f,x);
		while(1)
		{
			if(((c-cookies)/cps)+((x-cookies)/(cps+f))>(x-cookies)/cps)
			{
				ans+=x/cps;
				break;
			}
			else
			{
				ans+=(c-cookies)/cps;
				cps+=f;
			}
			//printf("Case #%d: %LF\n",i,ans);
			
		}
		printf("Case #%d: %.7LF\n",i,ans);
	}
return 0;
}
