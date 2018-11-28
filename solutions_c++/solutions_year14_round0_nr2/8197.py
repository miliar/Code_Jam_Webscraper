#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int TT;
	scanf("%d", &TT);
	for (int T = 1; T <= TT; T++) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double add = 2;
		double time = 0;
		double best = x/add;
		while (time < best) {
			time += c / add;
			add += f;
			double total = time + x / add;
			if (total < best)
				best = total;
		}


		printf("Case #%d: %.16lf\n", T, best);
	}
}