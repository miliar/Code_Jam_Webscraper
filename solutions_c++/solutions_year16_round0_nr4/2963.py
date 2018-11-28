#include <iostream>
#include <fstream>
using namespace std;

typedef unsigned long long ll;

int main() {
	ifstream fin("D-small-attempt0.in"); ofstream fout("output.txt");

	ll t, n, c, s, x, p;
	fin >> t;

	for (int k = 1; k <= t; k++) {
		fin >> n >> c >> s;
		fout << "Case #" << k << ": ";

		x = 0, p = 1;
		for (int i = 0; i < c; i++) x += p, p *= n;
		for (int i = 0; i < n; i++) fout << 1 + i * x << ' '; fout << endl;
	}

	fin.close(); fout.close();
	return 0;
}