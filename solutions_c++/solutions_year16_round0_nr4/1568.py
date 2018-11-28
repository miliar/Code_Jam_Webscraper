#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
#include <bitset>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <assert.h>

using namespace std;

int t;
int mat[100][100];

void clear() {
	memset(mat, 0, 10000 * sizeof(int));
}

int main() {
	ifstream fin("D-small-attempt1.in", ifstream::in);  // TODO
	ofstream fout("result.out", ofstream::out);
	fin >> t;
	//cin >> t;
	int k, c, s;
	for (int i = 0; i < t; ++i) {
		clear();
		fin >> k >> c >> s;
		//cin >> k >> c >> s;
		if (s >= k) {  // TODO
			cout << "Case #" << (i + 1) << ": ";
			fout << "Case #" << (i + 1) << ": ";
			for (int j = 1; j <= k; ++j) {
				cout << j << " ";
				fout << j << " ";
			}
			cout << endl;
			fout << endl;
		} else {
			if (c * s < k) {
				cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
				fout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
				continue;
			}
			int temp = 0;
			for (int p = 0; p < c; ++p) {
				for (int q = 0; q < s; ++q) {
					if (temp < k) {
						mat[p][q] = temp++;
					} else {
						mat[p][q] = 0;  // TODO check 0 or 1?
					}
					
				}
			}
			cout << "Case #" << (i + 1) << ": ";
			fout << "Case #" << (i + 1) << ": ";
			for (int p = 0; p < s; ++p) {
				long long result = 0;  // TODO check
				for (int q = 0; q < c; ++q) {
					result += mat[q][p] * pow(k, c - 1 - q);
				}
				cout << ++result << " ";
				fout << ++result << " ";
			}
			cout << endl;
			fout << endl;
		}
	}
	return 0;
}
