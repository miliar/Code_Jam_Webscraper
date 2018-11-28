#include <iostream>
#include <fstream>
#include <cassert>
#include <algorithm>
#include <functional>
#include <vector>
#include <stack>
#include <queue>
#include <string>

using namespace std;


bool solve(int x, int r, int c) {
	if (r > c) swap(r, c);
	if (x >= 7) return true;
	if (r * c % x != 0) return true;
	if (x > c) return true;
	if ((x + 1) / 2 > r) return true;
	if (x == 2 * r && r>1) return true;
	return false;
}

int main() {
	string inputFile = "D-small-attempt1.in";
	string outputFile = "D-small-attempt1.out";
	ifstream fin(R"(D:\coder\)" + inputFile);
	ofstream fout(R"(D:\coder\)" + outputFile);
	int t;
	fin >> t;
	for (int k = 1; k <= t; k++) {
		int x, r, c;
		fin >> x >> r >> c;
		bool result = solve(x, r, c);
		fout << "Case #" << k << ": " << (result ? "RICHARD" : "GABRIEL") << endl;
	}
	return 0;
}
