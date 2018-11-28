#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

void work(ifstream & fin, ofstream & fout, int caseno) {
	string s;
	fin >> s;
	int cnt = 1;
	int start = s[0] == '-' ? 0: 1;
	for (int i = 1; i < s.size(); ++i) {
		if (s[i] != s[i - 1])
			++cnt;
	}

	// dp
	// 0: - 
	// 1: +
	// f[i][j][k]
	// i: length
	// j: start with '-' or '+'
	// k: convert all to '-' or '+'
	int f[cnt + 1][2][2];
	f[1][0][0] = 0;
	f[1][0][1] = 1;
	f[1][1][0] = 1;
	f[1][1][1] = 0;
	for (int i = 2; i <= cnt; ++i) {
		for (int j = 0; j < 2; ++j) {
			for (int k = 0; k < 2; ++k) {
				int r = (i % 2 + j + 1) % 2;
				if (r == k)
					f[i][j][k] = f[i - 1][j][k];
				else
					f[i][j][k] = f[i - 1][j][1 - k] + 1;
			}
		}
	}

	int ans = f[cnt][start][1];
	fout << "Case #" << caseno << ": " << ans << endl;
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