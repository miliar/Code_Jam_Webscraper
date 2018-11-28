#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	int testCase;
	string input;
	ifstream fin;
	ofstream fout;

	fin.open("B-large.in");
	fout.open("output.txt");

	fin >> testCase;
	for (int test = 0; test < testCase; test++) {
		fin >> input;

		int rotateCount = 0;
		int length = input.length();
		bool beforeState = true;
		if (input[0] == '-') beforeState = false;

		for (int loop = 1; loop < length; loop++) {
			if (input[loop] == '-' && beforeState == true) {
				beforeState = false;
				rotateCount++;
			}
			else if (input[loop] == '+' && beforeState == false) {
				beforeState = true;
				rotateCount++;
			}			
		}
		if (input[length - 1] == '-') rotateCount++;
		fout << "Case #" << test + 1 << ": " << rotateCount << endl;
		cout << "Case #" << test + 1 << ": " << rotateCount << endl;
	}

	fin.close();
	fout.close();
	return 0;
}

/*
int main() {
	int testCase;
	int K, C, S;
	ifstream fin;
	ofstream fout;

	fin.open("D-small-attempt1.in");
	fout.open("output.txt");

	fin >> testCase;
	for (int test = 0; test < testCase; test++) {
		fin >> K >> C >> S;
		
		fout << "Case #" << test + 1 << ": ";
		cout << "Case #" << test + 1 << ": ";
		for (int loop = 1; loop <= K; loop++) {
			fout << loop << " ";
			cout << loop << " ";
		}
		fout << endl;
		cout << endl;
		
	}

	fin.close();
	fout.close();
	return 0;
}
*/