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

	fin.open("A-large.in");
	fout.open("output.txt");

	fin >> testCase;
	for (int test = 0; test < testCase; test++) {
		fin >> input;
		string output = "";
		for (int loop = 0; loop < input.length(); loop++) {
			char testChar = input[loop];
			if (output.length() == 0) { output += testChar; }
			else {
				if (output[0] <= testChar) {
					output = testChar + output;
				}
				else {
					output = output + testChar;
				}
			}
		}

		
		fout << "Case #" << test + 1 << ": " << output << endl;
		cout << "Case #" << test + 1 << ": " << output << endl;
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