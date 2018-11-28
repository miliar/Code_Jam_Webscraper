#include<iostream>
using namespace std;
int main()
{
	long long int t;
	scanf("%lld",&t);
	long long int cases=1;
	while(t--)
	{
		double c,f,x,time=0;
		double rate=2,ans=0;
		scanf("%lf %lf %lf",&c,&f,&x);
		while(ans!=x)
		{
			if((c/rate)+x/(rate+f)>=(x/rate))
			{
				time+=(x/rate);
				ans=x;
			}
			else
			{
				time+=(c/rate);
				rate+=f;
				ans=0;
			}
		}
		printf("Case #%lld: %0.7lf\n",cases,time);
		cases++;
	}
}
