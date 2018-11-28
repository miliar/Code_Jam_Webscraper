#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>

using namespace std;

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++TK);

		double C = 0.0;
		double F = 0.0;
		double X = 0.0;
		scanf("%lf %lf %lf",&C,&F,&X);
		double ans = X / 2.0;
		double speed = 2.0;
		double machineTime = 0.0;
		while(true)
		{
			double thisTime = machineTime + C/speed;
			speed += F;
			machineTime = thisTime;
			ans = min(ans, machineTime + X/speed);
			if(machineTime > ans) break;
		}
		printf("%.7f\n",ans);
	}
	return 0;
}