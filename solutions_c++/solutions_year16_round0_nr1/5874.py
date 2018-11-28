#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define ll long long
int t;
ll n;
int main() {
	ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	#endif

	cin >> t;
	for (int i = 1; i <= t; ++i) {
		ll n;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA\n";
			continue;
		}
		ll init = n;
		set<int> mySet;
		ll x = n;
		while (x) {
			mySet.insert(x % 10);
			x /= 10;
		}
		int ceva = 2;
		for (; ;) {
			if (mySet.size() == 10) {
				cout << "Case #" << i << ": " << n << "\n";
				break;
			} else {

				n += init;
				//cout << n << "\n";
				ceva++;
				ll x = n;
				while (x) {
					mySet.insert(x % 10);
					x /= 10;
				}
			}
		}
	}

	return 0;
}