#include <stdio.h>
#include <math.h>

unsigned int const MAX_STRING_LENGTH = 101;

int getLeastAmountOfMoves(char** stringList, int numOfStrings) {
	int numberOfMoves = 0;
	int* index = new int[numOfStrings];
	int* charcount = new int[numOfStrings];
	for (int i = 0; i < numOfStrings; i++) { index[i] = 0; charcount[i] = 0; }

	while (index != NULL) {
		unsigned char charToCheck = stringList[0][index[0]];
		for (int i = 1; i < numOfStrings; i++) {
			if (stringList[i][index[i]] != charToCheck) { delete index; delete charcount; return -1; }
		}
		if (charToCheck == '\0') {
			delete index; index = NULL;
			delete charcount; charcount = NULL;
			continue;
		}

		int totalNumber = 0;
		for (int i = 0; i < numOfStrings; i++) { charcount[i] = 0; }

		for (int i = 0; i < numOfStrings; i++) {
			while (stringList[i][index[i]] == charToCheck) {
				index[i]++;
				charcount[i]++;
				totalNumber++;
			}
		}

		int average = (int)roundf((float)totalNumber / (float)numOfStrings);
		for (int i = 0; i < numOfStrings; i++) {
			numberOfMoves += abs(charcount[i] - average);
		}
	}

	delete index; delete charcount;
	return numberOfMoves;
}

int main(void) {
	FILE *outputFile, *inputFile;
	fopen_s(&inputFile, "A-small-attempt0.in", "r");
	fopen_s(&outputFile, "solution.txt", "w");

	int numberOfCases = 0;
	fscanf_s(inputFile, "%i", &numberOfCases);

	for (int i = 0; i < numberOfCases; i++) {
		int numberOfStrings = 0;
		fscanf_s(inputFile, "%i", &numberOfStrings);
		char test[100];
		int testInt = fscanf_s(inputFile, "%c", test);
		char** stringList = new char*[numberOfStrings];
		for (int j = 0; j < numberOfStrings; j++) {
			stringList[j] = new char[MAX_STRING_LENGTH];
			fscanf_s(inputFile, "%s", stringList[j], 101);
		}
		int moveCount = getLeastAmountOfMoves(stringList, numberOfStrings);
		if (moveCount == -1) {
			fprintf_s(outputFile, "Case #%i: Fegla Won\n", i + 1);
		}
		else {
			fprintf_s(outputFile, "Case #%i: %i\n", i + 1, moveCount);
		}

		for (int j = 0; j < numberOfStrings; j++) {	delete stringList[j]; }
		delete stringList;
	}
}