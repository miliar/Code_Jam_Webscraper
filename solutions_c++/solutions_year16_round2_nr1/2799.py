#include <cstdio>
#include <iostream>
#include <algorithm>
#include <functional>
#include <sstream>
#include <cmath>
#include <string>

using namespace std;

int his[50];
string s;
int res[50];

void solved() {
	for (int i = 0; i < 10; ++i) {
		res[i] = 0;
		his[i] = 0;
	}

	for (int i = 0; i < s.length(); ++i) {
		++his[(int)(s[i] - 'A')];
	}

	if (his[(int)('G' - 'A')] > 0) {
		int t = his[(int)('G' - 'A')];
		his[(int)('E' - 'A')] -= t;
		his[(int)('I' - 'A')] -= t;
		his[(int)('G' - 'A')] -= t;
		his[(int)('H' - 'A')] -= t;
		his[(int)('T' - 'A')] -= t;

		res[8] = t;
	}

	if (his[(int)('W' - 'A')] > 0) {
		int t = his[(int)('W' - 'A')];
		his[(int)('T' - 'A')] -= t;
		his[(int)('W' - 'A')] -= t;
		his[(int)('O' - 'A')] -= t;

		res[2] = t;
	}

	if (his[(int)('X' - 'A')] > 0) {
		int t = his[(int)('X' - 'A')];
		his[(int)('S' - 'A')] -= t;
		his[(int)('I' - 'A')] -= t;
		his[(int)('X' - 'A')] -= t;

		res[6] = t;
	}

	if (his[(int)('S' - 'A')] > 0) {
		int t = his[(int)('S' - 'A')];
		his[(int)('S' - 'A')] -= t;
		his[(int)('E' - 'A')] -= t;
		his[(int)('V' - 'A')] -= t;
		his[(int)('E' - 'A')] -= t;
		his[(int)('N' - 'A')] -= t;

		res[7] = t;
	}

	if (his[(int)('V' - 'A')] > 0) {
		int t = his[(int)('V' - 'A')];
		his[(int)('F' - 'A')] -= t;
		his[(int)('I' - 'A')] -= t;
		his[(int)('V' - 'A')] -= t;
		his[(int)('E' - 'A')] -= t;

		res[5] = t;
	}

	if (his[(int)('Z' - 'A')] > 0) {
		int t = his[(int)('Z' - 'A')];
		his[(int)('Z' - 'A')] -= t;
		his[(int)('E' - 'A')] -= t;
		his[(int)('R' - 'A')] -= t;
		his[(int)('O' - 'A')] -= t;

		res[0] = t;
	}

	if (his[(int)('T' - 'A')] > 0) {
		int t = his[(int)('T' - 'A')];
		his[(int)('T' - 'A')] -= t;
		his[(int)('H' - 'A')] -= t;
		his[(int)('R' - 'A')] -= t;
		his[(int)('E' - 'A')] -= t;
		his[(int)('E' - 'A')] -= t;

		res[3] = t;
	}

	if (his[(int)('R' - 'A')] > 0) {
		int t = his[(int)('R' - 'A')];
		his[(int)('F' - 'A')] -= t;
		his[(int)('O' - 'A')] -= t;
		his[(int)('U' - 'A')] -= t;
		his[(int)('R' - 'A')] -= t;

		res[4] = t;
	}

	if (his[(int)('O' - 'A')] > 0) {
		int t = his[(int)('O' - 'A')];
		his[(int)('O' - 'A')] -= t;
		his[(int)('N' - 'A')] -= t;
		his[(int)('E' - 'A')] -= t;

		res[1] = t;
	}

	if (his[(int)('I' - 'A')] > 0) {
		int t = his[(int)('I' - 'A')];
		his[(int)('N' - 'A')] -= t;
		his[(int)('I' - 'A')] -= t;
		his[(int)('N' - 'A')] -= t;
		his[(int)('E' - 'A')] -= t;

		res[9] = t;
	}
}

int main() {
	
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cin >> s;
		cout << "Case #" << i << ": ";
		solved();
		for (int j = 0; j <= 9; ++j) {
			if (res[j] > 0) {
				for (int z = 0; z < res[j]; ++z) {
					cout << j;
				}
			}
		}

		cout << endl;
	}

	return 0;
}