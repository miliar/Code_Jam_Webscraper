#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	long long t,cas=1;
	scanf("%lld",&t);
	while(t--)
	{
		double c,f,x,rate=2, tim=0,dum;
		scanf("%lf%lf%lf",&c,&f,&x);
		dum = x/2;
		while(1)
		{
			tim += c/rate;
			rate +=f;
			if(dum>(tim+x/ rate))
				dum = (tim+x/rate);
			else
				break;
		}
		printf("Case #%lld: %.7lf\n",cas,dum );
		cas++;
	}
	return 0;
}
