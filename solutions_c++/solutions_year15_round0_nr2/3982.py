#include <cstdio>
#include <cstdint>
#include <cmath>

const uint32_t MAX_NUM_OF_PANCAKES = 1000;

int main(int argc, char** argv) {
	printf_s("Google Code Jam 2015\n");

	if (argc != 3) {
		printf_s("Please enter the name of the input and output files only.\n");
		return 0;
	}

	FILE *inputFile = NULL, *outputFile = NULL;
	fopen_s(&inputFile, argv[1], "r");
	fopen_s(&outputFile, argv[2], "w");

	if (inputFile == NULL || outputFile == NULL) {
		printf_s("Unable to open the file.\n");
		return 0;
	}

	uint32_t numOfTestCases = 0;
	fscanf_s(inputFile, "%u", &numOfTestCases);
	printf_s("There are %u number of test cases.\n", numOfTestCases);
	
	uint32_t pancakeCounts[MAX_NUM_OF_PANCAKES] = { 0 };
	uint32_t numOfNonEmptyPlates = 0;
	for (uint32_t i = 0; i < numOfTestCases; i++) {
		
		for (uint32_t j = 0; j < MAX_NUM_OF_PANCAKES; j++) {
			pancakeCounts[j] = 0;
		}
		
		fscanf_s(inputFile, "%u", &numOfNonEmptyPlates);
		uint32_t pancakeCount = 0;
		for (uint32_t j = 0; j < numOfNonEmptyPlates; j++) {
			fscanf_s(inputFile, "%u", &pancakeCount);
			pancakeCounts[pancakeCount-1]++;
		}

		uint32_t minTime = MAX_NUM_OF_PANCAKES + 1;
		uint32_t minLimit = 0;
		for (uint32_t j = 0; j < MAX_NUM_OF_PANCAKES; j++) {
			uint32_t specialTime = 0;
			for (uint32_t k = j + 1; k < MAX_NUM_OF_PANCAKES; k++) {
				uint32_t numOfMoves = (uint32_t)(ceilf((float)(k + 1) / (float)(j + 1))) - 1;
				specialTime += numOfMoves * pancakeCounts[k];
			}
			uint32_t totalTime = specialTime + j + 1;

			//printf_s("Time %u, at %u\n", totalTime, j + 1);
			if (totalTime < minTime) {
				minTime = totalTime;
				minLimit = j+1;
			}
		}


		printf_s("Case #%u: %u, at %u\n", i + 1, minTime, minLimit);
		fprintf_s(outputFile, "Case #%u: %u\n", i + 1, minTime);
	}
	
	fclose(inputFile);
	fclose(outputFile);
}