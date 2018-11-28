#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <fstream>

using namespace std;


ifstream infile;
ofstream outfile;

int T;
long long K, C, S;


int main() {
	infile.open("input.txt");
	outfile.open("output.txt");

	infile >> T;

	for (int p = 1; p <= T; ++p) {
		//		reset();

		outfile << "Case #" << p << ":";

		infile >> K >> C >> S;

		if (C * S < K) {
			outfile << " IMPOSSIBLE" << endl;
			continue;
		}

		long long iter = 0;
		long long tmp;
		while (iter < K) {
			tmp = 0;
			for (int i = 1; i <= C; ++i) {
				++iter;
				tmp = tmp * K + (K < iter ? K : iter) - 1;
			}
			outfile << " " << tmp + 1;
		}

		outfile << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}