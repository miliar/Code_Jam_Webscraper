#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>

int K, N;
double P[200];

int comp (const void * a, const void * b) {
	if (*(double *)a < *(double *)b) {
		return -1;
	} else if (*(double *)a > *(double *)b) {
		return 1;
	}
	return 0;
}

double calc(int n) {
	double chance[201];
	for (int i = 1; i <= K; ++i) {
		chance[i] = 0;
	}
	chance[0] = 1;
	for (int i = 0; i < n; ++i) {
		for (int j = K / 2; j >= 0; --j) {
			chance[j + 1] += chance[j] * P[i];
			chance[j] *= 1 - P[i];
		}
	}
	for (int i = N - (K - n); i < N; ++i) {
		for (int j = K / 2; j >= 0; --j) {
			chance[j + 1] += chance[j] * P[i];
			chance[j] *= 1 - P[i];
		}
	}
	return chance[K / 2];
}

int main() {
	FILE * fin = fopen("input.in", "r"), * fout = fopen("output.out", "w");
	int T, t;
	double a, temp;
	fscanf(fin, "%d\n", &T);
	for (t = 1; t <= T; ++t) {
		fscanf(fin, "%d%d\n", &N, &K);
		for (int i = 0; i < N; ++i) {
			fscanf(fin, "%lf", P + i);
		}
		qsort(P, N, sizeof(double), comp);
		a = 0;
		for (int i = 0; i <= K; ++i) {
			temp = calc(i);
			if (a < temp) a = temp;
		}
		fprintf(fout, "Case #%d: %f\n", t, a);
	}
	return 0;
}
