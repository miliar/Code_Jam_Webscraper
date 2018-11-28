#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <functional>
#include <bitset>

using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef pair<int, int> PII;


#define FOR(i, x, y) for(ll i=x; i<=y; i++)
#define FORD(i, x, y) for (ll i = x; i >= y; --i)
#define REP(i, n) for(ll i=0; i<n; i++)
#define REPD(i, n) for(ll i = n - 1; i >= 0; --i) 

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define UNIQ(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define SZ(c) (int)(c).size()

#define CLEAR(x) memset(x,0,sizeof x)
#define FILL(x,v) memset(x,v,sizeof x)

#define pb push_back
#define mp make_pair
#define X first
#define Y second



const double eps = 1.0e-11;
const double pi = acos(-1.0);

const int N = 1010;

int n, m;

ll f(ll k) {
	return (2 * n - k + 1) * k / 2;
}

ll o[N], e[N], p[N];
vector<ll> segments, cnt;

ll get(int l, int r) {
	if (l >= r)
		return 0;
	bool ok = true;
	FOR(i, l, r - 1) {
		if (cnt[i])
			ok = false;
	}
	if (ok)
		return 0;

	ll mn = l;
	FOR(i, l, r - 1) {
		if (cnt[mn] > cnt[i])
			mn = i;
	}

	ll sum = f(segments[r] - segments[l]) * cnt[mn];
	ll mm = cnt[mn];
	FOR(i, l, r - 1)
		cnt[i] -= mm;

	sum += get(l, mn);
	sum += get(mn + 1, r);

	return sum;
}

void solve() {
	CLEAR(o);
	CLEAR(e);
	CLEAR(p);
	cin >> n >> m;
	segments.clear(), cnt.clear();
	ll res = 0;
	REP(i, m) {
		cin >> o[i] >> e[i] >> p[i];
		segments.push_back(o[i]);
		segments.push_back(e[i]);
		res += f(e[i] - o[i]) * p[i];
	}
	
	UNIQ(segments);
	FOR(i, 1, SZ(segments) - 1) {
		ll c = 0;
		REP(j, m)
			if (o[j] <= segments[i - 1] && segments[i] <= e[j])
				c += p[j];
		cnt.push_back(c);
	}

	ll sum = get(0, SZ(segments) - 1);
	cout << " " << res - sum << endl;
}

int main() {
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("outputA", "w", stdout);

	int TEST;
	cin >> TEST;

	REP(T, TEST) {
		printf("Case #%lld:", T + 1);
		solve();
	}
	return 0;
}