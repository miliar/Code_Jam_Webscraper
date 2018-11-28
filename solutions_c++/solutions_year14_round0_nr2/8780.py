#include <iostream>
#include <cstring>
#include <cstdio>







int main()
{	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, k;

	scanf("%d", &n);
	for (k=1; k<=n; ++k)
	{
		long float c, f, x, time, speed;
		scanf("%lf%lf%lf", &c, &f, &x);
		speed=2;
		time=0;
		while ((x/speed)>(c/speed+x/(speed+f)))
		{
			time=time+c/speed;
			speed=speed+f;
		}
		time=time+x/speed;

		printf("Case #%d: %.7lf\n", k, time);
	}
	
	return 0;
}