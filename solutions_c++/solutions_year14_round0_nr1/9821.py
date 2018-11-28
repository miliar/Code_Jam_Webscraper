#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define COLSIZE 4
#define ROWSIZE 4

int main() {
	FILE *inputFilePtr;
	FILE *outputFilePtr;
	int colSize, totalNum, selectedRowNum, i, j, k, m, match, card;
	int temp[COLSIZE], cards[COLSIZE];

	inputFilePtr = fopen("A-small-attempt0.in", "r");
	outputFilePtr = fopen("output.out", "a");

	fscanf(inputFilePtr, "%d", &totalNum);

	for (i = 1; i <= totalNum; ++i) {

		fscanf(inputFilePtr, "%d", &selectedRowNum);

		for (j = 1; j <= ROWSIZE; ++j) {
			fscanf(inputFilePtr, "%d %d %d %d", &temp[0], &temp[1], &temp[2], &temp[3]);

			if (j == selectedRowNum) {
				memcpy(&cards, &temp, sizeof(temp));
			}
		}

		match = 0;

		fscanf(inputFilePtr, "%d", &selectedRowNum);

		for (j = 1; j <= ROWSIZE; ++j) {
			fscanf(inputFilePtr, "%d %d %d %d", &temp[0], &temp[1], &temp[2], &temp[3]);
			if (j == selectedRowNum) {

				for (m = 0; m < COLSIZE; ++m) {
					for (k = 0; k < COLSIZE; ++k) {
						if (cards[k] == temp[m]) {
							++match;
							card = cards[k];
						}
					}
				}
			}
		}

		if (match == 0) {
			fprintf(outputFilePtr, "Case #%d: Volunteer cheated!\n", i);
		} else if (match == 1) {
			fprintf(outputFilePtr, "Case #%d: %d\n", i, card);
		} else {
			fprintf(outputFilePtr, "Case #%d: Bad magician!\n", i);
		}

	}

	fclose(inputFilePtr);
	fclose(outputFilePtr);

	return 0;
}

