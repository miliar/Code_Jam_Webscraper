#include <fstream>
#include <iostream>
#include <stdio.h>

FILE *fin = fopen("input.txt", "r");
FILE *fout = fopen("output.txt", "w");

using namespace std;

char data[1111];

int main() {
	int i, j, T, n;
	char cnum;
	int num;
	int result;
	int ableLimit;

	fscanf(fin, "%d", &T);

	for (i = 0; i < T; i++) {
		fscanf(fin, "%d %s", &n, &data);

		result = ableLimit = 0;

		for (j = 0; j <= n; j++) {
			num = data[j] - '0';
			if (j <= ableLimit) {
				ableLimit += num;
			}
			else {
				result += (j - ableLimit);
				ableLimit = j;
				ableLimit += num;
			}
		}

		fprintf(fout, "Case #%d: %d\n", i + 1, result);
	}
	return 0;
}