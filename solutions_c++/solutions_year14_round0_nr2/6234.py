#include <stdio.h>

double solve(double C, double F, double X)
{
	double ans, cookie_rate;

	ans = 0;
	cookie_rate = 2.0;
	while (true)
	{
		if( X <= C ) {ans += X / cookie_rate; return ans;}
		else
		{
			//사야되는지 안사야되느지 판단
			if( X / cookie_rate > (X / (cookie_rate + F)) + C / cookie_rate )
			{
				ans += C / cookie_rate;
				cookie_rate += F;
			}
			else 
			{
				ans += X / cookie_rate;
				return ans;
			}
		}
	}


	return 0;
}


int main()
{
	int i, j, T, TestCase;
	double c, f, x;

	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);

	for(TestCase = 1; TestCase <= T; TestCase++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		printf("Case #%d: %lf\n", TestCase, solve(c, f, x));
	}

	return 0;
}