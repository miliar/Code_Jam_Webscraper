#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>

int main(void) {
	FILE * iff = fopen("in", "r");
	FILE * off = fopen("out", "w");
	int T;
	fscanf(iff, "%d", &T);
	for (int cse = 1; cse <= T; ++cse) {
		int X,R,C;
		fscanf(iff, "%d %d %d", &X, &R, &C);
		if (X == 1) {
			fprintf(off, "Case #%d: GABRIEL\n",cse);
		} else if (X == 2) {
			if ((R * C) % 2 != 0) {
				fprintf(off, "Case #%d: RICHARD\n", cse);
			} else {
				fprintf(off, "Case #%d: GABRIEL\n", cse);
			}
		} else if (X == 3) {
			if (R * C <= 3) {
				fprintf(off, "Case #%d: RICHARD\n", cse);
			} else if ((R * C) % 3 != 0) {
				fprintf(off, "Case #%d: RICHARD\n", cse);
			} else {
				fprintf(off, "Case #%d: GABRIEL\n", cse);
			}
		} else if (X == 4) {
			if (R * C <= 4 || R * C == 8) {
				fprintf(off, "Case #%d: RICHARD\n", cse);
			} else if ((R * C) % 4 != 0) {
				fprintf(off, "Case #%d: RICHARD\n", cse);
			} else {
				fprintf(off, "Case #%d: GABRIEL\n", cse);
			}
		}
	}
	fclose(iff);
	fclose(off);
	return 0;
}