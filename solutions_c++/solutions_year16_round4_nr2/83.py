#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 505;

ld in[nax];
ld dp[nax];

void te() {
	int n, k;
	scanf("%d%d", &n, &k);
	REP(i, n) scanf("%Lf", &in[i]);
	sort(in, in + n);
	ld ans = 0;
	REP(a,n) FOR(d, a, n-1) if(a == 0 || d == n - 1)
	FOR(b, a, d) {
		// (b - a + 1) + (d - c + 1) == k
		int c = b - a + 1 + d + 1 - k;
		if(! (b < c && c <= d)) continue;
		REP(i, n + 2) dp[i] = 0;
		dp[0] = 1;
		int cnt = 0;
		REP(ii, n) if((a <= ii && ii <= b) || (c <= ii && ii <= d)) {
			++cnt;
			ld suc = in[ii];
			FORD(i, n, 0) if(dp[i] >= 1e-15) {
				dp[i+1] += dp[i] * suc;
				dp[i] *= (1 - suc);
			}
		}
		if(cnt == k)
			maxi(ans, dp[k/2]);
	}
	printf("%.10Lf\n", ans);
}

int main() {
	int T;
	scanf("%d", &T);
	RI(nr, T) {
		cerr << nr << "\n";
		printf("Case #%d: ", nr);
		te();
	}
	return 0;
}
