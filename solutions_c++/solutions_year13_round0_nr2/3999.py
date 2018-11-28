// test1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"
#include "string.h"
#include "case.h"

void lawn(FILE *fIn, FILE *fOut);
void lawnCase(FILE *fIn, FILE *fOut, int T, int N, int M);
int getMax(int *line, int len);
int equal(int N, int M);

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fIn = fopen("B-large.in", "r+");
	FILE *fOut = fopen("B-large.out", "w+");

	lawn(fIn, fOut);

	fclose(fIn);
	fclose(fOut);

	return 0;
}

int matrix[102][102];
int resMatrix[102][102];

void lawn(FILE *fIn, FILE *fOut) {
	int T;
	fscanf (fIn, "%d\n", &T);

	int N, M;
	for (int i = 0; i < T; i++) {
		fscanf (fIn, "%d %d\n", &N, &M);
		for (int n = 0; n < N; n++) {
			for (int m = 0; m < M; m++) {
				fscanf (fIn, "%d", &matrix[n][m]);
				resMatrix[n][m] = 100;
			}
		}

		lawnCase(fIn, fOut, i, N, M);
	}
}

void lawnCase(FILE *fIn, FILE *fOut, int T, int N, int M) {
	for (int i = 0; i < N; i++) {
		int max = getMax(matrix[i], M);
		for (int j = 0; j < M; j++) {
			resMatrix[i][j] = max;
		}
	}

	for (int i = 0; i < M; i++) {
		int *line = (int *)malloc(sizeof(int) * N);
		for (int j = 0; j < N; j++) {
			line[j] = matrix[j][i];
		}
		int max = getMax(line, N);
		for (int j = 0; j < N; j++) {
			if (resMatrix[j][i] > max) {
				resMatrix[j][i] = max;
			}
		}
	}

	int ret = equal(N, M);
	if (ret == 1) {
		fprintf(fOut, "Case #%d: %s\n", T + 1, "YES");
	}
	else {
		fprintf(fOut, "Case #%d: %s\n", T + 1, "NO");
	}
}

int getMax(int *line, int len) {
	int ret = -1;
	for (int i = 0; i < len; i++) {
		if (line[i] > ret) {
			ret = line[i];
		}
	}

	return ret;
}

int equal(int N, int M) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (matrix[i][j] != resMatrix[i][j]) {
				return 0;
			}
		}
	}
	return 1;
}