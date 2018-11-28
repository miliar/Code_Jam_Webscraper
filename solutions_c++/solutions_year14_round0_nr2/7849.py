#include <stdio.h>

int main()
{
	int tc, ct;
	scanf("%d", &tc);
	for(ct=1;ct<=tc;ct++)
	{
		double c, f, x, next_farm = 0, tnow = 0;
		double production = 2;
		double ans, ans2;
		scanf("%lf %lf %lf",&c,&f,&x);
		ans2 = x / production;
		do
		{
			ans = ans2;
			tnow += (c / production);
			production += f;
			ans2 = tnow + (x / production);
		}
		while(ans > ans2);

		printf("Case #%d: %.7lf\n", ct, ans);
	}
	return 0;
}
