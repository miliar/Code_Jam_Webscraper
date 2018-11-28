//============================================================================
// Name        : codejam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
#define MIN(a, b) ((a > b) ? b : a)
#define MAX(a, b) ((a > b) ? a : b)

int main() {
	ifstream fi;
	ofstream fo;
	fi.open("in");
	fo.open("out");

	int t;
	fi >> t;
	for (int c = 1; c <= t; c++) {
		int m, n;
		fi >> n >> m;
		vector<vector<int> > a(n), cut(n);
		for (int i = 0; i<n; i++) {
			a[i] = vector<int>(m, 100); //, 100);
			cut[i] = vector<int>(m, 100);
			for (int j = 0; j < m; j++)
				fi >> a[i][j];
		}

		//find the max for each row
		for (int i = 0; i < n; i++) {
			int max = 0;
			for (int j = 0; j < m; j++) {
				max = MAX(max, a[i][j]);
			}
			for (int j = 0; j < m; j++) {
				cut[i][j] = min(max, cut[i][j]);
			}
		}

		for (int j = 0; j < m; j++) {
			int max = 0;
			for (int i = 0; i < n; i++) {
				max = MAX(max, a[i][j]);
			}
			for (int i = 0; i < n; i++) {
				cut[i][j] = min(max, cut[i][j]);
			}
		}
		bool feasible = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (a[i][j] != cut[i][j]) {
					feasible = false;
				}

		if (feasible) fo << "Case #" << c << ": YES\n";
		else 	fo << "Case #" << c << ": NO\n";
	}

	fo.close();
	fi.close();
	return 0;
}
