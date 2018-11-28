#include <stdio.h>
#include <math.h>

double c, f, x;

int main () {

	int t;
	scanf ("%d", &t);
	for (int i = 1; i <= t; i++) {

		scanf ("%lf%lf%lf", &c, &f, &x);
		int n = (int) floor ((f * x - 2 * c)/ (c * f));
		double s1 = 0;
		if (n < 0)
			n = 0;
		for (int j = 0; j < n; j++)
			s1 += c / (f * j + 2);
		double s2 = s1 + c / (f * n + 2);
		s1 += x / (f * n + 2);
		s2 += x / (f * (n + 1) + 2);
		printf ("Case #%d: %.7lf\n", i, s1 < s2 ?s1:s2);

	}
	return 0;
}
