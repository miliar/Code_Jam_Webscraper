#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//*
int main(void) {
	int t = 0;
	double c = 0, f = 0, x = 0;
	double total = 0;
	double time = 0;
	double v = 0;

	FILE * fp, * fout;

	fp = fopen("B-large.in", "r");
	fout = fopen("B-large.out", "w");

	fscanf(fp, "%d", &t);
	for (int caseIndex = 0; caseIndex < t; caseIndex++) {
		fscanf(fp, "%lf%lf%lf", &c, &f, &x);
		total = 0;
		time = 0;
		v = 2;

		if (x <= c) {
			time = x / v;
		}
		else {
			while (total < x) {
				time += c / v;
				total = c;

				if ((x - total) / v < x / (v + f)) {
					time += (x - total) / v;
					break;
				}
				else {
					total = 0;
					v += f;
				}
			}
		}

		fprintf(fout, "Case #%d: %.7lf\n", caseIndex + 1, time);
	}

	fclose(fp);
	fclose(fout);

	return 0;
}
//*/