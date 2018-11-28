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
using namespace std;
typedef long long LL;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }


int get(const string& s) {
	int d = 0;
	int n = s.size();
	for (int i = 0; i < n; i++) {
		if (i == n || s[i] != s[i + 1]) {
			d++;
		}
	}
	if (s[n - 1] == '+') {
		return d - 1;
	}
	else {
		return d;
	}
}
void Go() {
	string s;
	cin >> s;
	cout << get(s) << endl;
}

int main() {
	const string task = "B";
	const string folder = "gcj/2016/qual";
	const int attempt = -1;
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
