#include<fstream>
#include<iostream>
#include<string>
using std::cin;
using std::cout;
using std::endl;

int main() {
	int T, test;

	std::ifstream fin("B-large.in");
	if (!fin) { cout << "Error on open fin" << endl; return 1; }
	std::ofstream fout("B-large.out");
	if (!fout) { cout << "Error on open fout" << endl; return 1; }

	fin >> T;
	for (test = 0; test < T; ++test) {
		std::string S;
		int n = 0;
		fin >> S;

		S += '+';

		for (int i = 1; i < S.size(); ++i) {
			if (S[i] != S[i - 1]) { ++n; }
		}

		fout << "Case #" << test + 1 << ": " << n << endl;
	}
}