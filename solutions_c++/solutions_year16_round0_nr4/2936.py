#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<vii> vvii;
typedef set<int> si;
typedef vector<si> vsi;
typedef pair<double, double> dd;

const int inf = 1e9;

int main() {
	ios::sync_with_stdio(false);

	int ts; cin >> ts;
	for (int t = 1; t <= ts; t++) {
		ll k, c, s;
		cin >> k >> c >> s;

		vector<ll> ans;
		ll step = pow(k, c - 1);
		ll last = pow(k, c);
		if (c == 1)
			step = 0;
		for (ll i = 1; i <= last; i += step, i++)
			ans.push_back(i);

		cout << "Case #" << t << ": ";
		cout << ans[0];
		for (int i = 1; i < ans.size(); i++)
			cout << ' ' << ans[i];
		cout << endl;
	}

	return 0;
}
