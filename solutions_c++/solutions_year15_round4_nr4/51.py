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
double eps = 10e-10;
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

int main() {
	int T, r, c;
	cin >> T;
	rep(X, 0, T) {
		cin >> r >> c;
		vvl ans = ml(r + 5, 15, 0);
		ans[0][1] = 1;

		rep(i, 3, r + 5) {
			ans[i][1] = add(ans[i][1], ans[i - 3][1]);
			ans[i][3] = add(ans[i][3], ans[i - 3][3]);
			ans[i][4] = add(ans[i][4], ans[i - 3][4]);
			ans[i][6] = add(ans[i][6], ans[i - 3][6]);
			ans[i][12] = add(ans[i][12], ans[i - 3][12]);
			if (i >= 4 && c % 3 == 0) {
				ans[i][3] = add(ans[i][3], ans[i - 4][1]);
				ans[i][3] = add(ans[i][3], mul(ans[i - 4][3], 3));
				ans[i][12] = add(ans[i][12], ans[i - 4][4]);
				ans[i][6] = add(ans[i][6], mul(ans[i - 4][6], 3));
				ans[i][12] = add(ans[i][12], mul(ans[i - 4][12], 3));
			}
			if (i >= 4 && c % 6 == 0) {
				ans[i][6] = add(ans[i][6], ans[i - 4][1]);
				ans[i][6] = add(ans[i][6], mul(ans[i - 4][3], 3));
				ans[i][12] = add(ans[i][12], mul(ans[i - 4][4], 2));
				ans[i][6] = add(ans[i][6], mul(ans[i - 4][6], 6));
				ans[i][12] = add(ans[i][12], mul(ans[i - 4][12], 6));
			}
			if (i >= 5 && c % 4 == 0) {
				ans[i][4] = add(ans[i][4], ans[i - 5][1]);
				ans[i][12] = add(ans[i][12], ans[i - 5][3]);
				ans[i][4] = add(ans[i][4], mul(ans[i - 5][4], 4));
				ans[i][12] = add(ans[i][12], mul(ans[i - 5][6], 2));
				ans[i][12] = add(ans[i][12], mul(ans[i - 5][12], 4));
			}
		}

		ll bigans = 2 * (ans[r][1] + ans[r][3] + ans[r][4] + ans[r][6] + ans[r][12]) +
			ans[r + 2][1] + ans[r + 2][3] + ans[r + 2][4] + ans[r + 2][6] + ans[r + 2][12] +
			ans[r - 2][1] + ans[r - 2][3] + ans[r - 2][4] + ans[r - 2][6] + ans[r - 2][12];

		printf("Case #%d: %lld\n", X + 1, bigans % mod);
	}
}
