#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <cstdlib>

using namespace std;

int t;
vector<char> vec;

void clear() {
	vec.clear();
}

int main() {
	ifstream fin("B-large.in", ifstream::in);
	ofstream fout("result.out", ofstream::out);
	fin >> t;
	//cin >> t;
	string s;
	for (int i = 0; i < t; ++i) {
		fin >> s;
		//cin >> s;
		int result = 0;
		int len = s.size();
		if (len > 0) {
			if (s[len - 1] == '-') {
				++result;
			}
			if (len > 1) {
				for (int i = len - 2; i >= 0; --i) {
					if (s[i] != s[i + 1]) {
						++result;
					}
				}
			}
		}
		cout << "Case #" << (i + 1) << ": " << result << endl;
		fout << "Case #" << (i + 1) << ": " << result << endl;
	}

	return 0;
}
