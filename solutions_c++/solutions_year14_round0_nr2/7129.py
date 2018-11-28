#include<bits/stdc++.h>
using namespace std;

double c,f,x,ans,nowspeed;
int t,tcase=0;

int main()
{
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=0;
		nowspeed=2.0;
		while(1)
		{
			double tmp1=x/nowspeed;
			double tmp2=c/nowspeed+x/(nowspeed+f);
			if(tmp1<=tmp2)
			{
				ans+=tmp1;
				break;
			}
			else
			{
				ans+=c/nowspeed;
				nowspeed+=f;
			}
		}
		printf("Case #%d: %.7lf\n",++tcase,ans);
	}
	return 0;
}
