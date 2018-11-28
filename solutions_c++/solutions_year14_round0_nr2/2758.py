#include <stdio.h>
#include <stdlib.h>

int test, tt;
double cost, profit, target, time_pass, pps, ans, temp;

int main()
{
	freopen("B-large.in", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--)
	{
		scanf("%lf %lf %lf", &cost, &profit, &target);
		pps = 2.0;
		time_pass = 0.0;
		ans = target / pps;
		while (1)
		{
			temp = time_pass + cost / pps + target / (pps + profit);
			if (temp > ans + 1e-9)
				break;
			ans = temp;
			time_pass += cost / pps;
			pps += profit;
		}
		
		printf("Case #%d: %.7f\n", ++tt, ans);
	}
	
	return 0;
}
