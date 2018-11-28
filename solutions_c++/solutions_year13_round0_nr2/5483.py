#include <stdio.h>

int lawn[100][100];
int want[100][100];

int verticleAllOne(int k, int n) {
	int j;
	for (j = 0; j < n; j++) {
		if (want[j][k] != 1) {
			return 0;
		}
	}
	return 1;
}

int main() {
	int t, n, m;
	int i, j, k, temp;
	int height, notPossible, dif;
	FILE *fin, *fout;

	fin = fopen("B-small-attempt2.in", "r");
	fout = fopen("B-small-attempt2.out", "w");

	fscanf(fin, "%d", &t);

	for (i = 1; i <= t; i++) {
		notPossible = 0;
		fscanf(fin, "%d %d", &n, &m);

		for (j = 0; j < n; j++) {
			for (k = 0; k < m; k++) {
				fscanf(fin, "%d", &want[j][k]);
			}
		}

		for (j = 0; j < n; j++) {
			dif = 0;
			temp = want[j][0];

			for (k = 1; k < m; k++) {
				if (temp != want[j][k]) {
					dif = 1;
					break;
				}
			}
			if (dif == 1) {
				for (k = 0; k < m; k++) {
					if (want[j][k] == 1) {
						if (verticleAllOne(k, n)) {
						} else {
							notPossible = 1;
							goto out;
						}
					}
				}
				dif = 0;
			}
		}
		out: if (notPossible) {
			fprintf(fout, "Case #%d: NO\n", i);
		} else {
			fprintf(fout, "Case #%d: YES\n", i);
		}
	}

	return 0;
}
