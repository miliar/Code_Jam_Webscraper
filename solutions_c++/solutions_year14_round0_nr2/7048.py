//#pragma warning( disable : 4996 )
#include<stdio.h>

int k, test;
double A, B, res;
double x, f, cost, rate;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &test);
	for (k = 1; k <= test; k++)
	{
		res = 0;
		scanf("%lf %lf %lf\n", &cost, &f, &x);
		
		if (cost >= x)
		{
			x = x / 2.0;
			printf("Case #%d: %.7lf\n", k, x);
		}
		else
		{
			for (rate = 2.0;; rate = rate + f)
			{
				A = x / rate;
				B = cost / rate + x / (rate + f);
				
				if (A < B)
				{
					res = res + x / rate;
					break;
				}
				res = res + cost / rate;
			}
			printf("Case #%d: %.7lf\n", k, res);
		}
	}

	return 0;
}