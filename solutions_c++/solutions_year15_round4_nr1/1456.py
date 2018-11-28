#include <cstdio>
#include <cstdint>
#include <cmath>

char inputGrid[100][100];

int32_t doesUpChange(uint32_t r, uint32_t c, uint32_t rows, uint32_t columns) {
	for (int32_t i = r-1; i >= 0; i--) {
		if (inputGrid[i][c] != '.') {
			return 0;
		}
	}

	for (int32_t i = r + 1; i < (int32_t)rows; i++) {
		if (inputGrid[i][c] != '.') {
			return 1;
		}
	}

	for (int32_t i = c - 1; i >= 0; i--) {
		if (inputGrid[r][i] != '.') {
			return 1;
		}
	}

	for (int32_t i = c + 1; i < (int32_t)columns; i++) {
		if (inputGrid[r][i] != '.') {
			return 1;
		}
	}

	return -1;
}

int32_t doesDownChange(uint32_t r, uint32_t c, uint32_t rows, uint32_t columns) {
	for (int32_t i = r + 1; i < (int32_t)rows; i++) {
		if (inputGrid[i][c] != '.') {
			return 0;
		}
	}

	for (int32_t i = r - 1; i >= 0; i--) {
		if (inputGrid[i][c] != '.') {
			return 1;
		}
	}

	for (int32_t i = c - 1; i >= 0; i--) {
		if (inputGrid[r][i] != '.') {
			return 1;
		}
	}

	for (int32_t i = c + 1; i < (int32_t)columns; i++) {
		if (inputGrid[r][i] != '.') {
			return 1;
		}
	}

	return -1;
}

int32_t doesRightChange(uint32_t r, uint32_t c, uint32_t rows, uint32_t columns) {
	for (int32_t i = c + 1; i < (int32_t)columns; i++) {
		if (inputGrid[r][i] != '.') {
			return 0;
		}
	}

	for (int32_t i = r + 1; i < (int32_t)rows; i++) {
		if (inputGrid[i][c] != '.') {
			return 1;
		}
	}

	for (int32_t i = r - 1; i >= 0; i--) {
		if (inputGrid[i][c] != '.') {
			return 1;
		}
	}

	for (int32_t i = c - 1; i >= 0; i--) {
		if (inputGrid[r][i] != '.') {
			return 1;
		}
	}

	return -1;
}

int32_t doesLeftChange(uint32_t r, uint32_t c, uint32_t rows, uint32_t columns) {
	for (int32_t i = c - 1; i >= 0; i--) {
		if (inputGrid[r][i] != '.') {
			return 0;
		}
	}

	for (int32_t i = c + 1; i < (int32_t)columns; i++) {
		if (inputGrid[r][i] != '.') {
			return 1;
		}
	}

	for (int32_t i = r + 1; i < (int32_t)rows; i++) {
		if (inputGrid[i][c] != '.') {
			return 1;
		}
	}

	for (int32_t i = r - 1; i >= 0; i--) {
		if (inputGrid[i][c] != '.') {
			return 1;
		}
	}
	
	return -1;
}
int main(int argc, char** argv) {
	printf_s("Google Code Jam 2015\nPegman Challenge\n");

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

	uint64_t numOfTestCases = 0;
	fscanf_s(inputFile, "%llu", &numOfTestCases);
	printf_s("There are %llu number of test cases.\n", numOfTestCases);


	//Code here
	for (uint64_t i = 0; i < numOfTestCases; i++) {
		uint32_t rows, columns;
		fscanf_s(inputFile, "%lu %lu", &rows, &columns);
		//printf("There are %lu rows and %u columns.\n", rows, columns);
		for (uint32_t r = 0; r < rows; r++) {
			for (uint32_t c = 0; c < columns; c++) {
				char tempC = (char)getc(inputFile);
				if (tempC == '\n') {
					tempC = (char)getc(inputFile);
				}
				inputGrid[r][c] = tempC;
				//printf_s("%c", tempC);
			}
		}

		uint32_t numOfSwaps = 0;

		for (uint32_t r = 0; r < rows; r++) {
			for (uint32_t c = 0; c < columns && numOfSwaps <= 5000000; c++) {
				if (inputGrid[r][c] == '^') {
					int32_t result = doesUpChange(r, c, rows, columns);
					if (result == -1) {
						numOfSwaps = 5000000;
					}
					else {
						numOfSwaps += result;
					}
				}

				if (inputGrid[r][c] == 'v') {
					int32_t result = doesDownChange(r, c, rows, columns);
					if (result == -1) {
						numOfSwaps = 5000000;
					}
					else {
						numOfSwaps += result;
					}
				}

				if (inputGrid[r][c] == '>') {
					int32_t result = doesRightChange(r, c, rows, columns);
					if (result == -1) {
						numOfSwaps = 5000000;
					}
					else {
						numOfSwaps += result;
					}
				}

				if (inputGrid[r][c] == '<') {
					int32_t result = doesLeftChange(r, c, rows, columns);
					if (result == -1) {
						numOfSwaps = 5000000;
					}
					else {
						numOfSwaps += result;
					}
				}

			}
		}

		if (numOfSwaps >= 5000000) {
			printf_s("Case #%llu: IMPOSSIBLE\n", i + 1);
			fprintf_s(outputFile, "Case #%llu: IMPOSSIBLE\n", i + 1);
		}
		else {
			printf_s("Case #%llu: %lu\n", i + 1, numOfSwaps);
			fprintf_s(outputFile, "Case #%llu: %lu\n", i + 1, numOfSwaps);
		}
	}



	fclose(inputFile);
	fclose(outputFile);
}