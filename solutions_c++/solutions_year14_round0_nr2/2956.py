#include <stdio.h>
#include <string.h>
#include <math.h>
#define min(a, b) ((a)<(b)?(a):(b))
int t;
double c, f, x;

int main() {
	int cas = 0;
	scanf("%d", &t);
	while (t--) {
		scanf("%lf%lf%lf", &c, &f, &x);
		int n = (int)floor((f * x - 2 * c) / (c * f));
		double sum1 = 0;
		if (n < 0) n = 0;
		for (int i = 0; i < n; i++) {
			sum1 += c / (f * i + 2);
		}
		double sum2 = sum1 + c / (f * n + 2);
		sum1 += x / (f * n + 2);
		sum2 += x / (f * (n + 1) + 2);
		double sum = min(sum1, sum2);
		printf("Case #%d: %.7lf\n", ++cas, sum);
	}
	return 0;
}