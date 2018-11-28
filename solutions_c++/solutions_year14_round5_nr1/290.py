#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <iostream>
#include <utility>
#include <cctype>
using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x))

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define FU(i, a, b) for(decltype(b) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)

#define mset(c, v) memset(c, v, sizeof(c))
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define SZ(c) int((c).size())

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;
const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;


int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

vll S;
ll best(int size) {
	int m = 0, M = size;
	ll ans = 1000000000000000ll;
	while (M > m) {
		int me = (m + M)/2;
		ll tmp = max(S[me], S[size] - S[me]);
		ans = min(ans, tmp);
		if (tmp == S[me]) M = me;
		else m = me+1;
	}
	return ans;
}

int main() {
	int _42;
	cin >> _42;
	fu(_41, _42) {
		printf("Case #%d: ", _41+1);
		ll N, p, q, r, s;
		cin >> N >> p >> q >> r >> s;
		vll X(N);
		fu(i, N) X[i] = ( (i*p + q) % r) + s;
		S.assign(N+1, 0);
		FU(i, 1, N+1) S[i] = S[i-1] + X[i-1];
		ll ans = 1000000000000000000ll;
		// try with a = 0
		fu(b, N+1) {
			ll tmp = max(S[b], S[N] - S[b]);
			ans = min(ans, tmp);
		}
		// try the rest
		FU(b, 1, N+1) {
			ll tmp = max(S[N] - S[b], best(b));
			ans = min(ans, tmp);
		}
		double A = S[N] - ans;
		A /= S[N];
		printf("%.10f\n", A);
	}
	return 0;
}
