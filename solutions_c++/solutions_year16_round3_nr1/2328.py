
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include <queue>
#include "string.h"
#include "assert.h"
#include "math.h"

using namespace std;

typedef vector<pair<int, char>> vec;
bool rev_order(const pair<int, int> & a, const pair<int, int> & b) {
	return a.first > b.first;
}


void solve() {
	int N; cin >> N;
	vec v;
	int s = 0;

	for (int i = 0; i < N; i++) {
		int k; cin >> k;
		v.push_back(pair<int,char>(k, i + 'A'));
		s += k;
	}
	if (s == 1) {
		cout << v[0].second;
		return;
	}

	sort(v.begin(), v.end(), rev_order);

	if (s % 2 == 1) {
		cout << v[0].second << " ";
		(v[0].first)--;
		sort(v.begin(), v.end(), rev_order);
	}

	while (N > 0) {
		cout << v[0].second;
		(v[0].first)--;
		if (N > 1) {
			cout << v[1].second;
			(v[1].first)--;
		}

#if 1
		int s = 0;
		for (int i = 0; i < N; i++)
			s += v[i].first;

		for (int i = 0; i < N; i++)
			if (v[i].first > s / 2)
				cout << " ERROR ";
#endif

		sort(v.begin(), v.end(), rev_order);
		while (N > 0 && v[N - 1].first == 0)
			N--;

		if (N > 0) {
			cout << " ";
		}
	}
}

int main(int argc, char** argv) {
	int T;
	cin >> T; // number of test cases
	string s; getline(cin, s);
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}

	
