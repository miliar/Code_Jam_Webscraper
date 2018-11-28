#include <stdio.h>


int
main(void)
{
	int T;
	double c, f, x;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		double speed = 2.0;
		double eta = x / speed;
		double tl = 0.0;
		while(c/speed + (x/(speed+f)) + tl < eta)
		{
			tl += c/speed;
			speed += f;
			eta = (x/speed) + tl;
		}
		printf("Case #%d: %.7lf\n", t, eta);
	}
	return 0;
}
