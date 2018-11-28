#include <cstdio>

int main() {
	FILE * fin = fopen("B.in", "r"), * fout = fopen("B.out", "w");
	int T, t, i;
	double C, F, X, time;
	fscanf(fin, "%d", &T);
	for (t = 1; t <= T; ++t) {
		time = 0.0;
		fscanf(fin, "%lf%lf%lf", &C, &F, &X);
		for (i = 0; X / (2.0 + (i + 1) * F) > C / F; ++i) {
			time += C / (2.0 + i * F);
		}
		time += X / (2.0 + i * F);
		fprintf(fout, "Case #%d: %.7f\n", t, time);
	}
	return 0;
}
