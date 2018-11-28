#include <bits/stdc++.h>

#define ll long long
#define ld long double
#define pb push_back
#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define Repd(i,n) for(int i = (n)-1; i >= 0; --i)
#define For(i,a,b) for(int i = (a); i <= (b); ++i)
#define Ford(i,a,b) for(int i = (a); i >= (b); --i)
#define Fit(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define Fitd(i,v) for(__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); ++i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()
#define ms(a,x) memset(a, x, sizeof(a))
#define group vector<int>

using namespace std;

const int nm = 202;

int n, k;
ld a[nm], b[nm];
ld p[nm][nm];

ld P(ld b[]) {
	memset(p, 0, sizeof(p));
	p[0][0] = 1;
	for (int i = 1; i <= k; ++i) {
		p[i][0] = p[i - 1][0] * (1.0 - b[i]);
		for (int j = 1; j <= i; ++j)
			p[i][j] = (1.0 - b[i]) * p[i - 1][j] + b[i] * p[i - 1][j - 1];
	}
	return p[k][k / 2];
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> n >> k;
	for (int i = 1; i <= n; ++i)
		cin >> a[i];
	sort(a + 1, a + n + 1);
	ld res = 0;
	for (int i = 0; i <= k; ++i) {
		for (int j = 1; j <= i; ++j)
			b[j] = a[j];
		for (int j = 1; j <= k - i; ++j)
			b[i + j] = a[n + 1 - j];
		res = max(res, P(b));
	}
	cout << setprecision(9) << fixed << (double) res << "\n";
}

int main() {
#ifdef LOCAL
	freopen("B-large (3).in", "r", stdin);
//	freopen("input.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
