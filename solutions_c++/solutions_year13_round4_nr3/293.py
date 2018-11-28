#include <stdio.h>
#include <string.h>

#define INFILE		"erdos.in"
#define OUTFILE		"erdos.out"

int n;
int a[32];
int b[32];
int res[32];
int sol[32];

bool ok(int pos) {
	memset(sol, 0, n*sizeof(int));
	for (int i=0; i<=pos; i++)
		if (res[i] > 0) {
			sol[i] = 1;
			for (int j=0; j<i; j++)
				if (res[j] > 0 && res[j] < res[i] && sol[i] < sol[j] + 1)
					sol[i] = sol[j] + 1;
		}
	if (sol[pos] != a[pos])
		return false;
	sol[pos] = 0;
	for (int i=n-1; i>=pos; i--)
		if (res[i] > 0) {
			sol[i] = 1;
			for (int j=n-1; j>i; j--)
				if (res[j] > 0 && res[j] < res[i] && sol[i] < sol[j] + 1)
					sol[i] = sol[j]+1;
		}
	if (sol[pos] != b[pos])
		return false;
	return true;
}

int recurse(int x) {
	if (x == n + 1)
		return true;

	for (int i=0; i<n; i++)
		if (res[i] == 0 && x >= a[i] && x >= b[i]) {
			res[i] = x;
			if (ok(i) && recurse(x+1))
				return true;
			res[i] = 0;
		}
	return false;
}

void solve(FILE *fin, FILE *fout) {
	int tests;
	fscanf(fin, "%d", &tests);
	for (int t=0; t<tests; t++) {
		fscanf(fin, "%d", &n);
		for (int i=0; i<n; i++)
			fscanf(fin, "%d", a+i);
		for (int i=0; i<n; i++)
			fscanf(fin, "%d", b+i);
		memset(res, 0, sizeof(res));
		recurse(1);
		
		fprintf(fout, "Case #%d: ", t+1);
		for (int i=0; i<n-1; i++)
			fprintf(fout, "%d ", res[i]);
		fprintf(fout, "%d\n", res[n-1]);
	}

}

int main() {
	FILE *fin = fopen(INFILE, "r");
	FILE *fout = fopen(OUTFILE, "w");
	if (!fin) {
		printf("Cannot open input file!\n");
		return 0;
	}
	if (!fout) {
		printf("Cannot open output file!\n");
		return 0;
	}

	solve(fin, fout);

	fclose(fin);
	fclose(fout);
	return 0;
}
