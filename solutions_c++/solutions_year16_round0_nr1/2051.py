#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <fstream>

using namespace std;

int T;
long long N;

bool label[10];

int cnt;

void reset() {
	for (int i = 0; i <= 9; ++i)
		label[i] = false;
	cnt = 0;
}

void proc(long long N) {
	long long tmp = 0;
	while (N > 0) {
		tmp = N % 10;
		if (!label[tmp]) {
			label[tmp] = true;
			++cnt;
		}
		N /= 10;
	}
}

int main() {
	ifstream infile;
	infile.open("input.txt");
	ofstream outfile;
	outfile.open("output.txt");


	infile >> T;

	for (int p = 1; p <= T; ++p) {
		reset();

		infile >> N;
		outfile << "Case #" << p << ": ";
		for (int i = 1; i <= 1e7; ++i) {
			if (N == 0) break;
			proc(N * i);
			if (cnt == 10) {
				outfile << N * i << endl;
				break;
			}
		}

		if (cnt < 10) {
			outfile << "INSOMNIA" << endl;
		}
	}

	infile.close();
	outfile.close();
	return 0;
}