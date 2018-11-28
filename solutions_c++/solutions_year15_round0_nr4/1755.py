#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

inline int floor(int a) {
	return a / 2 + a % 2;
}

int main()
{
	int testcases;
	FILE *pFile = fopen("D-small-attempt1.in", "r");
	FILE *outFile = fopen("d-small.out", "w");
	fscanf(pFile, "%d", &testcases);
	for (int tc=1; tc<=testcases; tc++) {
		fprintf(outFile, "Case #%d: ", tc);
		int N, R, C;
		fscanf(pFile, "%d%d%d", &N, &R, &C);
		cout << R << " " << C << endl;
		if (N == 1) {
			fprintf(outFile, "GABRIEL\n");
		} else if (N == 2) {
			fprintf(outFile, (R * C) % 2 == 0 ? "GABRIEL\n" : "RICHARD\n");
		} else if (N == 3) {
			if ((R * C) % 3 != 0) {
				fprintf(outFile, "RICHARD\n");
			} else {
				fprintf(outFile, (R == 1 || C == 1) ? "RICHARD\n" : "GABRIEL\n");
			}
		} else {
			if ((R * C) % 4 != 0) {
				fprintf(outFile, "RICHARD\n");
			} else {
				fprintf(outFile, R * C >= 12 ? "GABRIEL\n" : "RICHARD\n");
			}
		}
	}
	return 0;
}