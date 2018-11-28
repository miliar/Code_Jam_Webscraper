#include <stdio.h>

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		double C, F, X;
		double time = 0.0, speed = 2.0;
		
		scanf("%lf %lf %lf", &C, &F, &X);
		
		while(true)
		{
			if(X / speed < C / speed + X / (speed + F))
			{
				time += X / speed;
				break;
			}
			else
			{
				time += C / speed;
				speed += F;
			}
		}
		
		printf("Case #%d: %.7lf\n", t, time);
	}
	
	return 0;
}

