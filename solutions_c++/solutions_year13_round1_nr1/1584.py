//============================================================================
// Name        : TicTacToeTomek.cpp
// Author      : Steve
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
	string line;
	int cases = 0;

	ifstream stream("tests/A-small-attempt0.in");

	FILE *file;
	file = fopen("tests/A-small-attempt0.out", "w");

//	if (stream.is_open()) {
//		printf("File is opened\n");
//	} else {
//		printf("Failed to open file\n");
//	}
	//printf("Enter number of cases: ");

	getline(stream, line);

	cases = atoi(line.c_str());

	//printf("Reading in %d cases\n", cases);

	for (int caseNum = 1; caseNum <= cases; caseNum++) {
		getline(stream, line);
		unsigned sp = line.find_first_of(" ");
		if(sp != string::npos) {
			long r = atol(line.substr(0, sp).c_str());
			long t = atol(line.substr(sp+1).c_str());

			//printf("\tRead in: %ld %ld\n", r, t);

			long last = r;
			long total = 0;
			while(true) {
				long next = (last+1)*(last+1)-last*last;
				//printf("\t\tnext: %ld\n", next);
				if (next <= t) {
					t -= next;
					total++;
					last += 2;
				} else {
					break;
				}
			}

			fprintf(file, "Case #%d: %ld\n", caseNum, total);
			printf("Case #%d: %ld\n", caseNum, total);
		}
	}

	stream.close();
	fclose(file);

	return 0;
}
