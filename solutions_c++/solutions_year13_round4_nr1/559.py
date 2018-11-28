// .... .... .....!
// P..... C.....!

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cassert>

#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

#include <cstdio>
#include <cstring>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define fch(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define sz(x) (int((x).size()))
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()

typedef long long ll;
typedef pair <int, int> pii;

////////////////////////////////////////////////////////////////////////////////

const int mod = 1000002013;

const int maxm = 1000 + 100;

ll n;
int m;
ll l[maxm], r[maxm], p[maxm];
ll c[2*maxm];
ll f[2*maxm];

int main()
{
	ios::sync_with_stdio (false);

	int ttt, ttc = 1;
	for (cin >> ttt; ttc <= ttt; ttc++)
	{
		cin >> n >> m;
		rep (i, m) cin >> l[i] >> r[i] >> p[i], c[2*i] = l[i], c[2*i+1] = r[i];

		sort (c, c+2*m);
		int k = unique (c, c+2*m) - c;
		memset (f, 0, sizeof f);

		rep (i, m) rep (j, k-1) if (c[j] >= l[i] && c[j+1] <= r[i]) f[j] += p[i];
		rep (j, k) f[j] %= mod;

		ll ans = 0;

		while (1)
		{
			int pos = -1;
			rep (i, k) if (f[i]) { pos = i; break; }
			if (pos == -1) break;

			ll minf = 1LL<<61;
			int end = pos;
			while (f[end]) minf = min (minf, f[end]), end++;

			ll len = c[end] - c[pos];
			ans += (len*n - len * (len-1) / 2) % mod * minf % mod;
			ans %= mod;

//			cerr << " ## " << c[pos] << ' ' << c[end] << ' ' << minf << endl;

			fer (i, pos, end)
				f[i] -= minf;
		}

		ans = (-ans + mod) % mod;
		rep (i, m) ans = (ans + ( n * (r[i]-l[i]) - (r[i]-l[i]) * (r[i]-l[i]-1) / 2 ) % mod * p[i]) % mod;

		cout << "Case #" << ttc << ": " << ans << endl;
	}

	{ int _; cin >> _; return 0; }
}
