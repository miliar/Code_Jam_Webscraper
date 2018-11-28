#include <cstdio>

double minTime(double &c,double &f,double &x,double rate);
int main()
{
	freopen("TestSets/cookie.in","r",stdin);
	freopen("TestSets/cookie.out","w",stdout);

	int t,cnt = 1;
	double c,f,x,rate = 2.0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		printf("Case #%d: %.7lf\n",cnt,minTime(c,f,x,rate));
		cnt++;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}

double minTime(double &c,double &f,double &x,double rate)
{
	double mintime = 0.0;
	int i = 0;

	double initFarmTime = c/rate;
	double initBuyTime = x/rate;
	double newBuyTime = x/(rate+f);
	while(initFarmTime+newBuyTime<initBuyTime)
	{
		mintime += initFarmTime;
		rate += f;
		initFarmTime = c/rate;
		initBuyTime = newBuyTime;
		newBuyTime = x/(rate+f);
	}
	return (mintime+initBuyTime);
}
