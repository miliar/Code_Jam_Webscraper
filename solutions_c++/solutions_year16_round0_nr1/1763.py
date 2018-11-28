#include<fstream>
#include<iostream>
using std::cin;
using std::cout;
using std::endl;

int main() {
	int T, test;
	const int p = 10;

	std::ifstream fin("A-large.in");
	if (!fin) { cout << "Error on open fin" << endl; return 1; }
	std::ofstream fout("A-large.out");
	if (!fout) { cout << "Error on open fout" << endl; return 1; }

	fin >> T;
	for (test = 0; test < T; ++test) {
		long N, S = 0;
		int dmask = 0;
		fin >> N;

		if (N == 0) {
			fout << "Case #" << test + 1 << ": INSOMNIA" << endl;
			continue;
		}

		while (dmask < 1023) {
			S += N;
			int d = S;
			while (d) {
				dmask |= 1 << (d % 10);
				d /= 10;
			}
		}
		fout << "Case #" << test + 1 << ": " << S << endl;
	}
}