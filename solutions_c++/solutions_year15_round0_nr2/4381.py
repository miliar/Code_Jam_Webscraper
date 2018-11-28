#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

void fastInOut();

int d, mx;
vector<int> arr;

bool isZero(vector<int>& cur) {
	for (int i = 0; i < int(cur.size()); ++i)
		if (cur[i] != 0)
			return 0;
	return 1;
}

int bt(vector<int> cur, int lvl) {
	if (isZero(cur))
		return 0;
	if (lvl == mx)
		return 1e9;
	int ret = 1e9, sz = cur.size();
	sort(cur.begin(), cur.end());
	cur.push_back(0);
	for (int dv = 2; dv <= 3; ++dv) {
		int md = cur[sz - 1] / dv;
		if (md != 0) {
			cur[sz - 1] -= md, cur[sz] += md;
			ret = min(ret, 1 + bt(cur, lvl + 1));
			cur[sz - 1] += md, cur[sz] -= md;
		}
	}
	cur.pop_back();
	for (int i = 0; i < sz; ++i)
		cur[i] = max(0, cur[i] - 1);
	return ret = min(ret, 1 + bt(cur, lvl + 1));
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	fastInOut();
	int t;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		cin >> d, arr.resize(d), mx = 0;
		for (int i = 0; i < d; ++i)
			cin >> arr[i], mx = max(mx, arr[i]);
		cout << "Case #" << tst << ": " << bt(arr, 0) << endl;
	}
	return 0;
}

void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}
