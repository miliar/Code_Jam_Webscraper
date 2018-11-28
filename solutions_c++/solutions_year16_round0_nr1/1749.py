#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <bitset>
#include <string>
#include <cassert>
#include <sstream>
#include <iostream>
using namespace std;
typedef long long LL;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }

int get(int n) {
	if (n == 0) {
		return -1;
	}
	bitset<10> digits;
	auto add = [&](int x) {
		assert(x != 0);
		while (x > 0) {
			digits[x % 10] = true;
			x /= 10;
		}
	};
	auto d = n;
	while (true) {
		add(n);
		if (digits.all()) {
			return n;
		}
		assert((LL)n + d > (LL)n);
		n += d;
	}
}
void Go() {
	int n;
	cin >> n;
	int res = get(n);
	if (res == -1) {
		cout << "INSOMNIA" << endl;
	}
	else {
		cout << res << endl;
	}
}

int main() {
	const string task = "A";
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
