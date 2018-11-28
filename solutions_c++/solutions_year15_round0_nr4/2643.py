#include <stdio.h>

FILE *fin = fopen("input.txt", "r");
FILE *fout = fopen("output.txt", "w");

int x, r, c;
int data[5][5][5];

void preprocess();
int max(int a, int b);

int main() {
	int i;
	int T;

	preprocess();

	fscanf(fin, "%d", &T);

	for (i = 0; i < T; i++) {
		fscanf(fin, "%d %d %d", &x, &r, &c);
		if (data[x][r][c] == 1) {
			fprintf(fout, "Case #%d: RICHARD\n", i + 1);
		}
		else {
			fprintf(fout, "Case #%d: GABRIEL\n", i + 1);
		}
	}
	return 0;
}

void preprocess() {
	int i, j, k;
	int w, h;

	for (i = 1; i <= 4; i++) {
		for (j = 1; j <= 4; j++) {
			for (k = 1; k <= 4; k++) {
				if (i > max(j, k)) {
					data[i][j][k] = 1;
				}
				else {
					if (i == 1) w = h = 1;
					else if (i == 2) {
						w = 2;
						h = 1;
					}
					else if (i == 3) {
						w = h = 2;
					}
					else if (i == 4) {
						w = 3;
						h = 2;
					}

					int ww = max(j, k);
					int hh = j + k - ww;

					if (w > ww || h > hh) data[i][j][k] = 1;

					if ((j*k) % i != 0) data[i][j][k] = 1;

				}
			}
		}
	}
	data[4][4][2] = data[4][2][4] = 1;
}

int max(int a, int b) {
	if (a > b)return a;
	return b;
}