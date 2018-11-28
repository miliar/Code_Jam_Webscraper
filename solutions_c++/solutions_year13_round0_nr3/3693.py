// test1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"
#include "string.h"
#include "case.h"
#include <math.h>

void fair(FILE *fIn, FILE *fOut);
void fairCase(FILE *fIn, FILE *fOut, int T, unsigned long long A, unsigned long long B);
bool fairCheck(unsigned long long  num);

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fIn = fopen("C-small-attempt0.in", "r+");
	FILE *fOut = fopen("C-small-attempt0.out", "w+");

	fair(fIn, fOut);

	fclose(fIn);
	fclose(fOut);

	return 0;
}

void fair(FILE *fIn, FILE *fOut) {
	int T;
	fscanf (fIn, "%d\n", &T);

	unsigned long long A = 0, B = 0;
	for (int i = 0; i < T; i++) {
		fscanf (fIn, "%I64u %I64u\n", &A, &B);
		fairCase(fIn, fOut, i, A, B);
	}
}

void fairCase(FILE *fIn, FILE *fOut, int T, unsigned long long A, unsigned long long B) {
	unsigned long long ret = 0;
	unsigned long long root = sqrt((long double)A);

	while (root * root < A) {
		root++;
	}

	unsigned long long cur = 0;
	while ((cur = root * root) <= B) {
		if (fairCheck(root)) {
			if (fairCheck(cur)) {
				//fprintf(fOut, "%I64u %I64u\n", cur, root);
				ret++;
			}
		}
		root++;
	}

	fprintf(fOut, "Case #%d: %Lu\n", T + 1, ret);
}

bool fairCheck(unsigned long long num) {
	unsigned long long temp = num;
	char strNum[104];
	int len = 0;
	while (temp > 0) {
		strNum[len] = (char)(temp % 10 + '0');
		temp = temp / 10;
		len = len++;
	}

	int i = 0; 
	int j = len - 1;
	for (; i < j;) {
		if (strNum[i] != strNum[j]) {
			return false;
		}
		i++;
		j--;
	}

	return true;
}