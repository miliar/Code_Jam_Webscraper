#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pllll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pii> vpii;
typedef vector<pllll> vpllll;
#define NoSync_NoTie ios_base::sync_with_stdio(0); cin.tie(0);
#define INF INT_MAX
#define UINF UINT_MAX
#define LLINF LLONG_MAX
#define ULLINF ULLONG_MAX
#define REP(i, a, b) for (int i = a; i < b; ++i)
#define REPI(i, a, b) for (int i = a; i <= b; ++i)
#define rep(i, n) REP(i, 0, n)
#define repi(i, n) REPI(i, 0, n)
#define memall(arr, x) memset(arr, x, sizeof arr)
#define sz(x) x.size()
#define all(x) x.begin(), x.end()
#define isOdd(x) (x&1)
#define isEven(x) (!(x&1))
int gcd(int a, int b) { return (!a ? b : gcd(b % a, a)); }
int lcm(int a, int b) { return (a * (b / gcd(a, b))); }
vi v;
int c[10], special = 0;
void solve(int i) {
	if (!i)
		return;
	while (!c[i])
		--i;
	v.push_back(special + i);
	for (int j = 1; j <= i / 2; ++j) {
		c[j] += c[i];
		c[i - j] += c[i];
		special += c[i];
		solve(i - 1);
		c[j] -= c[i];
		c[i - j] -= c[i];
		special -= c[i];
	}
}
int main() {
	NoSync_NoTie
	ifstream cin("B-small.in");
	ofstream cout("B-small.out");
	int T;
	cin >> T;
	rep(t, T) {
		v.clear();
		memall(c, 0);
		special = 0;
		int d, mx = 0;
		cin >> d;
		rep(i, d) {
			int p;
			cin >> p;
			c[p]++;
			mx = max(mx, p);
		}
		solve(mx);
		int ans = v[0];
		rep(i, sz(v))
			ans = min(ans, v[i]);
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}