#include <stdio.h>
#include <string.h>

int main() {
	int t = 0;
	int	num = 0;
	FILE *in;
	FILE *out;

	int lawn[100][100];
	bool flag[100][100];

	in = fopen("B-small-attempt0.in", "r");
	//in = fopen("test.txt", "r");
	out = fopen("out.txt", "w");

	fscanf(in, "%d", &t);
	while (num ++ < t) {
		memset(lawn, 100, sizeof(int) * 100 * 100);
		memset(flag, false, sizeof(bool) * 100 * 100);

		int n, m;
		fscanf(in, "%d %d", &n, &m);

		int i, j;
		for (i = 0; i < n; i ++) {
			for (j = 0; j < m; j ++) {
				fscanf(in, "%d", &lawn[i][j]);
			}
		}

		for (i = 0; i < n; i ++) {
			for (int start = 100; start >= 1; start --) {
				bool temp[100];
				for (j = 0; j < m; j ++) {
					if (start == lawn[i][j]) {
						temp[j] = true;
					} else if (start > lawn[i][j]) {
						temp[j] = false;
					} else {
						break;
					}
				}
				if (j == m) {
					for (j = 0; j < m; j ++) {
						if (temp[j] == true) {
							flag[i][j] = true;
						}
					}
				}
			}
		}

		for (i = 0; i < m; i ++) {
			for (int start = lawn[0][i]; start >= 1; start --) {
				bool temp[100];
				for (j = 0; j < n; j ++) {
					if (start == lawn[j][i]) {
						temp[j] = true;
					} else if (start > lawn[j][i]) {
						temp[j] = false;
					} else {
						break;
					}
				}
				if (j == n) {
					for (j = 0; j < n; j ++) {
						if (temp[j] == true) {
							flag[j][i] = true;
						}
					}
				}
			}
		}

		bool result = true;
		for (i = 0; i < n && result; i ++) {
			for (j = 0; j < m && result; j ++) {
				if (flag[i][j] == false) {
					result = false;
				}
			}
		}

		if (result == true) {
			fprintf(out, "Case #%d: YES\n", num);
		}
		else {
			fprintf(out, "Case #%d: NO\n", num);
		}
	}

	fclose(in);
	fclose(out);
	return 0;
}