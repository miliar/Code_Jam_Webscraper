#include <stdio.h>
int numTestCase = 0;
int userRowFirst = 0, userRowSecond = 0;
int cardFirst[16]= {0}, cardSecond[16] = {0};
int i = 0, j = 0, k = 0, count = 0, same = 0;

void handleOneTestInput() {
	scanf("%d", &userRowFirst);
	for (j = 0; j < 4; j++) {
		scanf("%d %d %d %d", &cardFirst[4 * j], &cardFirst[4 * j + 1]
			, &cardFirst[4 * j + 2], &cardFirst[4 * j + 3]);
	}
	scanf("%d", &userRowSecond);
	for (j = 0; j < 4; j++) {
		scanf("%d %d %d %d", &cardSecond[4 * j], &cardSecond[4 * j + 1]
			, &cardSecond[4 * j + 2], &cardSecond[4 * j + 3]);
	}
}

void printCheckOutput() {
	printf("numTestCase: %d userRowFirst: %d userRowSecond:%d\n", 
		numTestCase, userRowFirst, userRowSecond);
	printf("CardFirst\n");
	for (j = 0; j < 4; j++) {
		printf("%d %d %d %d\n", cardFirst[4*j], cardFirst[4*j+1]
			, cardFirst[4*j+2], cardFirst[4*j+3]);
	}
	printf("CardSecond\n");
	for (j = 0; j < 4; j++) {
		printf("%d %d %d %d\n", cardSecond[4*j], cardSecond[4*j+1]
			, cardSecond[4*j+2], cardSecond[4*j+3]);
	}
}

void solveTestCase() {
	count = 0, same = 0;
	for (j = 0; j < 4; j++) {
		for (k = 0; k < 4; k++) {
			if (cardFirst[4*(userRowFirst-1) + j] == cardSecond[4*(userRowSecond-1) + k]) {
				same = cardFirst[4*(userRowFirst-1) + j], count++;
				if (count == 2) return;
				// printf("debug count:%d, userRowFirst: %d, userRowSecond: %d, j: %d, k: %d\n"
				//	, count, userRowFirst, userRowSecond, j, k);
			}
		}
	}
}

void printResult() {
	printf("Case #%d: ", i+1);
	if (count == 1) {
		printf("%d\n", same);
	} else if (count > 1) {
		printf("Bad magician!\n");
	} else {
		printf("Volunteer cheated!\n");
	}
}

int main() {
	scanf("%d", &numTestCase);
	for(i = 0; i < numTestCase; i++) {
		// printf("debug TestCase %d\n", i);
		handleOneTestInput();
		solveTestCase();
		printResult();
	}
	return 0;
}