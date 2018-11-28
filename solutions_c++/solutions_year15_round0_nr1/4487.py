// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

typedef struct sTestCase {
	int MaxShyness;
	int Audience[1024];
} sTestCase;

int ProcessTestCase(sTestCase Case) {
	int NeededFriends = 0;
	int TotalPeopleStanding = 0;
	for (int Shyness=0; Shyness<=Case.MaxShyness; ++Shyness) {
		if (TotalPeopleStanding < Shyness) {
			NeededFriends += Shyness - TotalPeopleStanding;
			TotalPeopleStanding += (Shyness - TotalPeopleStanding);
		}
		TotalPeopleStanding += Case.Audience[Shyness];
	}
	return NeededFriends;
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
	char ShynessBuf[4096];
	for (int i=0; i<TestCases; ++i) {
		sTestCase Case;
		memset((void *)&Case, 0, sizeof(sTestCase));

		// Read line
		fgets(LineBuf, 4096, InputFile);

		// Read case
		sscanf(LineBuf, "%i %s\n", &Case.MaxShyness, ShynessBuf);
	
		// Parse shyness
		for (int j=0; j<=Case.MaxShyness; ++j) {
			Case.Audience[j] = ShynessBuf[j] - '0';
		}

		// Call process test case
		int NeededFriends = ProcessTestCase(Case);

		// Print
		printf("Case #%i: %i\n", i, NeededFriends);
		fprintf(OutputFile, "Case #%i: %i\n", i+1, NeededFriends);
	}

	// Close file
	fclose(InputFile);
	fclose(OutputFile);
	_getch();

	return 0;
}

