#include <cstdio>

int main()
{
	int t;
	scanf("%d", &t);
	for (int cn=1; cn<=t; ++cn)
	{
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);

		double goal = x / 2;
		double minv = goal;

		for (double start = c / 2, rate = 2 + f; start < minv; start += c / rate, rate += f)
		{
			double nv = start + x / rate;
			if (nv < minv)
			{
				minv = nv;
			}
		}
		
		printf("Case #%d: %.7f\n", cn, minv);
	}

	return 0;
}