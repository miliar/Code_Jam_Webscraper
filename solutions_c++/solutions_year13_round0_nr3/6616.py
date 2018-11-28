// CodeJam2013.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include "StringTokenizer.hpp"

using namespace std;

bool isPalindrome(int number) {
	stringstream ss;
	ss << number;
	string str = ss.str();
	for (int charIndex = 0; charIndex < str.length() / 2; ++charIndex) {
		if (str[charIndex] != str[str.length() - 1 - charIndex]) {
			return false;
		}
	}

	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inputFS;
	inputFS.open("input.txt");

	ofstream outputFS;
	outputFS.open("output.txt");

	if (inputFS.is_open()) {
		string line;
		getline(inputFS, line);
		int numTestCases = atoi(line.c_str());
		for (int testCase = 0; testCase < numTestCases; ++testCase) {
			getline(inputFS, line);
			vector<string> tokens;
			StringTokenizer::tokenize(line, tokens, " ");
			int a = atoi(tokens[0].c_str());
			int b = atoi(tokens[1].c_str());
			int fairAndSquare = 0;
			int root = int(ceil(powf((float)a, 0.5f)));
			while (root * root <= b) {
				int square = root * root;
				if ((isPalindrome(root)) && (isPalindrome(square))) {
					++fairAndSquare;
				}
				++root;
			}

			outputFS << "Case #" << (testCase + 1) << ": " << fairAndSquare << endl;
		}
		inputFS.close();
		outputFS.close();
	}

	return 0;
}
