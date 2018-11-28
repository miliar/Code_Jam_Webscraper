#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <string>
#include <cassert>
#include <sstream>
#include <iostream>
#include <functional>
using namespace std;
typedef long long LL;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }

char winner(char a, char b) {
	if (a == b) {
		return 0;
	}
	if (a == 'P' && b == 'R' || a == 'R' && b == 'S' || a == 'S' && b == 'P') {
		return a;
	}
	return b;
}
void Go() {
	int N, R, P, S;
	cin >> N >> R >> P >> S;
	string s;
	for (int i = 0; i < P; i++) {
		s.push_back('P');
	}
	for (int i = 0; i < R; i++) {
		s.push_back('R');
	}
	for (int i = 0; i < S; i++) {
		s.push_back('S');
	}
	string best;
	auto check = [&]() {
		string ss = s;
		while (ss.size() > 1) {
			for (int i = 0; i < ss.size() / 2; i++) {
				ss[i] = winner(ss[i * 2], ss[i * 2 + 1]);
				if (ss[i] == 0) {
					return false;
				}
			}
			ss.resize(ss.size() / 2);
		}
		return true;
	};
	do {
		if (check() && (best.size() == 0 || s < best)) {
			best = s;
		}
	} while (next_permutation(s.begin(), s.end()));
	if (best.size() == 0) {
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		cout << best << endl;
	}
}

int main() {
	const string task = "A";
	const string folder = "gcj/2016/2";
	const int attempt = 0;
	const bool dbg = false;

	if (dbg) {
		freopen("inp.txt", "r", stdin);
	}
	else {
		stringstream ss;
		ss << folder << '/' << task;
		if (attempt < 0)
			ss << "-large";
		else
			ss << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}


	static char tt[128];
	gets(tt);
	int t;
	sscanf(tt, "%d", &t);
	for (int i = 0; i < t; i++) {
		printf("Case #%d: ", i + 1);
		Go();
	}
	return 0;
}
