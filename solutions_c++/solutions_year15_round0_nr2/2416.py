#include <bits/stdc++.h>

using namespace std;

#define _ ios_base::sync_with_stdio(false); cin.tie(NULL);

typedef long long ll;

constexpr int N = 1e3 + 5;

int main() { _
	ll t;
	cin >> t;
	for (ll test = 1; test <= t; ++test) {
		cout << "Case #" << test << ": ";
		vector<int> v;
		int d, ans = 1e9, mx = 0;
		cin >> d;
		for (int i = 0; i < d; ++i) {
			int p;
			cin >> p;
			v.emplace_back(p);
			mx = max(mx, p);
		}
		
		for (int i = 1; i <= mx; ++i) {
			int cnt = 0;
			for (auto j: v)
				cnt += (j - 1) / i;
			ans = min(ans, cnt + i);
		}
		cout << ans << '\n';
	}
}
