#include <stdio.h>
#include <math.h>

int counter = 0;
void make() {
	printf("Case #%d: ", ++counter);

	long long r; scanf("%lld", &r);
	long long t; scanf("%lld", &t);

	double a = 2;
	double b = 2*r -1;
	double c = -t;

	int i = (int) ((-b + sqrt(b * b - 4 * a *c)) / (2 * a));

	if (b == 2*r) --i;

	printf("%d\n", i);
}

int main() {
	int t; scanf("%d", &t);
	while(t--) {
		make();
	}
	return 0;
}