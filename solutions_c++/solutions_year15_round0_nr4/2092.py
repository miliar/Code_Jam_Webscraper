#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("omino.in");
ofstream fout("omino.out");

void solve() {
	int n, y, x;
	fin >> n >> y >> x;
	if (n == 1) {
		fout << "GABRIEL\n";
		return;
	}
	if (n == 2) {
		fout << ((x * y) % 2 == 0 ? "GABRIEL\n" : "RICHARD\n");
		return;
	}
	if (n == 3) {
		if ((x * y) % 3 != 0 || min(x,y) == 1) {
			fout << "RICHARD\n";
			return;
		}
		fout << "GABRIEL\n";
	}
	if (n == 4) {
		if (x > y) swap(x, y); // x is smaller
		if (y == 4 && x >= 3) fout << "GABRIEL\n";
		else fout << "RICHARD\n";
		return;
	}
}

int main() {
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) {
		fout << "Case #" << i+1 << ": ";
		solve();
	}
}
