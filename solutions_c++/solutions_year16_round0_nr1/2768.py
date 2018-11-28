#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

void work(ofstream & fout, int caseno, int n) {
	if (n == 0)
		fout << "Case #" << caseno << ": INSOMNIA" << endl;
	else {
		int digits[10] = {};
		int cnt = 0;
		int cur = 0;
		while (cnt < 10) {
			cur += n;
			int tmp = cur;
			while (tmp > 0) {
				int r = tmp % 10;
				tmp /= 10;
				if (digits[r] == 0)
					++cnt;
				++digits[r];
			}
		}
		fout << "Case #" << caseno << ": " << cur << endl;
	}
}

int main() {
	ifstream fin;
	fin.open("input");
	ofstream fout;
	fout.open("output");
	int testcase;
	int n;
	fin >> testcase;
	for (int i = 0; i < testcase; ++i) {
		fin >> n;
		work(fout, i + 1, n);
	}
	return 0;
}