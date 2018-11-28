#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

typedef double R;

int TC;
int N, K;

R p[210];
R dp[210][110];

int main() {
    scanf("%d", &TC);

    for (int tc = 1; tc <= TC; ++tc) {
	scanf("%d %d", &N, &K);

	rep(i, N) scanf("%lf", &p[i]);
	sort(p, p + N);

	double ret = 0.0;
	for (int i = 0; i <= K; ++i) { //left
	    vector<R> u;
	    for (int j = 0; j < i; ++j) u.pb(p[j]);

	    int id = N - 1;
	    while (u.size() < K) u.pb(p[id--]);

	    rep(j, 210) rep(k, 110) dp[j][k] = 0.0;
	    dp[0][0] = 1.0;

	    rep(j, K) {
		rep(k, 110) {
		    R t = dp[j][k] * (1.0 - u[j]);
		    if (k > 0) t += dp[j][k - 1] * u[j];
		    dp[j + 1][k] = t;
		}
	    }
	    ret = max(ret, dp[K][K / 2]);
	}

	printf("Case #%d: %.8f\n", tc, ret);

    }

    return 0;
}
