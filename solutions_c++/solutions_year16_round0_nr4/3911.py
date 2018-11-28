#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ifstream fin("d.in");
ofstream fout("d.out");

void solve() {
	ll k, c, s;
	fin >> k >> c >> s;
	for (int i = 0; i < k; i++) fout << ' ' << i+1;
}

int main() {
	int t;
	fin >> t;
	for (int i = 1; i <= t; i++) {
		fout << "Case #" + to_string(i) + ":";
		solve();
		fout << "\n";
	}
}
