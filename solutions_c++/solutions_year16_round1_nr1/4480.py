#include <bits/stdc++.h>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("a.out");

string solve() {
	string s, res = "";
	fin >> s;
	for (char c : s) {
		if (c >= res[0]) res = c + res;
		else res = res + c;
	}
	return res;
}

int main() {
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) fout << "Case #" << i+1 << ": " << solve() << '\n';
}
