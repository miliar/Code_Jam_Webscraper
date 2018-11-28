#include <cstdio>
#include <cstdlib>

int comp(const void * a, const void * b) {
	return *(int *)a - *(int *)b;
}

int main() {
	FILE * fin = fopen("A.in", "r"), * fout = fopen("A.out", "w");
	int t, T;
	int i, j, N, X, S[10000];
	fscanf(fin, "%d", &T);
	for (t = 1; t <= T; ++t) {
		fscanf(fin, "%d%d", &N, &X);
		for (i = 0; i < N; ++i) {
			fscanf(fin, "%d", S + i);
		}
		qsort(S, N, 4, comp);
		j = 0;
		for (i = N - 1; i >= j; --i) {
			if (S[i] + S[j] <= X) {
				++j;
			}
		}
		fprintf(fout, "Case #%d: %d\n", t, N - i - 1);
	}
	return 0;
}
