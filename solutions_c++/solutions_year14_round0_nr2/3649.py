#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	freopen("B-large.in", "rb", stdin);
	freopen("2l.txt", "wb", stdout);

	int t, k = 0;
	scanf("%d", &t);
	while(k++ < t)
	{
		double C, F, X;
		double speed = 2.0;
		double cost = 0;
		scanf("%lf%lf%lf", &C, &F, &X);
		if(X <= C)
		{
			printf("Case #%d: %.9lf\n", k, X / speed);
			continue;
		}

		while((X - C) / speed > X / (speed + F))
		{
			cost += C / speed;
			speed += F;
		}

		printf("Case #%d: %.9lf\n", k, cost + X / speed);
	}
	return 0;
}