#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

void openFiles() {
#ifndef ONLINE_JUDGE
	//freopen("test.in", "rt", stdin);
	freopen("B-small-attempt4.in", "rt", stdin);
	freopen("B-small-attempt4.out", "wt", stdout);
#endif
}

#define REP(i, n) for (int i = 0; i < (int)(n); i++)

template <class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
	os << "["; REP(i, v.size()) os << " " << v[i]; os << " ]";
    return os;
}

/* Bruteforce alternative to verify solution. */
map<vector<int>, int> states;
int steps = 0;
int bruteforce(const vector<int>& v) {
	steps++;
	if (states.find(v) != states.end()) {
		return states[v];
	}
	if (v.size() == 0) {
		return 0;
	}
	int k = 0x7FFFFFFF;
	for (int i = 0; i < v.size() && v[i] > 0; i++) {
		if (v[i] > 1) {
			vector<int> w(v);
			w.push_back(w[i] / 2);
			w[i] = w[i] / 2 + w[i] % 2;
			sort(w.begin(), w.end());
			k = min(k, bruteforce(w) + 1);
		}
	}
	for (int i = 0; i < v.size() && v[i] > 0; i++) {
		if (v[i] > 2) {
			vector<int> w(v);
			w.push_back(w[i] / 3);
			w[i] = w[i] / 3 + (w[i] % 3 > 0 ? 1 : 0);
			w.push_back(w[i] / 3 + (w[i] % 3 == 2 ? 1 : 0));
			sort(w.begin(), w.end());
			k = min(k, bruteforce(w) + 2);
		}
	}
	vector<int> w;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > 1) {
			w.push_back(v[i] - 1);
		}
	}
	sort(w.begin(), w.end());
	k = min(k, bruteforce(w) + 1);
	states[v] = k;
	return k;
}

void solve() {
	int n; scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) {
		scanf("%d ", &v[i]);
	}
	vector<int> w = v;

	int moves = 0;
	while (v.size() > 0) {
		sort(v.rbegin(), v.rend());
		//cout << v << endl;
		bool split = false;
		if (v.size() == 1 && v[0] > 1) {
			v.push_back(v[0] / 2);
			v[0] = v[0] / 2 + v[0] % 2;
			moves++;
			continue;
		}

		for (int i = 0; i < v.size() && v[i] > 0; i++) {
			if (v[0] / 2 > i + 1 && v[0] / 2 + v[0] % 2 >= (i + 1 == v.size() ? 0 : v[i + 1])) {
				for (int j = 0; j <= i; j++) {
					v.push_back(v[j] / 2);
					v[j] = v[j] / 2 + v[j] % 2;
				}
				moves += i + 1;
				split = true;
				break;
			}
		}

		if (!split) {
			while (v.size() > 0 && (*v.rbegin()) == 1) v.pop_back();
			for (int i = 0; i < v.size(); i++) v[i]--;
			moves++;
		}
	}

	int k = bruteforce(w);
	printf("%d\n", k);
	// if (k != moves) {
	// 	printf("%d %d\n", moves, k);
	// } else {
	// 	printf("OK\n");
	// }
}

int main() {
	openFiles();
	int n; scanf("%d ", &n);
	for (int i = 0; i < n; i++) {
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
