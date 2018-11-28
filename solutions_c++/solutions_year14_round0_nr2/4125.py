#include <cstdio>

int main(int argc, char const *argv[])
{
	double rate = 2.0, c, f, x, cookies;
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		rate = 2.0;
		cookies = 0;
		double tempo = 0;
		double twin  = (x) / rate;
		double tfarm = (c) / rate + x / (rate + f);
		while (twin > tfarm)
		{
			tempo += (c) / rate;
			rate += f;
			twin  = x / rate;
			tfarm = c / rate + x / (rate + f);
		}
		printf("Case #%d: %.7lf\n", t, tempo + twin);
	}

	return 0;
}