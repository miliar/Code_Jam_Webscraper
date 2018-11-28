#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double c, f, x;

double cal(int times)
{
	int i;
	double t1 = x/(times*f + 2);
	for (i = 1; i <= times; i++)
	{
		t1 += c/(2+(i-1)*f);
	}
	return t1;
}


main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int nc;
	int t = 0;
	scanf("%d", &nc);
	while (t++ < nc)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		int n = (int)(x/c - 2/f);
		if (n <= 0)
		{
			n = 0;
		}
		double minT = cal(n);
		printf("Case #%d: %.7lf\n", t, minT);
	}
	return 0;
}