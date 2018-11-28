#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

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