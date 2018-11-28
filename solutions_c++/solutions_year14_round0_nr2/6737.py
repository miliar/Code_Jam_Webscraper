#include <stdio.h>
#include <vector>
using namespace std;

void main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	double C, F, X, time, time_farm,time2, cps;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%lf%lf%lf", &C, &F, &X);
		cps = 2.0;
		time = X / cps;
		time_farm = 0.0;
		for (;;)
		{
			time2 = time_farm + C / cps + X / (cps + F);
			if (time < time2)
			{
				printf("Case #%d: %.7lf\n", i+1, time);
				break;
			}
			else
			{
				time = time2;
				time_farm += C / cps;
				cps += F;
			}
		}
	}
}