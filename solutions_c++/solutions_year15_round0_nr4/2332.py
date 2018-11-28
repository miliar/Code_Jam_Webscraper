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
bool whatever(int x, int r, int c) {
	return !(r % x) && c >= x - 1 || !(c % x) && r >= x - 1;
}
int main() {
	NoSync_NoTie
	ifstream cin("D-small.in");
	ofstream cout("D-small.out");
	int T;
	cin >> T;
	rep(t, T) {
		int x, r, c;
		cin >> x >> r >> c;
		cout << "Case #" << t + 1 << ": " << (whatever(x, r, c) ? "GABRIEL" : "RICHARD") << endl;
	}
	return 0;
}