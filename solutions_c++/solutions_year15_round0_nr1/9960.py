#include <stdio.h>

long T, i, j, n, x, s, invite;
int main() {
	FILE *fin = fopen("A-small-attempt1.in","r");
	FILE *fout = fopen("a.out","w+");
	fscanf(fin, "%d", &T);
	for (j = 0; j < T; j++) {
		fscanf(fin, "%d ", &n);
		s = 0;
		invite = 0;
		for (i = 0; i <= n; i++) {
			x = fgetc(fin) - 48;
			if ((x > 0) && (s < i)) {
				invite += i - s;
				s += invite;
			}
			s += x;
		}
		fprintf(fout, "Case #%d: %d\n", j + 1, invite);
		fgetc(fin);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
