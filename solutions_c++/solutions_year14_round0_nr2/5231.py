#include <stdio.h>
#include <stdlib.h>
double rate;
double cookie(double x, double c, double f, double farms)
{
	double time = 0;
	while(1)
	{
	double normal = x / (rate + farms * f);
	double abnormal = (x / (rate + (farms+1) * (f))) + c / (rate + farms * f);
	if (normal <= abnormal)
		return normal + time;
	else
	{
		time += (c / (rate + farms * f));
		farms++;
	}
	}
}

int main()
{
	int test;
	double c, f, x;
	double time;
	int i;
	scanf("%d", &test);
	for (i = 1; i <= test; i++)
	{
		rate = 2;
		scanf("%lf %lf %lf", &c, &f, &x);
		time = cookie(x, c, f, 0);
		printf("Case #%d: %.7lf\n", i, time);

	}
}
