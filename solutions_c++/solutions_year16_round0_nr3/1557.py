#include<fstream>
#include<iostream>
#include<string>
using std::cin;
using std::cout;
using std::endl;

int main() {
	int T, test;
	const std::string divisors = " 3 4 5 6 7 8 9 10 11";

	std::ifstream fin("C-large.in");
	if (!fin) { cout << "Error on open fin" << endl; return 1; }
	std::ofstream fout("C-large.out");
	if (!fout) { cout << "Error on open fout" << endl; return 1; }

	fin >> T;
	for (test = 0; test < T; ++test) {
		int N, J;
		fin >> N >> J;

		fout << "Case #" << test + 1 << ":" << endl;
		for (int i = 0; i < J; ++i) {
			std::string S = "11";
			int a = i;
			for (int k = 0; k < N / 2 - 2; ++k) {
				S += (a % 2) ? "11" : "00";
				a /= 2;
			}
			while (S.size() < N) {
				S += "11";
			}
			fout << S << divisors << endl;
		}
	}
}