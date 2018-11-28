#include <cstdio>
#include <iostream>
using namespace std;

typedef long long ll;

int t;
ll n, p;

ll getBest(int n, ll worse)
{
	if (worse == 0) return (1ll << n) - 1ll;
	return getBest(n - 1, (worse - 1ll) / 2ll);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		cin >> n >> p;
		cout << "Case #" << tc << ": ";
		ll l = 0, r = (1ll << n) - 1ll;
		ll res = 0;
		while (l <= r) {
			ll mid = l + r >> 1ll;
			ll cur = (1ll << n) - 1ll - mid;
			ll pl = getBest(n, (1ll << n) - 1ll - cur);
			if ((1ll << n) - 1ll - pl <= p - 1ll) { res = mid; l = mid + 1ll; }
			else r = mid - 1ll;
		}
		cout << res << " ";
		l = 0, r = (1ll << n) - 1ll;
		res = 0;
		while (l <= r) {
			ll mid = l + r >> 1;
			if (getBest(n, (1ll << n) - 1ll - mid) <= p - 1ll) { res = mid; l = mid + 1ll; }
			else r = mid - 1ll;
		}
		cout << res << endl;
	}
	return 0;
}