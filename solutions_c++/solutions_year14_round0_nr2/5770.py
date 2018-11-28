#include <cstdio>

int nCases;
double c, f, x;

int main() {
	scanf("%d", &nCases);
	for (int cs = 0; cs < nCases; cs++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		double best, newtime;
		double rate = 2;
		newtime = x / rate;
		best = x / rate;
		bool done = false;
		while (done == false) {
			double newrate = rate + f;
			newtime -= (x/rate);
			newtime += (c/rate)+(x / newrate);
			if (newtime < best){
				 best = newtime;

			} else {
				done = true;
			} 
			rate = newrate;
		}
		printf("Case #%d: %.7lf\n", cs+1, best);
	}
	return 0;
}
