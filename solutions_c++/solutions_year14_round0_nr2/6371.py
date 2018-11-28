#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
	int t,test;
	double c,f,x,ans,max,r,nr,pur;
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=0.0;
		r=2.0;
		while(true)
		{
			max=x/r;
			nr=r+f;
			pur=c/r+x/nr;
			if(pur<=max)
			{
				ans+=c/r;
				r+=f;
			}
			else
			{
				ans+=max;
				break;
			}
		}
		printf("Case #%d: ",t);
		printf("%.7lf\n",ans);
	}
	return 0;
}
