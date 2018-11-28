#include <cstdio>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);
		double cps = 2;
		double res = X / cps;
		double curtime = 0;
		while (true) {
			curtime += C / cps;
			cps += F;
			double improved = curtime + X / cps;
			if (improved > res) {
				break;
			}
			res = improved;
		}
		printf("Case #%d: %.7f\n", tc + 1, res);
	}
}