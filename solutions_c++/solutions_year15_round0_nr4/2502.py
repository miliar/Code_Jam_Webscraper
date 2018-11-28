#include <cstdio>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

typedef enum { GA, RI } Result;

int main() {
	FILE *fin = fopen("D-small-attempt0.in", "r");
	FILE *fout = fopen("D-small-attempt0.out", "w");
	int T;
	fscanf(fin, "%d", &T);
	for (int TestCase = 1; TestCase <= T; TestCase++) {
		int X, R, C;
		Result rs = GA;
		fscanf(fin, "%d %d %d", &X, &R, &C);
		if (R < C) swap(R, C);
		if ((R * C) % X != 0 || X >= 7)
			rs = RI;
		else if (X == 1) {
			if (R < 1 || C < 1)
				rs = RI;
		}
		else if (X == 2) {
			if (R < 2 || C < 1)
				rs = RI;
		}
		else if (X == 3) {
			if (R < 3 || C < 2)
				rs = RI;
		}
		else if (X == 4) {
			if (R < 4 || C < 3)
				rs = RI;
		}
		else if (X == 5) {
			if (R < 5 || C < 4)
				rs = RI;
		}
		else if (X == 6) {
			if (R < 6 || C < 4)
				rs = RI;
		}

		fprintf(fout, "Case #%d: %s\n", TestCase, (rs == GA) ? "GABRIEL" : "RICHARD");
	}

	return 0;
}