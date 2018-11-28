// lamphanviet@gmail.com
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
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
#define MAX 233
#define MOD 1000000007

int n, k;
double b[MAX], p[MAX][MAX];

double check(vector<double> a) {
	if ((int)a.size() != k) {
		puts("failed");
		return 0;
	}

	//rep(i, k) printf("%lf ", a[i]); puts("");

	p[0][0] = 1.0 - a[0];
	p[0][1] = a[0];
	fr(i, 1, k - 1) fr(j, 0, k / 2) {
		p[i][j] = 0.0;
		if (i + 1 < j) continue;

		if (i >= j) p[i][j] += p[i - 1][j] * (1.0 - a[i]);
		p[i][j] += p[i - 1][j - 1] * a[i];
	}

	rep(i, k) {
		//fr(j, 0, k / 2) printf("%.2lf ", p[i][j]);
		//puts("");
	}

	return p[k - 1][k / 2];
}

double solve() {
	double res = 0.0;

	sort(b, b + n);

	fr(i, 0, k) {
		vector<double> a;
		rep(j, i) a.pb(b[j]);
		int m = k - i, j = n - 1;
		while (m-- > 0) {
			a.pb(b[j]);
			j--;
		}
		res = max(res, check(a));
	}

	return res;
}

int main() {
	//ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("blarge.inp", "r", stdin);
		freopen("blarge.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		scanf("%d %d", &n, &k);
		rep(i, n) scanf("%lf", &b[i]);
		printf("Case #%d: %.12lf\n", ++caseNo, solve());
	}
	return 0;
}

