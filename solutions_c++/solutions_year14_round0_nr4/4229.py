#include <stdio.h>
#include <string.h>

typedef struct {
	double value;
	bool who;
} Block;

int numTestCases = 0;
int i = 0, j = 0, numBlocks = 0;
int humbleResult = 0, deceitfulResult = 0;
Block block[2000];

void printBlocks() {
	for (j = 0; j < numBlocks * 2; j++) {
		if (block[j].who) printf("\t");
		printf("%lf\n", block[j].value);
	}
//	printf("\n");
	for (j = 0; j < numBlocks * 2; j++)
		printf("%d ", block[j].who);
	printf("\n");
}

int quickSort(Block* blockArray, int lowIndex, int highIndex) {
	int pivotPoint = 0, indexI = 0, indexJ = 0;
	double pivotItem = 0, tempValue = 0;
	bool tempBool = false;
	if (highIndex <= lowIndex) {return 1;}

	pivotItem = blockArray[lowIndex].value;
	indexJ = lowIndex;
	for (indexI = lowIndex + 1; indexI <= highIndex; indexI++) {
		if (blockArray[indexI].value >= pivotItem) {continue;}
		indexJ++;

		tempValue = blockArray[indexI].value;
		tempBool = blockArray[indexI].who;
		blockArray[indexI].value = blockArray[indexJ].value;
		blockArray[indexI].who = blockArray[indexJ].who;
		blockArray[indexJ].value = tempValue;
		blockArray[indexJ].who = tempBool;
	}
	pivotPoint = indexJ;
	tempValue = blockArray[lowIndex].value;
	tempBool = blockArray[lowIndex].who;
	blockArray[lowIndex].value = blockArray[pivotPoint].value;
	blockArray[lowIndex].who = blockArray[pivotPoint].who;
	blockArray[pivotPoint].value = tempValue;
	blockArray[pivotPoint].who = tempBool;

	quickSort(blockArray, lowIndex, pivotPoint - 1);
	quickSort(blockArray, pivotPoint + 1, highIndex);
	return 1;
}

void handleTestCase() {
	// Get humble one
	int tmpCount = 0, sumN = 0, sumK = 0;

	for (j = 0; j < numBlocks * 2; j++) {
		if (block[j].who == true) {
			sumK++;
			if (sumK <= sumN) {
				tmpCount++;
			} else {
				sumK--;
			}
		} else {
			sumN++;
		}
	}
	humbleResult = numBlocks - tmpCount;

	// Get deceitful one
	tmpCount = 0, sumN = 0, sumK = 0;
	deceitfulResult = numBlocks;
	for (j = numBlocks * 2 - 1; j >= 0 && block[j].who == true; j--)
		tmpCount++;
	for (; j >= 0 && sumN + tmpCount < numBlocks; j--) {
		if (block[j].who == true) {
			sumK++;
			if (sumK > sumN) {
//				deceitfulResult--;
				sumK--, tmpCount++;
			}
		} else {
			sumN++;
		}
	}
	deceitfulResult -= tmpCount;
}

int main() {
	for (int i = 0; i < 2000; i++) {
		block[i].value = 2, block[i].who = false;
	}

	scanf("%d", &numTestCases);
	for (i = 0; i < numTestCases; i++) {
		scanf("%d", &numBlocks);
		for (j = 0; j < numBlocks; j++) {
			scanf("%lf", &block[j].value);
			block[j].who = false;
		}
		for (j = 0; j < numBlocks; j++) {
			scanf("%lf", &block[numBlocks + j].value);
			block[numBlocks + j].who = true;
		}
		quickSort(block, 0, numBlocks * 2 - 1);
//d		printBlocks();	// debug
		handleTestCase();

		printf("Case #%d: %d %d\n", i+1, deceitfulResult, humbleResult);
//d		printf("\n");	// debug
		for (j = 0; j < numBlocks * 2; j++)
			block[j].value = 2, block[j].who = false;
	}
}