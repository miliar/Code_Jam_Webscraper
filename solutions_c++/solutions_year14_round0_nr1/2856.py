//============================================================================
// Name        : MagicTrick.cpp
// Author      : J.Son
// Version     :
// Copyright   : GNU LGPL
// Description : 2014 Google Code Jam Qualification Round Problem A
//============================================================================

#include <cstdio>

#define N 4
using namespace std;

void extractRow(int *result) {
	int r, index = 0;

	scanf("%d", &r);

	while (index++ < (r - 1) * N) {
		scanf("%*d");
	}

	for (int i = 0; i < N; i++) {
		int num;
		scanf("%d", &num);

		result[i] = num;
		++index;
	}

	while (index++ <= N * N) {
		scanf("%*d");
	}
}

int compareRows(int *firstRow, int *secondRow, int *answer) {
	int numSame = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (firstRow[i] == secondRow[j]) {
				++numSame;
				*answer = firstRow[i];
				break;
			}
		}
	}

	return numSame;
}

int main() {
	int t, firstRow[N], secondRow[N], ans;

	scanf("%d", &t);

	for (int c = 1; c <= t; c++) {
		extractRow(firstRow);
		extractRow(secondRow);

		printf("Case #%d: ", c);

		switch (compareRows(firstRow, secondRow, &ans)) {
		case 0:
			printf("Volunteer cheated!\n");
			break;
		case 1:
			printf("%d\n", ans);
			break;
		default:
			printf("Bad magician!\n");
		}
	}

	return 0;
}
