#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//*
int notfit(int p, int q) {
	if ((q & (q - 1)) == 0) return 0;

}

int main(void) {
	FILE * fp = NULL;
	FILE * fout = NULL;
	int t = 0;
	int p = 0, q = 0;
	int gen = 0;

	if (fopen_s(&fp, "A-small-attempt0.in", "r") != NULL) return -1;
	if (fopen_s(&fout, "A-small.out", "w") != NULL) return -1;

	fscanf(fp, "%d", &t);
	for (int caseIndex = 1; caseIndex <= t; caseIndex++) {
		fscanf(fp, "%d/%d", &p, &q);

		gen = 1;
		double f = (double)p / q;
		while (f < 0.5) {
			gen++;
			if (gen > 40) break;
			f *= 2;
		}

		if (gen > 40 || notfit(p, q)) fprintf(fout, "Case #%d: impossible\n", caseIndex);
		else fprintf(fout, "Case #%d: %d\n", caseIndex, gen);
	}

	fclose(fout);
	fclose(fp);

	return 0;
}
//*/