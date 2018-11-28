#include <stdio.h>

int main()
{
	/*freopen("sample.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
*/
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		double C,F,X;
		scanf("%lf %lf %lf", &C, &F, &X);
		double cur = 0.0;
		double curratio = 2;
		double time = 0.0;
		while(cur < X)
		{
			if(cur < C)
			{
				if(C < X)
				{
					time += C / curratio;
					cur = C;
				}
				else
				{
					time += X / curratio;
					break;
				}
			}
			else if(cur == C)
			{
				double t1 = (X - cur) / curratio;
				double t2 = X / (curratio + F);
				if(t1 < t2)
				{
					time += t1;
					break;;
				}
				else
				{
					cur = 0.0;
					curratio += F;
				}
			}
		}
		printf("Case #%d: %.7lf\n", i, time);
	}
}