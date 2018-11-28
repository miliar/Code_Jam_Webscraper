#include <iostream>
#include <cstdlib>
using namespace std;

int m[256][256];

inline int multiply(int a, int b) {
	int next = m[abs(a)][b];

	return a > 0 ? next :
		(next < 0 ? abs(next) : -next);
}

bool solve3(string &s, unsigned start) {
	int current = 1;

	for (unsigned i = start; i < s.size(); i++) {
		current = multiply(current, s[i]);
	}

	return current == 'k';
}

bool solve2(string &s, unsigned start) {
	int current = 1;

	for (unsigned i = start; i < s.size(); i++) {
		current = multiply(current, s[i]);

		if (current == 'j' && solve3(s, i + 1)) {
			return true;
		}
	}

	return false;
}

bool solve1(string &s) {
	int current = 1;

	for (unsigned i = 0; i < s.size(); i++) {
		current = multiply(current, s[i]);

		if (current == 'i' && solve2(s, i + 1)) {
			return true;
		}
	}

	return false;
}

int main(void) {
	int numCases;

	m[1][1] = 1;
	m[1]['i'] = 'i';
	m[1]['j'] = 'j';
	m[1]['k'] = 'k';
	m['i'][1] = 'i';
	m['i']['i'] = -1;
	m['i']['j'] = 'k';
	m['i']['k'] = -'j';
	m['j'][1] = 'j';
	m['j']['i'] = -'k';
	m['j']['j'] = -1;
	m['j']['k'] = 'i';
	m['k'][1] = 'k';
	m['k']['i'] = 'j';
	m['k']['j'] = -'i';
	m['k']['k'] = -1;

	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		int length, times;
		string s, full;

		cin >> length >> times >> s;
		for (int i = 1; i <= times; i++) {
			full += s;
		}

		cout << "Case #" << numCase << ": ";
		if (solve1(full)) {
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	}
}