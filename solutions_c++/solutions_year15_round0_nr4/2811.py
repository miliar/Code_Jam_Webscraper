
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <list>
#include <algorithm> 

using namespace std;

#define X_MAX 20
#define R_MAX 20
#define C_MAX 20

#define MAX(a,b) ((a>=b)?(a):(b))

int t, x, r, c;

int main(void) {

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	// richard: pick x, r, c
	// gabriel: make it
	int richard_win = 1;

	fscanf(fp, "%d", &t);
	for (int tc=1; tc<=t; tc++) {

		fscanf(fp, "%d %d %d", &x, &r, &c);

		// check if size is multiple rc = kx
		if ((r * c) % x != 0) {
			richard_win = 1;
			goto done;
		}

		if (r * c < x) {
			richard_win = 1;
			goto done;
		}

		if (x == 1) {
			richard_win = 0;
			goto done;
		}

		if (x == 2) {
			richard_win = 0;
			goto done;
		}

		// make r > c
		if (r < c) {
			int temp = c;
			c = r;
			r = temp;
		}

		// r x 1 case:
		if (c == 1) {
			if (r == 2) {
				richard_win = 0;
				goto done;
			}
			if (r > 2 && x != 2) {
				richard_win = 1;
				goto done;
			}
		}

		// r x 2 case:
		if (c == 2) {
			if (r == 2) {
				if (x == 4)
					richard_win = 1;
				else
					richard_win = 0;
				goto done;
			}
			if (r == 3) {
				richard_win = 0;
				goto done;
			}
			if (r > 3 && r == x) {
				richard_win = 1;
				goto done;
			}
		}

		// r x c case: (r>=3, c>=3)
		if (c >= 3) {
			if (x >= r + c - 1) {
				richard_win = 1;
			} else {
				richard_win = 0;
			}
			goto done;
		}
done:
		if (richard_win) {
			fprintf(ofp, "Case #%d: RICHARD\n", tc);
		} else {
			fprintf(ofp, "Case #%d: GABRIEL\n", tc);
		}
	}

	return 0;
}
