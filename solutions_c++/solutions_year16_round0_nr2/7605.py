#include <stdio.h>
#include <string.h>

const int MAX_LEN = 100;

const char HAPPY = '+';
const char BLANK = '-';

char str[MAX_LEN + 2];

int main() {
	int i, t, T, len;
	char last_stat;
	int cnt;

	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("output.txt", "w");

	fscanf(fin, "%d\n", &T);

	for (t = 1; t <= T; t++) {
		fscanf(fin, "%s\n", str);

		len = strlen(str);
		cnt = 0;

		last_stat = str[0];

		for (i = 1; i < len; i++) {
			if (str[i] != last_stat) {
				last_stat = str[i];
				cnt++;
			}
		}

		if (last_stat != HAPPY) cnt++;
		fprintf(fout, "Case #%d: %d\n", t, cnt);
	}	

	return 0;
}
