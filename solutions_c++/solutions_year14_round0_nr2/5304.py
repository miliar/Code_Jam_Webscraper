#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void work()
{
	double C, F, X;
	scanf("%lf%lf%lf", &C, &F, &X);
	double rate = 2.0;
	double elapsed = 0;
	double bestTime = 1e30;
	while (elapsed < bestTime) {
		// wait cookie
		if (elapsed + X / rate < bestTime)
			bestTime = elapsed + X / rate;
		// buy farm
		elapsed += C / rate;
		rate += F;
	}
	static int ttt = 0;
	printf("Case #%d: %.7f\n", ++ttt, bestTime);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	while (T--) work();
}