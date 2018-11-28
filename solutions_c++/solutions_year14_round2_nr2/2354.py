#include <Windows.h>
#include <stdio.h>
#include <math.h>

int main(void) {
	FILE *outputFile, *inputFile;
	fopen_s(&inputFile, "B-small-attempt2.in", "r");
	fopen_s(&outputFile, "solution.txt", "w");

	UINT64 numberOfCases = 0;
	fscanf_s(inputFile, "%llu", &numberOfCases);

	for (int i = 0; i < numberOfCases; i++) {
		UINT64 tempA, tempB;
		UINT64 smallLimit, largeLimit, ticketNum;
		fscanf_s(inputFile, "%llu %llu %llu", &tempA, &tempB, &ticketNum);
		if (tempA > tempB) {
			smallLimit = tempB; largeLimit = tempA;
		}
		else {
			smallLimit = tempA; largeLimit = tempB;
		}

		UINT64 numberOfPossibilities = smallLimit * largeLimit;

		if (smallLimit <= ticketNum) {
			fprintf_s(outputFile, "Case #%i: %i\n", i + 1, numberOfPossibilities);
			continue;
		}

		UINT64 potentialPossibilities = (smallLimit - ticketNum) * (largeLimit - ticketNum);
		numberOfPossibilities -= potentialPossibilities;

		//Find remain possibilities
		for (int i = ticketNum; i < smallLimit; i++) {
			for (int j = ticketNum; j < largeLimit; j++) {
				if ((i&j) < ticketNum){
					numberOfPossibilities++;
				}
			}
		}


		fprintf_s(outputFile, "Case #%i: %i\n", i + 1, numberOfPossibilities);
	}
}