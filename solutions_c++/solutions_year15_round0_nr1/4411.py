#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("ovation.in");
ofstream fout("ovation.out");

void solve() {
	int sz, sum = 0;
	fin >> sz;
	vector<int> v (sz + 1);
	for (int i = 0; i <= sz; i++) {
		char c;
		fin >> c;
		v[i] = c - '0';
		sum += v[i];
	}
	int orig0 = v[0];
	for (int i = 0; i < 1003; i++) {
		v[0] = orig0 + i;
		int num = v[0];
		for (int j = 1; j <= sz; j++)
			if (num >= j) num += v[j];
		if (num == sum + i) {
			fout << i << '\n';
			return;
		}
	}
}

int main() {
	int n;
	fin >> n;
	for (int i = 0; i < n; i++) {
		fout << "Case #" << i+1 << ": ";
		solve();
	}
}
