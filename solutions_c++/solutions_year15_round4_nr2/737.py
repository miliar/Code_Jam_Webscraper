#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("B-small-attempt0.in");
ofstream fout("test.out");

int n;
double v, x;
double r[100], c[100];

int main() {
	int t;
	fin >> t;
	for (int case_num = 1; case_num <= t; case_num++) {
		fin >> n >> v >> x;
		for (int i = 0; i < n; i++)
			fin >> r[i] >> c[i];
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				if (c[i] > c[j]) {
					swap(r[i], r[j]);
					swap(c[i], c[j]);
				}
		fout << "Case #" << case_num << ": ";
		fout.precision(15);
		if (c[0] == x && c[1] == x) {
			fout << v / (r[0] + r[1]) << endl;
			continue;
		}
		if (c[0] == x) {
			fout << v / r[0] << endl;
			continue;
		}
		if (c[1] == x) {
			fout << v / r[1] << endl;
			continue;
		}
		if (c[1] < x || c[0] > x) {
			fout << "IMPOSSIBLE" << endl;
			continue;
		}
		double f1 = x - c[0], f2 = c[1] - x;
		double v1 = v * f2 / (f1 + f2);
		double v2 = v * f1 / (f1 + f2);
		fout << max(v1 / r[0], v2 / r[1]) << endl;
	}
	return 0;
}