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
#include <string.h>
#include <math.h>
#include <sstream>

using namespace std;

string itoa(int i)
{
    std::string s;
    std::stringstream out;
    out << i;
    s = out.str();
    return s;
}

bool isPalindrome(string s) {
	for (unsigned int i = 0; i < s.length()/2+1; i++) {
		if (s[i] != s[s.length()-i-1]) {
			return false;
		}
	}

	return true;
}

int main(int argc, char *argv[]) {
	string line;
	int cases = 0;

	ifstream stream("tests/C-small-attempt0.in");

//	if (stream.is_open()) {
//		printf("File is opened\n");
//	} else {
//		printf("Failed to open file\n");
//	}
	//printf("Enter number of cases: ");

	getline(stream, line);

	cases = atoi(line.c_str());

	for (int caseNum = 1; caseNum <= cases; caseNum++) {
		string result = "no result";

		getline(stream, line);

		char input[100];
		strcpy(input, line.c_str());
		char* tok = strtok(input, " ");

		int a = atoi(tok);
		tok = strtok(NULL, " ");
		int b = atoi(tok);

		int count = 0;

		for (int i = a; i <= b; i++) {
			double root = sqrt((double) i);
			if (floor(root) != ceil(root)) {
				continue;
			}
			string num = itoa(i);
			if (isPalindrome(num)) {
				num = itoa((int) root);
				if (isPalindrome(num)) {
					//printf("\tFound: %s (%f)\n", num.c_str(), root);
					count++;
				}
			}
		}

//		printf("Case #%d: %s\n", caseNum, result.c_str());
		printf("Case #%d: %d\n", caseNum, count);
	}

	stream.close();

	return 0;
}
