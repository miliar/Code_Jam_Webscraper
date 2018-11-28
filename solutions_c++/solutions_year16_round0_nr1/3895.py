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

const int MX = 1005;

const int MOD = 1000000007;

int solve(int n)
{
	if (!n) return -1;
	bool d[10] = {false};
	bool ok = true;
	int x = 1;
	while (ok) {
		ok = false;
		ll N = (ll)x*n;
		while (N) {
			d[N%10] = true;
			N /= 10;
		}
		FOR(i,0,10) if (!d[i]) { ok = true; break; }
		if (!ok) return (ll)x*n;
		++x;
	}
	return 0;
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

	int T,n;
	cin >> T;
	FOR(testcase,1,T+1) {
		cin >> n;
		int res = solve(n);
		if (res == -1) cout << "Case #" << testcase << ": INSOMNIA" << endl;
		else cout << "Case #" << testcase << ": " << res << endl;
	}
	return 0;
}
