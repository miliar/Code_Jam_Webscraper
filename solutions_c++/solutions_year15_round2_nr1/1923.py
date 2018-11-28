#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
#define CHECK(x_) if ((x_) == n) { \
	cout << c << endl; \
	for (ll l = x_; l > 1; l = M[l]) { \
		cout << l << " "; \
	} \
	cout << endl; \
	return; \
}
#define DO(x_) do { \
	CHECK(x_); \
	S.insert(x_); \
	M[x_] = x; \
	Q.emplace(x_, c); \
} while (0)

typedef pair<ll,ll> par;

ll reverse(ll x)
{
	ll ret = 0;
	int cnt = 0;
	while (x > 0) {
		ret = ret * 10 + x % 10;
		x /= 10;
		cnt++;
	}
	return ret;
}

void solve()
{
	ll n;
	cin >> n;
	if (n == 1) {cout << 1 << endl; return;}
	queue<par> Q;
	set<ll> S{1};
	map<ll,ll> M;
	Q.emplace(1,1);
	//S.insert(1);
	ll sol = 1;
	
	while (!Q.empty()) {
		ll x = Q.front().first, c = Q.front().second + 1, r = 0; Q.pop();

		ll ar[] = {reverse(x), x + 1};

		for (ll r : ar) {
			if (S.count(r) == 0) {
				S.insert(r);
				M[r] = x;
				if (r == n) {
					cout << c << endl;
					// for (ll l = r; l > 1; l = M[l]) printf("%I64d%c", l, l == 2 ? '\n' : ' ');
					return;
				}
				Q.emplace(r, c);
			}
		}

		// r = x + 1;
		// if (S.count(r) == 0) {
		// 	DO(r);
		// }
		// r = reverse(x);
		// if (S.count(r) == 0) {
		// 	DO(r);
		// }
	}
}

int main()
{
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
