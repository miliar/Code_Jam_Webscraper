#include <cstdio>
int t;
long double per_sec, time, C, F, X, akt, prev;
int main () {
	scanf ("%d", &t);
	for (int i = 1; i <= t; i ++) {
		per_sec = 2, time = 0;
		scanf ("%llf %llf %llf", &C, &F, &X);
		akt = X/per_sec;

		do {
			prev = akt;
			
			time += C/per_sec;
			per_sec += F;

			akt = time + X/per_sec;

		} while (akt < prev);
		printf ("Case #%d: %.7llf\n", i, prev);
		
	}
}
