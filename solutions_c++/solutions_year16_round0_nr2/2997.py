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
#define MAX 111
#define MOD 1000000007

int n;
char s[MAX];

int solve() {
	int res = 0;
	n = strlen(s);
	rep(i, n) s[i] = (s[i] == '+') ? 0 : 1;
	int st = n - 1;
	if (s[st] == 1) res++;
	while (true) {
		int i = st;
		while (i >= 0 && s[i] == s[st]) i--;
		if (i < 0) {
			return res;
		}
		st = i;
		res++;
	}
}

int main() {
	ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("test.inp", "r", stdin);
		freopen("test.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		scanf(" %s ", s);
		printf("Case #%d: %d\n", ++caseNo, solve());
	}
	return 0;
}

