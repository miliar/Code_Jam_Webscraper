/*
 * b.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: cacevedo
 */

#include <iostream>
#include <cstdlib>
#include <cstdio>

bool check(int lawn[100][100], int n, int m) {
	int maxC[100], maxR[100];
	for (int i = 0; i < n; ++i) {
		maxR[i] = 0;
	}
	for (int i = 0; i < m; ++i) {
		maxC[i] = 0;
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (maxC[j] < lawn[i][j]) maxC[j] = lawn[i][j];
			if (maxR[i] < lawn[i][j]) maxR[i] = lawn[i][j];
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (lawn[i][j] != maxR[i] && lawn[i][j] != maxC[j]) {
				return false;
			}
		}
	}
	return true;
}

int main () {
	int T, total;
	int n,m;
	int lawn[100][100];

	FILE * file = fopen("test.txt", "r"),
			* result = fopen("result.txt", "w");

	fscanf(file, "%d\n", &total);
	T = total + 1;
	while (total) {
		fscanf(file, "%d %d\n", &n, &m);

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				fscanf(file, "%d", &lawn[i][j]);
			}
			fscanf(file, "\n");
		}
		if (n == 1 || m == 1) {
			fprintf(result, "Case #%d: YES\n", T-total);
		} else {
			if (check(lawn, n, m)) {
				fprintf(result, "Case #%d: YES\n", T-total);
			} else {
				fprintf(result, "Case #%d: NO\n", T-total);
			}
		}

		total --;
	}

	fclose(file);
	fclose(result);

	return 0;
}
