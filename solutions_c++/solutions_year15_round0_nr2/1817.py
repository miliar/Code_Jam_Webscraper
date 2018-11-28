
//#pragma warning(disable:4996)

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <utility>
#include <string>
using namespace std;

const int maxn = 1000 + 123;
int amt[1234][1234] = {0};

void init() {
	amt[2][1] = 1;
	int offer;
	const int upper_bnd = 1000;
	for (int i = 3; i <= upper_bnd; ++i) {
		for (int j = 1; j < i; ++j) {
			amt[i][j] = i - 1; //i-1
			for (int t = 1; t + t <= i; ++t) {
				//t, i - t
				offer = 1 + amt[t][j] + amt[i-t][j];
				if (offer < amt[i][j]) {
					amt[i][j] = offer;
				}
			}
		}
	}
}

int solve(int n, const vector<int>& v) {
	static vector<int> m(maxn);
	int mx = v[0];
	for (int i = 1; i < n; ++i) {
		mx = max(mx, v[i]);
	}
	for (int i = 1; i <= mx; ++i) {
		m[i] = 0;
		for (int j = 0; j < n; ++j) {
			m[i] += amt[v[j]][i];
		}
	}
	int ans = m[1] + 1;
	for (int i = 2; i <= mx; ++i){ 
		ans = min(ans, m[i] + i);
	}
	return ans;
}

int main () {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	vector<int> v(maxn);
	int n;
	init();

	int t;
	cin >> t;
	int ans;
	for (int test = 1; test <= t; ++test) {
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> v[i];
		}
		ans = solve(n, v);
		cout << "Case #" << test << ": ";
		cout << ans;
		cout << "\n";
	}

	return 0;
}