#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	tr(c,i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())
#define	endl			'\n'

typedef long long		ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>		vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>		vpii;

const int MX = 101;

int dp[MX][2];

const int MOD = 1000000007;

static ll fastPow(ll n, int k)
{
	ll p = 1;
	while (k > 0) {
		if (k&1)
			p *= n;
		n = n*n;
		k >>= 1;
	}
	return p;
}

void solve(int n, int J, ostream &cout)
{
	FOR(x,0,1<<(n-2)) {
		ll y = 1<<(n-1) | (x<<1) | 1;
		bool ok = true;
		ll v[10];
		ll Z;
		FOR(b,2,11) {
			ll z = 0;
			FOR(i,0,n) if ((1<<i)&y) z += fastPow(b,i);
			Z = z;
			bool found = false;
			for (ll d = 2; d*d <= z; ++d) {
				if (z%d == 0) {
					v[b-2] = d;
					found = true;
					break;
				}
			}
			if (!found) {
				ok = false;
				break;
			}
		}
		if (!ok) continue;
		if (!J) return;
		--J;
		cout << Z << " ";
		FOR(i,0,9) cout << v[i] << " ";
		cout << endl;
	}
}

int main(int argc, char *argv[])
{
#ifndef ONLINE_JUDGE
	freopen(argv[1],"r",stdin);
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	ios :: sync_with_stdio(false);
	cin.tie(NULL);

	int T,n,j;
	cin >> T;
	FOR(testcase,1,T+1) {
		cin >> n >> j;
		cout << "Case #" << testcase << ":\n";
		solve(n,j,cout);
	}
	return 0;
}
