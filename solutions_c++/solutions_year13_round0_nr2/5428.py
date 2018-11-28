#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
#include<stdarg.h>

FILE *input;
FILE *output;
int lawn[10][10];
char buff[255];


bool HasPath(int row, int col, int width, int length);

#define DEBUG 1

#define FETCH_E do {\
	memset(buff, 0, 255);\
	fgets(buff, 255, input);\
	if (DEBUG) \
		printf("%s\n", buff);\
	} while(0)

int main(int argC, char *argV[]) {
	char *fileIn = argV[1];
	
	FILE *input = fopen(argV[1], "r");
	FILE *output = fopen("B.out", "w");

	int cases;

	FETCH_E;
	sscanf(buff, "%d", &cases);

	for (int n = 0; n < cases; n++) {
		int row, col;
		FETCH_E;
		sscanf(buff, "%d %d", &row, &col);
		for (int r = 0; r < row; r++) {
			FETCH_E;
			char *p = buff;
			for (int c = 0; c < col; c++) {
				sscanf(p, "%d", &lawn[r][c]);
				p = strchr(p, ' ') + 1;
			}
		}
		fprintf(output, "Case #%d: ", n + 1);
		bool breakFlag = false;
		for (int r1 = 0; r1 < row && !breakFlag; r1++) {
			for (int c1 = 0; c1 < col; c1++) {
				if (!HasPath(r1, c1, row, col)) {
					fprintf(output, "NO\n");
					breakFlag = true;
					break;
				}
			}
		}
		if (!breakFlag)
			fprintf(output, "YES\n");
	}
	fclose(input);
	fclose(output);
	return 0;
}

bool HasPath(int row, int col, int length, int width) {
	int testVal = lawn[row][col];
	if (DEBUG)
		printf("Testing (%d, %d) : %d\n", row, col, testVal);

	bool hasPath = true;
	for (int c = 0; c < width; c++) {
		if (DEBUG)
			printf("\tComparing (%d, %d) : %d;\t Testval:%d\n", row, c, lawn[row][c], testVal);
		
		if (lawn[row][c] > testVal) {
			hasPath = false;
			break;
		}
	}

	if (hasPath)
		return true;
	else if (DEBUG)
		printf("\tPath on row not found\n", row, col, testVal);
		
	hasPath = true;
	for (int r = 0; r < length; r++) {
		if (lawn[r][col] > testVal) {
			hasPath = false;
			break;
		}
	}

	if (DEBUG && !hasPath)
		printf("\tPath on column not found\n", row, col, testVal);
	return hasPath;
}