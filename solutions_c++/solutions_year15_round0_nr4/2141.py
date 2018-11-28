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


int WhoWin(int X, int R, int C) {
	if (C < R) {
		return WhoWin(X, C, R);
	}
	if (X == 1) {
		return 2;
	}
	if (R * C % X != 0) {
		return 1;
	}
	if (X == 2) {
		return 2;
	}
	if (R < X && C < X) {
		return 1;
	}

	int pb[8][4] = {
		3, 1, 3, 1,
		3, 2, 3, 2,
		3, 3, 3, 2,
		3, 3, 4, 2,
		4, 1, 4, 1,
		4, 2, 4, 1,
		4, 3, 4, 2,
		4, 4, 4, 2,
	};
	for (int i = 0; i < 8; i++) {
		if (pb[i][0] == X && pb[i][1] == R && pb[i][2] == C) {
			return pb[i][3];
		}
	}
	throw 42;
}

void Go() {
	int X, R, C;
	cin >> X >> R >> C;
	if (WhoWin(X, R, C) == 1) {
		cout << "RICHARD";
	}
	else {
		cout << "GABRIEL";
	}
}

int main() {
	const string task = "D";
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