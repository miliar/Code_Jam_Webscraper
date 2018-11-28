#include <stdio.h>
#pragma warning(disable: 4996)

const double EPS = 1e-6;

double abs(double x)
{
	if (x>EPS)
		return x;
	else
		if (-EPS<x && x<EPS)
			return 0;
		else
			if (x<-EPS)
				return -x;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Tests;
	scanf("%d", &Tests);
	for (int n = 0; n<Tests; n++)
	{
		double C, F, X, current = 0.0f, time = 0.0f, persec = 2.0f;
		scanf("%lf%lf%lf", &C, &F, &X);
		while (true)
		{
			if (X/persec<C/persec+X/(persec+F))
			{
				time += X/persec;
				break;
			}
			else
			{
				time += C/persec;
				persec += F;
				current = 0.0f;
			}
		}
		printf("Case #%d: %.7lf\n", n+1, time);
	}
	return 0;
}