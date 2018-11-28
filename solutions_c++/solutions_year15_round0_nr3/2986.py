#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }
#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)

enum V {
	One,
	I,
	J,
	K,
	MinusOne,
	MinusI,
	MinusJ,
	MinusK,
};

bool isNegative(V v) {
	switch (v) {
		case One:
		case I:
		case J:
		case K:
			return false;
		default:
			return true;
	}
}

V Minus(V v) {
	switch (v) {
		case One: return MinusOne;
		case I: return MinusI;
		case J: return MinusJ;
		case K: return MinusK;
		case MinusOne: return One;
		case MinusI: return I;
		case MinusJ: return J;
		case MinusK: return K;
		default: throw 42;
	}
}

V mult(V a, V b) {
	if (a == One) {
		return b;
	}
	if (b == One) {
		return a;
	}
	if (isNegative(a)) {
		return Minus(mult(Minus(a), b));
	}
	if (isNegative(b)) {
		return Minus(mult(a, Minus(b)));
	}
	switch (a) {
		case I:
			switch (b) {
				case I: return MinusOne;
				case J: return K;
				case K: return MinusJ;
				default: throw 42;
			}
		case J:
			switch (b) {
				case I: return MinusK;
				case J: return MinusOne;
				case K: return I;
				default: throw 42;
			}
		case K:
			switch (b) {
				case I: return J;
				case J: return MinusI;
				case K: return MinusOne;
				default: throw 42;
			}
		default: throw 42;
	}
}

V FromChar(char c) {
	switch (c) {
		case 'i': return I;
		case 'j': return J;
		case 'k': return K;
		default: throw 42;
	}
}
void Go() {
	int L, X;
	cin >> L >> X;
	string s;
	cin >> s;
	int n = L * X;
	vector<V> partialBegin(n), partialEnd(n);
	for (int i = 0; i < n; i++) {
		partialBegin[i] = mult(i == 0 ? One : partialBegin[i - 1], FromChar(s[i % L]));
	}
	for (int i = n - 1; i >= 0; i--) {
		partialEnd[i] = mult(FromChar(s[i % L]), i == n - 1 ? One : partialEnd[i + 1]);
	}

	for (int i = 1; i < n; i++) {
		if (partialBegin[i - 1] != I) {
			continue;
		}
		V sum = One;
		for (int j = i; j + 1 < n; j++) {
			sum = mult(sum, FromChar(s[j % L]));
			if (sum == J && partialEnd[j + 1] == K) {
				cout << "YES";
				return;
			}
		}
	}
	cout << "NO";
}

int main() {
	const string task = "C";
	const string folder = "gcj/2015/qual";
	const int attempt = 0;
	const bool dbg = 0;


	if (dbg) {
		freopen("inp.txt", "r", stdin);
	}
	else {
		stringstream ss;
		if (attempt < 0)
			ss << folder << '/' << task << "-large";
		else
			ss << folder << '/' << task << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}


	static char tt[128];
	gets(tt);
	int t;
	sscanf(tt, "%d", &t);
	FOR(i, t) {
		printf("Case #%d: ", i + 1);
		Go();
		printf("\n");
	}
	return 0;
}