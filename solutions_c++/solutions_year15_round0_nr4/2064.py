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
	printf_s("There are %u test cases.\n", numOfTestCases);

	uint32_t tetronimoSize = 0;
	uint32_t columns = 0, rows = 0;
	for (uint32_t i = 0; i < numOfTestCases; i++) {
		fscanf_s(inputFile, "%lu %lu %lu", &tetronimoSize, &rows, &columns);

		if (rows*columns % tetronimoSize != 0) {
			printf_s("Case #%lu: RICHARD - Gaps\n", i + 1);
			fprintf_s(outputFile, "Case #%lu: RICHARD\n", i + 1);
			continue;
		}

		uint32_t minLength = (uint32_t)floor((float)(tetronimoSize+1) / 2.0f);
		if (minLength > rows || minLength > columns) {
			printf_s("Case #%lu: RICHARD - Min Length %lu\n", i + 1, minLength);
			fprintf_s(outputFile, "Case #%lu: RICHARD\n", i + 1);
			continue;
		}

		if (tetronimoSize > rows && tetronimoSize > columns) {
			printf_s("Case #%lu: RICHARD - Max Length %lu\n", i + 1, tetronimoSize);
			fprintf_s(outputFile, "Case #%lu: RICHARD\n", i + 1);
			continue;
		}

		uint32_t minGrid = rows;
		if (columns > rows) {
			minGrid = columns;
		}
		if (minGrid >= 3 && tetronimoSize >= 7) {
			printf_s("Case #%lu: RICHARD - O Piece %lu\n", i + 1, minLength);
			fprintf_s(outputFile, "Case #%lu: RICHARD\n", i + 1);
			continue;
		}

		if (tetronimoSize >= 4 && rows*columns == tetronimoSize * 2) {
			printf_s("Case #%lu: RICHARD - Piece Block %lu\n", i + 1, minLength);
			fprintf_s(outputFile, "Case #%lu: RICHARD\n", i + 1);
			continue;
		}


		printf_s("Case #%lu: GABRIEL - Default\n", i + 1);
		fprintf_s(outputFile, "Case #%lu: GABRIEL\n", i + 1);

		//printf_s("Case #%lu: r%lu c%lu.\n", i + 1, rows, columns);
	}

	fclose(inputFile);
	fclose(outputFile);
}