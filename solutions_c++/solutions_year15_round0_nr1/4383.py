#include <cstdio>
#include <cstdint>

int main(int argc, char** argv) {
	printf_s("Google Code Jam 2015 - Standing Ovation.\n");

	if (argc != 3) {
		printf_s("Please enter the input and output filenames.\n");
		return 0;
	}

	FILE* inputFile = NULL;
	fopen_s(&inputFile, argv[1], "r");
	if (inputFile == NULL) {
		printf_s("Problem loading input file.\n");
		return 0;
	}

	FILE* outputFile = NULL;
	fopen_s(&outputFile, argv[2], "w");
	if (outputFile == NULL) {
		printf_s("Problem loading output file.\n");
		return 0;
	}


	uint32_t numOfTestCases = 0;
	fscanf_s(inputFile, "%u", &numOfTestCases);
	printf_s("There are %u testcases.\n", numOfTestCases);

	uint32_t shynessLevels[1001] = { 0 };
	uint32_t maxShynessLevel = 0;
	char shynessString[1002] = "";

	for (uint32_t i = 0; i < numOfTestCases; i++) {
		fscanf_s(inputFile, "%u %s", &maxShynessLevel, shynessString, 1001);

		uint32_t standingGuests = 0;
		uint32_t extraGuests = 0;

		for (uint32_t j = 0; j <= maxShynessLevel; j++) {
			if (standingGuests < j) {
				extraGuests++;
				standingGuests++;
			}

			shynessLevels[j] = shynessString[j] - '0';
			standingGuests += shynessLevels[j];
		}

		fprintf_s(outputFile, "Case #%u: %u\n", i + 1, extraGuests);
		printf_s("Case #%u: %u\n", i + 1, extraGuests);
	}
}