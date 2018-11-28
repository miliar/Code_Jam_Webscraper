#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//*
int main(void) {
	int t = 0;
	int n = 0, m = 0;
	int a[4], b[4], c[4];

	FILE * fp, * fout;
	fp = fopen("A-small-attempt4.in", "r");
	fout = fopen("A-small-attempt4.out", "w");

	fscanf(fp, "%d", &t);
	for (int caseIndex = 0; caseIndex < t; caseIndex++) {
		fscanf(fp, "%d", &n);
		for (int i = 0; i < 4; i++) {
			if (i == n - 1) fscanf(fp, "%d%d%d%d", &a[0], &a[1], &a[2], &a[3]);
			else fscanf(fp, "%d%d%d%d", &c[0], &c[1], &c[2], &c[3]);
		}

		fscanf(fp, "%d", &m);
		for (int i = 0; i < 4; i++) {
			if (i == m - 1) fscanf(fp, "%d%d%d%d", &b[0], &b[1], &b[2], &b[3]);
			else fscanf(fp, "%d%d%d%d", &c[0], &c[1], &c[2], &c[3]);
		}

		int counter = 0;
		int target = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (a[i] == b[j]) {
					counter++;
					target = a[i];
				}
			}
		}

		fprintf(fout, "Case #%d: ", caseIndex + 1);
		switch (counter) {
			case  0: fprintf(fout, "Volunteer cheated!\n");  break;
			case  1: fprintf(fout, "%d\n", target);  break;
			default: fprintf(fout, "Bad magician!\n");  break;
		}
	}

	fclose(fp);
	fclose(fout);

	return 0;
}
//*/