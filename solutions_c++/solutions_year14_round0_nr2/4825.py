#include <stdio.h>
#include <math.h>
#define eps 1e-7

int sgn (double x) {
	if (fabs(x) < eps)	return 0;
	return x < 0 ? -1 : 1;
}

int main (void) {
	int t, c;
	double C, F, X;
	double f, p, curr, ans;
	scanf ("%d", &t);
	for (c = 1; c <= t; c++) {
		printf ("Case #%d: ", c);
		scanf ("%lf%lf%lf", &C, &F, &X);
		f = 0;
		p = 2;
		curr = X/2;
		do {
			ans = curr;
			f += C/p;
			p += F;
			curr = f+X/p;
		//	printf ("%.8lf %.8lf\n", curr, ans);
		} while (sgn(curr-ans) < 0);
		printf ("%.8lf\n", ans);
	}
}
