#include <algorithm>
#include <cmath>
#include <cstdio>
#include <memory.h>

using namespace std;

int main(void)
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for (int tt = 1; tt <= TC; tt++) {
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double D = 2., Ans = X / 2., Cur = 0.;
		while (Cur <= Ans) {
			Ans = min(Ans, Cur + X / D);
			Cur += C / D;
			D += F;
		}
		printf("Case #%d: %.7lf\n", tt, Ans);
	}

	return 0;
}
