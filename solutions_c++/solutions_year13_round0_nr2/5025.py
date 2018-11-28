/*
 * main.cpp
 *
 *  Created on: 7 avr. 2013
 *      Author: Khabat95
 */


#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cassert>
#include <complex>

using namespace std;

void algo() {
	int n, m;
	cin >> n >> m;

	int lawn[n][m];
	int h_line[n];
	int h_column[m];
	for(int i=0; i<n; ++i) {
		for(int j=0; j<m; ++j) {
			cin >> lawn[i][j];

			if(i == 0)
				h_column[j] = lawn[i][j];
			else
				h_column[j] = max(h_column[j], lawn[i][j]);

			if(j == 0)
				h_line[i] = lawn[i][j];
			else
				h_line[i] = max(h_line[i], lawn[i][j]);

		}
	}

	bool res = false;
	for(int i=0; i<n; ++i) {
		for(int j=0; j<m; ++j) {
			if((lawn[i][j] != h_line[i]) && (lawn[i][j] != h_column[j])) {
				cout << "NO" << endl;
				return;
			}
		}
	}

	cout << "YES" << endl;
}

int main() {
	int n_cases;
	cin >> n_cases;

	for(int i=0; i<n_cases; ++i) {
		cout << "Case #" << i+1 << ": ";
		algo();
	}
}

