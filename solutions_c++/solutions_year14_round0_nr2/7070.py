#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define eps 1e-9
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	double c,f,x,tm,rate,extra,buy_after;
	int icase;
	scanf("%d",&icase);
	for(int k=1;k<=icase;k++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		tm=0;		
		rate=2;
		while(1)
		{
			tm+=(c/rate);			
		    extra=(x-c)/rate;
			buy_after=x/(rate+f);
			if(extra<buy_after||fabs(extra-buy_after)<eps)
			{
				tm+=extra;break;
			}
			else
			{
				rate+=f;
			}
		}
		printf("Case #%d: %.7lf\n",k,tm);


	}
	return 0;
}