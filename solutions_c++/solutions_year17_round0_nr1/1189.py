#include <stdio.h>
#include <string.h>

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int T, S, K;
char data[2000];

int main(void) {
	int i, j, k;
	int cnt;
	bool er;
	fscanf(in, "%d", &T);
	for (i = 1;i <= T;i ++) {
		cnt = 0; er = 0;
		fscanf(in, "%s %d", &data[1], &K);
		S = strlen(&data[1]);

		for (j = 1;j <= S;j ++) {
			if (data[j] == '-') {
				if (j+K-1 > S) {
					er = 1; break;
				}
				cnt ++;
				for (k = 0;k < K;k ++) {
					if (data[j+k] == '-') data[j+k] = '+';
					else data[j+k] = '-';
				}
			}
		}

		if (er == 1) {
			fprintf(out, "Case #%d: IMPOSSIBLE\n", i);
		} else fprintf(out, "Case #%d: %d\n", i, cnt);

	}

}