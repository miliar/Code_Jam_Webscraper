#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define all_of(v) v.begin(), v.end()
#define fi first
#define se second
#define pb push_back

int solve(vector<string> v) {
	vector<string> result;
	vector<vector<int>> repeats;

	for (string s: v) {
		result.pb("");
		repeats.pb({1});
		for (int i = 0; i < s.length() - 1; i++) {
			if (s[i] != s[i + 1]) {
				repeats.back().pb(1);
				result.back() += s[i];
			} else {
				repeats.back().back()++;
			}
		}

		result.back() += s[s.length() - 1];
	}

	for (int i = 1; i < result.size(); i++) {
		if (result[i] != result[i - 1]) {
			return -1;
		}
	}

	int ans = 0;

	for (int i = 0; i < result.back().length(); i++) {
		int cur_min = INT_MAX;
		
		for (int target = 1; target <= 100; target++) {
			int new_min = 0;
			for (int j = 0; j < repeats.size(); j++) {
				new_min += abs(repeats[j][i] - target);
			}

			if (new_min < cur_min) {
				cur_min = new_min;
			}
		}

		if (cur_min == INT_MAX) {
			cerr << "Error\n";
		}

		ans += cur_min;
	}

	return ans;
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		int n;
		cin >> n;

		vector<string> v(n);
		for (int i = 0; i < n; i++) {
			cin >> v[i];
		}

		int ans = solve(v);
		if (ans == -1) {
			cout << "Case #" << test << ": Fegla Won" << endl;
		} else {
			cout << "Case #" << test << ": " << ans << endl;
		}
	}
}