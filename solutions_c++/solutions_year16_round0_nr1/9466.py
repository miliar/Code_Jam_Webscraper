#include <iostream>
#include <fstream>

using namespace std;

int main () {
	ifstream fin ("a.in");
	ofstream fout ("a.out");
	int T;
	fin >> T;
	for (int tt = 0; tt < T; tt++) {
		int n;
		fin >> n;
		fout << "Case #" << tt + 1 << ": ";
		if (!n)
			fout << "INSOMNIA";
		else {
			int cnt = 0, k = 1, x = n;
			bool a[10] = {0};
			while (cnt < 10) {
				while (x) {
					int q = x % 10;
					if (!a[q]) {
						a[q] = 1;
						cnt++;
					}
					x /= 10;
				}
				k++;
				x = k * n;
			}
			fout << (k-1) * n;
		}
		fout << endl;
	}
	return 0;
}
