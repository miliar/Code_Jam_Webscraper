
#include <stdio.h>

using namespace std;

int shared = 0;

enum testOutcome { UNIQUE, BAD, CHEAT };

testOutcome compareLines(int first[4], int second[4]) {
	int sharedNums = 0;
	
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(first[i] == second[j]) {
				shared = first[i];
				sharedNums++;
			}
		}
	}
	
	if(sharedNums == 0) {
		return CHEAT;
	}
	else if(sharedNums == 1) {
		return UNIQUE;
	}
	else {
		return BAD;
	}
}

void initArray(int (&array)[4][4]) {
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			array[i][j] = 0;
		}
	}
}

int main() {

	int tests, firstGuess, secondGuess;
	int firstSet[4][4], secondSet[4][4];
	FILE* input;
	FILE* output;
	const char* inFile = "A-small-attempt2.in";
	const char* outFile = "A-small-attempt2.out";
	
	input  = fopen(inFile, "r");
	output = fopen(outFile, "w");

	fscanf(input, "%d", &tests);
	for(int i = 0; i < tests; i++) {
		initArray(firstSet);
		initArray(secondSet);
		
		fscanf(input, "%d", &firstGuess);
		for(int row = 0; row < 4; row++) {
			for(int col = 0; col < 4; col++) {
				fscanf(input, "%d", &firstSet[row][col]);
			}
		}
		fscanf(input, "%d", &secondGuess);
		for(int row = 0; row < 4; row++) {
			for(int col = 0; col < 4; col++) {
				fscanf(input, "%d", &secondSet[row][col]);
			}
		}
		
		switch(compareLines(firstSet[firstGuess-1], secondSet[secondGuess-1])) {
			case UNIQUE:
				fprintf(output, "Case #%d: %d\n", i+1, shared);
				shared = 0;
				break;
			case BAD:
				fprintf(output, "Case #%d: Bad magician!\n", i+1);
				break;
			case CHEAT:
				fprintf(output, "Case #%d: Volunteer cheated!\n", i+1);
				break;
		}
		
	}

	fclose(input);
	fclose(output);

}
