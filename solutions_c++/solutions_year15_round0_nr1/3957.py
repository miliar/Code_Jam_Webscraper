#include <iostream>
#include <cstdio>
#include <string>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	for (int q = 0; q < t; ++q) {
		int n;
		string s;
		fin >> n >> s;
		int cur = s[0] - '0';
		int ans = 0;
		for (int i = 1; i <= n; ++i) {
			int val = s[i] - '0';
			if (cur < i && val) {
				int add = i - cur;
				cur += add;
				ans += add;
			}
			cur += val;
		}
		fout << "Case #" << q + 1 << ": " << ans << "\n";
	}
	return 0;
}