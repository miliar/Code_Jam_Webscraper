#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

void work(ifstream & fin, ofstream & fout, int caseno) {
	int k, c, s;
	fin >> k >> c >> s;

	// seg = k^(c-1)
	long long seg = 1;
	for (int i = 0; i < c - 1; ++i)
		seg *= k;

	fout << "Case #" << caseno << ":";
	for (int i = 0; i < s; ++i) {
		fout << " " << seg * i + 1;
	}
	fout << endl;
}

int main() {
	ifstream fin;
	fin.open("input");
	ofstream fout;
	fout.open("output");
	int testcase;
	fin >> testcase;
	for (int i = 0; i < testcase; ++i) {
		work(fin, fout, i + 1);
	}
	fin.close();
	fout.close();
	return 0;
}