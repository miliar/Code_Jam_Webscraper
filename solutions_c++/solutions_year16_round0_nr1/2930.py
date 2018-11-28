// lamphanviet@gmail.com
#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define ull unsigned long long
#define ll long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define EPS 1e-7
#define MAX 100111
#define MOD 1000000007

ll solve(int n) {
	if (n == 0) return -1;
	int v = 0;
	fr(i, 1, 1000000) {
		ll m = n * 1LL * i;
		while (m > 0) {
			v |= (1 << (m % 10));
			m /= 10;
		}
		if (v == 1023) return n * 1LL * i;
	}
	return -1;
}

int main() {
	//ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("test.inp", "r", stdin);
		freopen("test.out", "w", stdout);
	#endif
	int cases, caseNo = 0, n;
	for (scanf("%d", &cases); cases--; ) {
		scanf("%d", &n);
		printf("Case #%d: ", ++caseNo);
		ll res = solve(n);
		if (res < 0) puts("INSOMNIA");
		else cout << res << endl;
	}
	return 0;
}

