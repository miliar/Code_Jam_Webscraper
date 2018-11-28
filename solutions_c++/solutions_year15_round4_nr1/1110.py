#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include "math.h"

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define fori(i, a, b) for (int i = int(a); i <= int(b); i++)

typedef long long ll;

using namespace std;

int r, c;
char a[100][100];

bool checkRight(int i, int j) {
	fori(x, j + 1, c - 1) {
		if (a[i][x] != '.') {
			return true;
		}
	}
	return false;
}

bool checkDown(int i, int j) {
	fori(x, i + 1, r - 1) {
		if (a[x][j] != '.') {
			return true;
		}
	}
	return false;
}

bool checkLeft(int i, int j) {
	fori(x, 0, j - 1) {
		if (a[i][x] != '.') {
			return true;
		}
	}
	return false;
}

bool checkUp(int i, int j) {
	fori(x, 0, i - 1) {
		if (a[x][j] != '.') {
			return true;
		}
	}
	return false;
}

int f() {
	int s = 0;
	forn(i, r) {
		forn(j, c) {
			char d = a[i][j];
			if (d != '.') {
				bool f = false;
				if (d == '>') {
					if (!checkRight(i, j)) {
						f = true;
					}
				} else if (d == '<') {
					if (!checkLeft(i, j)) {
						f = true;
					}
				} else if (d == '^') {
					if (!checkUp(i, j)) {
						f = true;
					}
				} else if (d == 'v') {
					if (!checkDown(i, j)) {
						f = true;
					}
				}
				if (f) {
					s++;
					if (!checkRight(i, j) && !checkLeft(i, j) && !checkUp(i, j) && !checkDown(i, j)) {
						return -1;
					}
				}
			}
		}
	}
	return s;
}

int main() {
	int ntc;
	cin >> ntc;
	fori(tc, 1, ntc) {
		cin >> r >> c;
		forn(i, r) {
			forn(j, c) {
				cin >> a[i][j];
			}
		}
		cout << "Case #" << tc << ": ";
		int s = f();
		if (s == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << s;
		}
		cout << endl;
	}
	return 0;
}
