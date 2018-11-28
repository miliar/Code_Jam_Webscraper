#include <stdio.h>

int main()
{
	int t, T;
	double C, F, X, R, best, cur, time;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		R = 2.0;
		cur = 0.0;
		best = 1e10;
		scanf("%lf%lf%lf", &C, &F, &X);
		while (cur < best) {
			time = X / R + cur;
			if (time < best) best = time;
			cur += C / R;
			R += F;
		}
		printf("Case #%d: %.7lf\n", t, best);
	}

	return 0;
}

