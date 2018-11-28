#include <cstdio>
#include <math.h>

int main ()
{
	freopen("b.in", "r",stdin);
	freopen("b.out", "w", stdout);

	int test_case = 0;
	int case_no = 1;

	scanf("%d", &test_case);
	while(test_case--)
	{
		double c = 0;
		double x = 0;
		double f = 0;

		scanf("%lf%lf%lf", &c, &f,&x);

		double incr = 2;
		double next_sec = x/incr;
		double sec = next_sec + 1;
		double farm_cost = c/incr;

		for(int i = 1; next_sec < sec; ++i)
		{
			incr = incr + f;
			sec = next_sec;
			next_sec = farm_cost + x/incr;
			farm_cost = farm_cost + c/incr;
		}

		printf("Case #%d: %.7lf\n", case_no++, sec);
	}

	return 0;
}