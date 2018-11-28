#include <cstdio>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, TC;
	scanf("%d", &T);
	TC = T;
	while (TC--) {
		double C, F, X, curr, ans, rate;
		scanf("%lf%lf%lf", &C, &F, &X);
		curr = 0;
		ans = 0;
		rate = 2;
		while (X - curr >= 1e-6) {
			if (curr + C >= X) {
				ans += (X - curr) / rate;
				break;
			} else {
				curr += C;
				ans += C / rate;
				if (((X - curr) / rate) > ((X - curr + C) / (rate + F))) {
					rate += F;
					curr -= C;
				}
			}
		}
		printf("Case #%d: %.7lf\n", T - TC, ans);
	}
}
