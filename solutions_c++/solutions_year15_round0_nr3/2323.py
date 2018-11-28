#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include "string.h"
#include "assert.h"
#include "math.h"

using namespace std;

#define abs(x)		((x) > 0 ? (x) : -(x))
#define sign(x)     ((x) > 0 ? 1 : -1)

bool rev_order(const pair<int, int> & a, const pair<int, int> & b) {
	return a.first > b.first;
}


// They are associative. Hooray!!!

void print(int r) {
	if (r < 0) {
		cout << '-';
		r = -r;
	}
	if (r == 1)
		cout << 1;
	else {
		cout << (char)('i' - 2 + r);
	}
}

/*
char table[3][3] = {
	{ -1,   'k',  -'j'},
	{ -'k', -1,   'i' }, 
	{ 'j', -'i', -1 }
};
*/

int table[4][4] = {
	{ 1,  2,  3,  4 }, 
	{ 2, -1,  4, -3 },
	{ 3, -4, -1,  2 },
	{ 4,  3, -2, -1 }
};

inline 
int step(int a, int b) {
	int c = sign(a) * sign(b) * table[abs(a) - 1][abs(b) - 1];
	return c;
}


int reduce(const char * s) {
	char r = 1;
	while (*s != 0) {
		char c = *s++;
		r = step(r, c - 'i' + 2);
	}
	return r;
}

typedef unsigned long long int uint64;

bool solve() {
	int L;
	uint64 X;

	cin >> L >> X;

	// Just reduce one instance for now
	string _s; cin >> _s; 
	const char * s = _s.c_str();

	int w = reduce(s);
	int whole = 1;
	uint64 Xrem = X % 4;
	for (int i = 0; i < Xrem; i++) 
		whole = step(whole, w);

	// "ijk" reduces to -1
	if (whole != -1)
		return false;


	// Find prefix that forms i and suffix that forms k
	bool done = false;
	int ri = 1, rk = 1;
	int ti = 0, li = 0, tk = 0, lk = 0, xi = 0, xk = 0;

	for (ti = 0; ti < X*L; ti++, li++) {
		if (li == L) {
			li = 0; xi++;
		}
		if (xi == 4)
			return false;
		ri = step(ri, s[li] - 'i' + 2);
		if (ri == 2)
			break;
	}

	if (ti >= X*L)
		return false;

	for (tk = 0; ti < X*L; tk++, lk++) {
		if (lk == L) {
			lk = 0; xk++;
		}
		if (xk == 4)
			return false;
		rk = step(s[L - lk - 1] - 'i' + 2, rk);
		if (rk == 4)
			break;
	}
	if (tk >= X*L)
		return false;

	if (ti + tk >= X*L)
		return false;

	return true;
}

int main(int argc, char** argv) {
	int T;
	cin >> T; // number of test cases

	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		bool a = solve();
		cout << (a ? "YES" : "NO");
		cout << endl;
	}
}

	