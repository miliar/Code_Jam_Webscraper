#include <stdio.h>
#include <iostream>

using namespace std;

int main (void) {
	int t, cc;
	double r[2], c[2], V, X;
	int n;
	scanf ("%d", &t);
	for (cc = 1; cc <= t; cc++) {
		scanf ("%d%lf%lf", &n, &V, &X);
		printf ("Case #%d: ", cc);
		for (int i = 0; i < n; i++) {
			scanf ("%lf%lf", &r[i], &c[i]);
		}
		if (n == 1) {
			if (c[0] != X)	printf ("IMPOSSIBLE\n");
			else	printf ("%.10lf\n", V/r[0]);
		} else {
			if ((c[0] > X && c[1] > X) || (c[0] < X && c[1] < X))	printf ("IMPOSSIBLE\n");
			else if (c[0] == X && c[1] == X) {
				printf ("%.10lf\n", V/(r[0]+r[1]));
			} else if (c[0] == X) {
				printf ("%.10lf\n", V/r[0]);
			} else if (c[1] == X) {
				printf ("%.10lf\n", V/r[1]);
			} else {
				double a = (c[0]-X), b = (c[1]-X);
				double V1 = a*V/(a-b), V0 = b*V/(b-a);
				double t0 = V0/r[0], t1 = V1/r[1];
				printf ("%.10lf\n", max(t0, t1));
			}
		}
	}
}