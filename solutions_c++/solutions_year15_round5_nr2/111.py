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

int main() {
	int T, n, k;
	cin >> T;
	rep(X, 0, T) {
		cin >> n >> k;
		vi avg(n - k + 1);
		irep(a, avg) {
			cin >> a;
		}
		vi mn(k), mx(k), diff(k);
		int upshift = 0;
		rep(i, 0, k) {
			int temp = 0;
			for (int j = i; j < n - k; j += k) {
				temp += avg[j + 1] - avg[j];
				mn[i] = min(mn[i], temp);
				mx[i] = max(mx[i], temp);
			}
			diff[i] = mx[i] - mn[i];
			upshift -= mn[i];
		}
		sort(all(diff));
		int d0 = ((avg[0] - upshift) % k + k) % k;

		rep(i, 0, d0) {
			diff[0]++;
			sort(all(diff));
		}
		printf("Case #%d: %d\n", X + 1, diff.back());
	}
}
