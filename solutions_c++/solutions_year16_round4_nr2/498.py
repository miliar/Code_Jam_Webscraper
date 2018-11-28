#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vb> vvb;
typedef vector<vs> vvs;
typedef vector<vl> vvl;

int inf = 0x3f3f3f3f;
double eps = 10e-8;
ll mod = 1000000007ll;

#define rep(k, a, b) for (int k = (a); k < int(b); k++)
#define sz(a) int(a.size())
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define x first
#define y second
#define mi(r, c, v) vvi(r, vi(c, v))
#define rrep(k, a, b) for (int k = (a); k >= int(b); k--)
#define irep(k, a) for (auto& k : (a))
#define md(r, c, v) vvd(r, vd(c, v))
#define mb(r, c, v) vvb(r, vb(c, v))
#define ms(r, c, v) vvs(r, vs(c, v))
#define ml(r, c, v) vvl(r, vl(c, v))
#define mc(r, c, v) vs(r, string(c, v))
#define add(i, j) ((i) + (j)) % mod
#define mul(i, j) ((i) * (j)) % mod
#define bits(n) int(__builtin_popcount(n))

double probtie(const vd &probs) {
	int n = sz(probs);
	vvd dp = md(n + 1, n + 1, 0);
	double ans = 0;

	dp[0][0] = 1;
	rep(i, 0, n) {
		rep(j, 0, n - i) {
			dp[i + 1][j] += dp[i][j] * probs[i + j];
			dp[i][j + 1] += dp[i][j] * (1 - probs[i + j]);
		}
	}

	return dp[n / 2][n / 2];
}

int main() {
	int T, n, k;
	cin >> T;
	rep(X, 1, T + 1) {
		cin >> n >> k;
		vd prob(n);
		double ans = 0;
		irep(p, prob)
			cin >> p;

		sort(all(prob));

		rep(i, 0, k + 1) {
			vd test;
			rep(j, 0, i)
				test.pb(prob[j]);
			rep(j, 1, k - i + 1)
				test.pb(prob[n - j]);
			ans = max(ans, probtie(test));
		}

		printf("Case #%d: %lf\n", X, ans);
	}
}
