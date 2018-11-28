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

int main() {
	ifstream fin("C-large.in", ifstream::in);  // TODO
	ofstream fout("result.out", ofstream::out);
	fin >> t;  // t = 1;
	//cin >> t;
	assert(t == 1);
	int n, j;
	for (int i = 0; i < t; ++i) {
		fin >> n >> j;
		//cin >> n >> j;
		assert(n == 32);  // TODO
		assert(j == 500);  // TODO
		cout << "Case #" << (i + 1) << ":" << endl;
		fout << "Case #" << (i + 1) << ":" << endl;
		int count = 0;
		for (int s = 3; s < n - 1; s += 2) {
			for (int t = 1; t < s; t += 2) {
				for (int p = 4; p < n - 1; p += 2) {
					for (int q = 2; q < p; q += 2) {
						bitset<32> result;  // TODO
						result.set(n - 1);
						result.set(0);

						cout << p << "," << q << "," << s << ","<< t << endl;
						result.set(p);
						result.set(q);
						result.set(s);
						result.set(t);

						cout << result << " 3 2 5 2 7 2 9 2 11" << endl;
						fout << result << " 3 2 5 2 7 2 9 2 11" << endl;
						++count;
						if (count >= j) {
							cout << "break" << endl;
							return 0;
						}
					}
				}
			}
		}
	}
	return 0;
}
