#include<fstream>
#include<iostream>
#include<string>
using std::cin;
using std::cout;
using std::endl;

int main() {
	int T, test;

	std::ifstream fin("D-small-attempt2.in");
	if (!fin) { cout << "Error on open fin" << endl; return 1; }
	std::ofstream fout("D-small-attempt2.out");
	if (!fout) { cout << "Error on open fout" << endl; return 1; }

	fin >> T;
	for (test = 0; test < T; ++test) {
		int K, C, S;
		fin >> K >> C >> S;

		fout << "Case #" << test + 1 << ":";
		for (int i = 0; i < S; ++i) {
//			long long pos = (i+1) * pow(K, C-1);
			fout << " " << i+1;
		}
		fout << endl;
	}
}