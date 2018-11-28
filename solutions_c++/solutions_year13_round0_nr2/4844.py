#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <fstream>

using namespace std;

ifstream in;
ofstream out;

int main() {
	
    in.open("input.txt");
    out.open("output.txt");
	int t, n, m;
	in >> t;
	bool no_solution;
	vector< vector<int> > a;
	vector<int> max_raw, max_col;
	for (int i = 0; i < t; ++i) {
		out << "Case #" << i + 1 << ": ";
		no_solution = false;
		in >> n >> m;
		a.resize(n);
		max_raw.assign(n, 0);
		max_col.assign(m, 0);
		for (int j = 0; j < n; ++j) {
			a[j].resize(m);
			for (int k = 0; k < m; ++k) {
				in >> a[j][k];
				if (a[j][k] > max_raw[j]) {
					max_raw[j] = a[j][k];
				}
			}
		}
		for (int j = 0; j < m; ++j) {
			for (int k = 0; k < n; ++k) {
				if (a[k][j] > max_col[j]) {
					max_col[j] = a[k][j];
				}
			}
		}
		/*for (int j = 0; j < m; ++j) {
			out << max_col[j] << " ";
		}
		out << "\n";
		for (int j = 0; j < n; ++j) {
			out << max_raw[j] << " ";
		}
		out << "\n";*/
		for (int j = 0; j < n; ++j) {
			for (int k = 0; k < m; ++k) {
				if (a[j][k] != min(max_raw[j], max_col[k])) {
					no_solution = true;
					break;
				}
			}
			if (no_solution) {
				break;
			}
		}
		if (no_solution) {
			if (i == t - 1)
				out << "NO";
			else
				out << "NO\n";
		} else {
			if (i == t - 1)
				out << "YES";
			else
				out << "YES\n";
		}

	}

	//system("PAUSE");
}