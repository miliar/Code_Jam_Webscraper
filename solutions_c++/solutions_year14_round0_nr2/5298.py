#include <stdio.h>

int main()
{
	int dat;
	scanf("%d", &dat);
	for (int cas = 1; cas <= dat; ++cas) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		int n = x / c - 2 / f;
		if (n < 0) n = 0;
		double s = x / (2 + n * f);
		for (int i = 0; i < n; ++i) s += c / (2 + i * f);
		printf("Case #%d: %.7f\n", cas, s);
	}
}
