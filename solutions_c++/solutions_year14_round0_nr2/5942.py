#include <cstdio>

using namespace std;

void solve()
{
	double C, F, X;
	scanf("%lf %lf %lf ", &C, &F, &X);

	double totalTime = 0;
	double rate = 2.0;
	double progress = 0;

	double finishTime =  (X - progress) / rate;
	double farmTime = 0;

	while(1)
	{
		double newFarmTime = farmTime + C/rate;
		//printf("%lf %lf %lf\n",farmTime, rate, newFarmTime);
		//printf("x - %lf %lf %lf\n",X, newFarmTime + (X-C)/(rate + F), (X-C)/rate);
		if (farmTime == 0)
		{
			if (newFarmTime + X/(rate + F) > X/rate)
				break;

		} 
		else if (newFarmTime + X/(rate + F) > farmTime + X/rate)
				break;
		farmTime = newFarmTime;
		rate += F;
	}
	if (farmTime == 0)
		printf("%.9lf\n",finishTime);
	else
		printf("%.9lf\n",farmTime + X/rate);
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int T;
	scanf("%d", &T);

	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}