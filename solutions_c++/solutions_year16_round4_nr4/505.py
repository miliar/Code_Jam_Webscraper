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
typedef pair<int, int> PII;

void Go() {
	int N;
	cin >> N;
	vector<string> mm(N);
	vector<PII> fr;
	for (int i = 0; i < N; i++) {
		cin >> mm[i];
		for (int j = 0; j < N; j++) {
			if (mm[i][j] == '0') {
				fr.push_back(PII(i, j));
			}
		}
	}
	auto ok = [&]() {
		vector<int> ww(N);
		for (int i = 0; i < N; i++) {
			ww[i] = i;
		}
		vector<char> used(N);
		function<bool(int)> bad = [&](int p) {
			if (p == -1) {
				return false;
			}
			bool found = false;
			for (int i = 0; i < N; i++) {
				if (mm[ww[p]][i] == '1' && !used[i]) {
					found = true;
					used[i] = 1;
					if (bad(p - 1)) {
						return true;
					}
					used[i] = 0;
				}
			}
			return !found;
		};
		do {
			if (bad(N - 1)) {
				return false;
			}
		} while (next_permutation(ww.begin(), ww.end()));
		return true;
	};
	int bestRes = -1;
	for (int m = 0; m < (1 << fr.size()); m++) {
		int bc = 0;
		for (int i = 0; i < fr.size(); i++) {
			if (m & (1 << i)) {
				mm[fr[i].first][fr[i].second] = '1';
				bc++;
			}
		}
		if (ok() && (bestRes == -1 || bc < bestRes)) {
			bestRes = bc;
		}
		for (int i = 0; i < fr.size(); i++) {
			if (m & (1 << i)) {
				mm[fr[i].first][fr[i].second] = '0';
			}
		}
	}
	cout << bestRes << endl;
}

int main() {
	const string task = "D";
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
