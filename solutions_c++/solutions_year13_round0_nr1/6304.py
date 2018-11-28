// P1.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

void solve(int n, char B[4][4], FILE *fp)
{
	int i, j;
	int dot = 0;
	//int row[4], col[4], dia[2];
	int st[10];
	char line[16] = {'\0'};
	int val;

	for (i=0; i<4; i++) {
		for (j=0; j<4; j++) {
			switch(B[i][j]) {
			case '.':
				dot = 1;
				B[i][j] = '4';
				break;
			case 'T':
				B[i][j] = '1';
				break;
			case 'X':
				B[i][j] = '2';
				break;
			case 'O':
				B[i][j] = '3';
				break;
			}
		}
	}

	// 4 rows
	for (i=0; i<4; i++) {
		strncpy(line, B[i], 4);
		st[i] = atoi(line);
		//printf("%d\n", st[i]);
	}

	// 4 cols
	for (i=0; i<4; i++) {
		for (j=0; j<4; j++) {
			line[j] = B[j][i];
		}
		st[i+4] = atoi(line);
		//printf("%d\n", st[i+4]);
	}

	// 2 diagnoses
	for (i=0; i<4; i++) {
		line[i] = B[i][i];
	}
	st[8] = atoi(line);
	//printf("%d\n", st[8]);

	for (i=0; i<4; i++) {
		line[i] = B[i][3-i];
	}
	st[9] = atoi(line);
	//printf("%d\n", st[9]);

	for (i=0; i<10; i++) {
		val = st[i];
		switch(val) {
		case 2222:
		case 2221:
		case 2212:
		case 2122:
		case 1222:
			fprintf(fp, "Case #%d: X won\n", n);
			return;
		case 3333:
		case 3331:
		case 3313:
		case 3133:
		case 1333:
			fprintf(fp, "Case #%d: O won\n", n);
			return;
		}
	}

	if (dot) {
		fprintf(fp, "Case #%d: Game has not completed\n", n);
	} else {
		fprintf(fp, "Case #%d: Draw\n", n);
	}
}

int main(int argc, char* argv[])
{
	FILE *fpi, *fpo;
	char line[128];
	int T;
	int i, j;
	char B[4][4];

	fpi = fopen("A-large.in", "r");
	fpo = fopen("A-large.out", "w");

	fgets(line, 128, fpi);
	sscanf(line, "%d", &T);

	for (i=0; i<T; i++) {
		for (j=0; j<4; j++) {
			fgets(line, 128, fpi);
			strncpy(B[j], line, 4);
		}
		fgets(line, 128, fpi); //discard new line
		solve(i+1, B, fpo);
	}

	fclose(fpi);
	fclose(fpo);
	return 0;
}

