#include <stdio.h>

#define EPS 1e-8

double c, f, x;

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int t, tt=0;
	scanf ("%d", &t);
	while (t--) {
		scanf ("%lf%lf%lf", &c, &f, &x);

		int n=0;
		double ans = 1e10;
		double acc = 0, speed = 2.0;
		while (ans > acc + EPS) {
			if (ans > acc + x / speed)
				ans = acc + x / speed;
			acc += c / speed;
			speed += f;
			n++;
		}

		printf ("Case #%d: %.7lf\n", ++tt, ans);
	}

	return 0;
}
