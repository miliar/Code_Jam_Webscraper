#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

double P[105];
int N, K;

double compute(vector<double> v){
	double dp[205][205];
	rep(i,0,K+1)
	rep(j,0,K+1)
		dp[i][j]=0;
	dp[0][0]=1;
	rep(i,0,v.size()){
		rep(j,0,K+1){
			dp[i+1][j] += v[i]*dp[i][j];
			dp[i+1][j+1] += (1-v[i])*dp[i][j];
		}
	}
	return dp[K][K/2];
}

void solve(){
	scanf("%d%d", &N, &K);
	rep(i,0,N)
		scanf("%lf", P+i);
	sort(P, P+N);
	double ans=0;
	rep(lo,0,K+1){
		vector<double> chosen;
		rep(i,0,lo)
			chosen.push_back(P[i]);
		rep(i,N-K+lo,N)
			chosen.push_back(P[i]);
		double res=compute(chosen);
		if(res > ans)
			ans=res;
	}
	printf("%.7lf\n", ans);
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i=1; i <= T; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}
