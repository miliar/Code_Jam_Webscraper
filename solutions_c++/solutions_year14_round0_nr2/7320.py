#include <stdio.h>


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b-outLarge.txt", "w", stdout);

	int tc, i;
	double c, x, f, rem, t, rate;

	c = f = x = 0.0000000;

	scanf("%d", &tc);

	for (i = 1; i <= tc; i++) {

		scanf("%lf %lf %lf", &c, &f, &x);
		t = 0.0000000;
		rate = 2.0000000;

		while (1) {

			if (c >= x) {
				t += (x / rate);
				break;
			}

			t += c / rate;

			if ((x / (rate + f)) <= ((x - c) / rate)) {
				rate += f;
			}
			else {
				t += (x-c) / rate;
				break;
			}
		}

		printf("Case #%d: %.7f\n", i, t);
	}
	return 0;
}