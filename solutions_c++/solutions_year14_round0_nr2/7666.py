#include <cstdlib>
#include <cstdio>

int main()
{
	int TC;
	scanf("%d", &TC);

	for (int tc = 1; tc <= TC; ++tc) {
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);

		double t = 0.0;
		double cps = 2.0;
		while (1) {
			double stf = C / cps;
			double stfx = stf + X / (cps + F);
			double stx = X / cps;
			if (stx < stfx) {
				printf("Case #%d: %0.7lf\n", tc, t + stx);
				break;
			} else {
				t += stf;
				cps += F;
			}
		}
	}
	return 0;
}