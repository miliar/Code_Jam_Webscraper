#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//*
 void sort(double * a, int start, int end) {
	double mid = a[(start + end) / 2];
	int i = start, j = end;
	double tmp;

	while (i <= j) {
		while (a[i] > mid) i++;
		while (a[j] < mid) j--;
		if (i <= j) {
			tmp = a[i];
			a[i] = a[j];
			a[j] = tmp;
			i++;
			j--;
		}
	}

	if (j > start) sort(a, start, j);
	if (i < end) sort(a, i, end);
}

int main(void) {
	int t = 0;
	int n = 0;
	int win1 = 0, win2 = 0;
	double a[2][1050];

	FILE * fp, * fout;
	fp = fopen("D-large.in", "r");
	fout = fopen("D-large.out", "w");

	fscanf(fp, "%d", &t);
	for (int caseIndex = 0; caseIndex < t; caseIndex++) {
		fscanf(fp, "%d", &n);
		for (int j = 0; j < 2; j++) {
			for (int i = 0; i < n; i++) {
				fscanf(fp, "%lf", &a[j][i]);
			}
		}

		win1 = win2 = 0;
		if (n == 1) {
			if (a[0][0] > a[1][0]) win1 = win2 = 1;
		}
		else {
			sort(a[0], 0, n - 1);
			sort(a[1], 0, n - 1);
			// War
			int head[2] = { 0, 0 };
			int tail[2] = { n - 1, n - 1 };

			for (int i = 0; i < n; i++) {
				if (a[0][head[0]] > a[1][head[1]]) {
					win2++;
					head[0]++;
					tail[1]--;
				}
				else {
					head[0]++;
					head[1]++;
				}
			}

			// Deceitful War
			head[0] = head[1] = 0;
			tail[0] = tail[1] = n - 1;

			if (a[0][0] > a[1][n - 1]) {
				for (int i = 0; i < n; i++) {
					if (a[0][tail[0]] > a[1][tail[1]]) {
						tail[0]--;
						tail[1]--;
						win1++;
					}
					else {
						tail[0]--;
						head[1]++;
					}
				}
			}
		}
		
		fprintf(fout, "Case #%d: %d %d\n", caseIndex + 1, win1, win2);
	}

	fclose(fp);
	fclose(fout);

	return 0;
}
//*/