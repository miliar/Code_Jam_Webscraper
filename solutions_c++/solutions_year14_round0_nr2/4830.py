#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T;
	double C,F,X;
	scanf("%d",&T);
	for (int t = 1; t <= T; ++t)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		double preTime = -1, currTime = -1;
		double speed = 2.0;
		int farm = 0;
		while (true)
		{
			currTime = 0;
			speed = 2;
			for (int i = 1; i <= farm; ++i)
			{
				currTime = currTime + C/speed;
				speed = speed + F;
			}
			currTime += X/speed;
			if (preTime == -1 || currTime < preTime)
			{
				preTime = currTime;
				farm++;
			}
			else
			{
				break;
			}
		}
		printf("Case #%d: %.7lf\n",t,preTime);
	}
	return 0;
}