#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

double C, F, X, T, factime[100005];
int Test, N;

int main(void) {
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &Test);
	for (int t = 1; t <= Test; t++) {
		scanf("%lf %lf %lf", &C, &F, &X);
		factime[0] = 0.0;
		T = X / 2.0;
		double timesum = 0.0;
		for (int i = 1; i <= 100000; i++) {
			factime[i] = factime[i - 1] + (C / (2.0 + (double)(i - 1) * F));
			double curtime = factime[i] + X / (2.0 + (double)i * F);
			if (T > curtime) T = curtime;
		}
		printf("Case #%d: %.7lf\n", t, T);
	}
	return 0;
}