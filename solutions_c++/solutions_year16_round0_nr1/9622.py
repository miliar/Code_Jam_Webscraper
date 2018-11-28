#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define sz(v) (int)v.size()

const int MX = 1000006;

ll ans[MX];

ll solve (ll n) {
	ll i;
	set<int> s;
	for (i = 1; sz(s) != 10; i++) {
		ll t = i * n;
		while (t) {
			s.insert(t % 10);
			t /= 10;
		}
	}
	return (i - 1) * n;
}

int main ( ) {
	freopen("1", "rt", stdin);
	freopen("2", "wt", stdout);
	for (int i = 1; i < MX; i++) {
		ll t = solve(i);
		ans[i] = t;
	}
	int tc, t = 0, n;
	scanf("%d", &tc);
	while (tc--) {
		scanf("%d", &n);
		if (!n) printf("Case #%d: INSOMNIA\n", ++t);
		else printf("Case #%d: %lld\n", ++t, ans[n]);
	}
}
