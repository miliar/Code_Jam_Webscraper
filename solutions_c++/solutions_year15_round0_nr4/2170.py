// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

typedef struct sTestCase {
	int X;
	int R;
	int C;
} sTestCase;

int imin(int a, int b) {
	return a > b? b : a;
}

std::string ProcessTestCase(sTestCase Case) {
	std::string Out = std::string("RICHARD");
	if (Case.X < 7)
		if (((Case.R*Case.C) % Case.X) == 0) {
			if (Case.X < 3) {
				Out = std::string("GABRIEL");
			} else {
				if (imin(Case.R, Case.C) >= imin(Case.X-1, 4))
					Out = std::string("GABRIEL");
			}
		}
	return Out;
}

int main(int argc, char* argv[]) {
	if (argc == 1) {
		return 1;
	}

	// Open file
	FILE *InputFile = NULL;
	FILE *OutputFile = NULL;
	InputFile = fopen(argv[1], "r");
	OutputFile = fopen("out.txt", "w");

	// Read cases
	int TestCases = 0;
	printf("Processing %s ... \n", argv[1]);
	int Read = fscanf(InputFile, "%i\n", &TestCases);
	if (Read != 1) {
		return 1;
	}

	// Cycle on cases
	char LineBuf[4096];
	int StringLength = 0, Repetitions = 0;
	for (int i=0; i<TestCases; ++i) {
		sTestCase Case;
		memset((void *)&Case, 0, sizeof(sTestCase));

		// Read settings
		fscanf(InputFile, "%i %i %i\n", &Case.X, &Case.R, &Case.C);

		// Call process test case
		std::string Player = ProcessTestCase(Case);

		// Print
		printf("Case #%i: %s\n", i+1, Player.c_str());
		fprintf(OutputFile, "Case #%i: %s\n", i+1, Player.c_str());
	}

	// Close file
	fclose(InputFile);
	fclose(OutputFile);
	_getch();

	return 0;
}

