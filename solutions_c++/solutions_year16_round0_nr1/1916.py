#include <bits/stdc++.h>

using namespace std;

using ll = long long;

ll solve(ll x)
{
	if (x == 0)
		return -1;
	ll f = 0;
	for (ll y = x; ; y += x) {
		ll t = y;
		do {
			f |= (1 << (t % 10));
			t /= 10;
		} while (t);
		if (f == 0x3ff)
			return y;
	}
}

int main()
{
	cin.sync_with_stdio(false);
	cin.tie(nullptr);
    size_t n; cin >> n;
	for (size_t i = 0; i < n; ++i) {
		ll x; cin >> x;
		cout << "Case #" << (i + 1) << ": ";
		if ((x = solve(x)) == -1)
			cout << "INSOMNIA";
		else
			cout << x;
		cout << endl;
	}
	return 0;
}
