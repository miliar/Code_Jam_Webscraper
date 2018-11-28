#include <cstdio>

#define MIN(a, b) (a < b) ? a : b

const double eps = 1e-9;

int leq(double a, double b) {
	if (a <= b) return 1;
	return (b - a < eps);
}

int main(void) {
	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("B-large.out", "w");
	
	int T;
	fscanf(fin, "%d", &T);
	
	for (int t = 1; t <= T; t++) {
		double C, F, X;
		fscanf(fin, "%lf %lf %lf", &C, &F, &X);
		
		double rate = 2.0, time = 0.0;
		double best = X/rate;
		
		while (time <= best) {
			if (time + X/rate < best) best = time + X/rate;
			
			time += C/rate;
			rate += F;
		}
		
		best = MIN(best, time);
		
		fprintf(fout, "Case #%d: %.7lf\n", t, best);
	}

	return 0;
}