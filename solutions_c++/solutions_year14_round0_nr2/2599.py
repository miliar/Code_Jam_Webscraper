#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T = 0;
	double C, F, X;
	scanf("%d", &T);
	for (int q = 0; q < T; q++)
	{
		scanf("%lf%lf%lf", &C, &F, &X);

		double profit = 2.0, cur_time = X / profit, delay = 0, general = 0;
		while ( true )
		{
			delay = C / profit;
			if ( cur_time > general + delay + X / (profit + F) )
			{
				general += delay;
				profit += F;
				cur_time = general + X / profit;
			} else
				break;
		}
		general += X / profit;
		printf("Case #%d: ", q + 1);
		printf("%.7lf", general);
		if (q != T - 1)
			printf("\n");
	}

	return 0;
}