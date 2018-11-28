#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <climits>
#include <ctime>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <memory.h>
#include <bitset>
#include <cstring>

using namespace std;

#define ll long long
#define mp make_pair

ll n, t, r, p, s;

string solve(string ss, int l, int r) {
	string tmps = "";
	if (r - l == 0) {
		return tmps + ss[l];
	}
	int mid = (r + l) / 2;
	string st1 = "", st2 = "";
	for (int i = l; i < mid + 1; i++)
		st1 += ss[i];
	for (int i = mid + 1; i <= r; i++) {
		st2 += ss[i];
	}
	if (st2 < st1) {
		return solve(ss, mid + 1, r) + solve(ss, l, mid);
	}
	else {
		return solve(ss, l, mid) + solve(ss, mid + 1, r);
	}
}

string convert(string ss) {
	return solve(ss, 0, ss.length() - 1);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> n >> r >> p >> s;
		vector<string> ans;
		for (int cur = 0; cur < 3; cur++) {
			ll ts = 0;
			ll tr = 0;
			ll tp = 0;
			vector<ll> v, v1;
			v.push_back(cur);
			for (int i = 0; i < n; i++) {
				v1.clear();
				for (int j = 0; j < v.size(); j++) {
					if (v[j] == 0) {
						v1.push_back(0);
						v1.push_back(1);
					}
					else if (v[j] == 1) {
						v1.push_back(1);
						v1.push_back(2);
					}
					else {
						v1.push_back(0);
						v1.push_back(2);
					}
				}
				v = v1;
			}
			for (int i = 0; i < v.size(); i++) {
				if (v[i] == 0)
					tp++;
				if (v[i] == 1)
					tr++;
				if (v[i] == 2)
					ts++;
			}
			if (tp <= p && tr <= r && ts <= s) {
				string ss = "";
				for (int j = 0; j < v.size(); j++) {
					if (v[j] == 0) {
						ss += 'P';
					}
					else if (v[j] == 1) {
						ss += 'R';
					}
					else if (v[j] == 2) {
						ss += 'S';
					}
				}
				ans.push_back(ss);
			}
		}
		cout << "Case #" << ii + 1 << ": ";
		if (ans.size()) {
			for (int i = 0; i < ans.size(); i++)
				ans[i] = convert(ans[i]);
			sort(ans.begin(), ans.end());
			cout << ans[0] << endl;
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}