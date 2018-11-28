#include <cstdio>
int main(int argc, char* argv[])
{
	double c, f, x, t, t1, t2, delta;
	unsigned int n, farmCount = 0;
	scanf("%d", &n);
	for (unsigned i = 1; i <= n; i++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		if (x <= c)
		{
			t = x / 2;
			printf("Case #%d: %.7lf\n", i, t);
			continue;
		}
		t = t1 = t2 = 0.0;
		t1 = 0.0;
		t2 = 0.0;
		delta = x - c;
		farmCount = 0;
		do
		{
			t += c / (2.0 + f*farmCount);
			t1 = x / (2.0 + f*(farmCount + 1));
			t2 = delta / (2.0 + f*farmCount);
			if (t1 < t2)
				farmCount++;
		} while (t1 < t2);
		t += t2;
		printf("Case #%d: %.7lf\n", i, t);
	}
	return 0;
}

