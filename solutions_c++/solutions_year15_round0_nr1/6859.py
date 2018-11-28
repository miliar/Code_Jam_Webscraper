#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#define MAXN 1001

using namespace std;

int t;
int s_m;
int s[MAXN];
string k;

int solve() {
	int ret = 0;
	int clap = 0;
	for (int j = 0; j <= s_m; j++) {
		if (clap <= j && s[j] > 0) {
			cout << j << " " << s[j] << endl;
			int ret_diff = j - clap;
			cout << ret_diff << endl;
			ret += ret_diff;
			clap += ret_diff;
		}
		clap += s[j];
	}
	return ret;
}

int main() {
	ifstream fin ("A-large.in");
	ofstream fout ("so.out");
	fin >> t;
	for (int i = 1; i <= t; i++) {
		fin >> s_m >> k;
		for (int j = 0; j < k.size(); j++) {
			s[j] = k[j] - '0';
		}
		fout << "Case #" << i << ": " << solve() << endl;
	}
}
