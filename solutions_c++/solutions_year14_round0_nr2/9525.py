#include <stdio.h>
#include <stdlib.h>
#include <float.h>

double cf(int max, double f)
{
	double tmp = 1 / (2 + max * f);
	return (max == 0) ? tmp : tmp + cf(max - 1, f);
}

int main()
{
	int t, n, i, j, k, count, number, tmp;
	int dp[4] = {0};
	int dp2[4] = {0};
	double C, F, X, min;
	bool isBreak;
	scanf(" %d", &t);
	for(i=0 ; i<t ; i++)
	{
		scanf(" %lf", &C);
		scanf(" %lf", &F);
		scanf(" %lf", &X);
		min = X / 2;
		if (X > 2.0)
		{
			isBreak = false;
			j = 1;
			while(1)
			{
				double tmp = X / (2 + j * F);
				tmp += cf(j-1, F) * C;

				if (tmp > min)
					isBreak = true;
				else
					min = tmp;

				if (isBreak == true)
					break;

				j++;
			}
			
		}

		printf("case #%d: %.7lf\n", i+1, min);
	}
	return 0;
}