#include <cstdio>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int q = 1; q <= t; q++) {
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);

		double min = x * 0.5;

		int n = 0;
		double tt = 0;
		double total, prev;

		prev = min;
		while (true) {
			tt += c / (2 + n * f);
			total = tt + x / (2 + (n  + 1) * f);

			if (total > prev) break;

			if (total < min) {
				min = total;
			}

			prev = total;
			n++;
		}

		printf("Case #%d: %.7lf\n", q, min);
	}

	return 0;
}