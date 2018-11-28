#include <bits/stdc++.h>

using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define FOR(i,n) REP(i,0,(int)n-1)
#define mp make_pair
#define ll long long
#define pb push_back
#define pii pair<int,int>
#define VI vector<int>
#define fi first
#define se second
#define pss pair<short int, short int>

double dp[242][242];

double tie(vector<double> &P) {
	int k = P.size();
	//FOR(i,k) cout<<P[i]<<" ";
	//cout<<endl;
	dp[0][0] = 1.0;
	REP(i,1,k) dp[0][i] = 0.0;
	REP(i,1,k) {
		REP(j,0,k) {
			dp[i][j] = (1-P[i-1]) * dp[i-1][j];
			if(j!=0) dp[i][j] += P[i-1] * dp[i-1][j-1];
			//cout<<dp[i][j]<<" ";
		}
		//cout<<endl;
	}
	//cout<<"k k/2 "<<k<<" "<<k/2<<" returning "<<dp[k][k/2]<<"\n";
	return dp[k][k/2];
}

void solve() {
	int n,k;
	cin>>n>>k;
	vector<double> P;
	FOR(i,n) {
		double p;
		cin>>p;
		P.pb(p);
	}
	sort(P.begin(), P.end());
	double res = 0.0;
	FOR(i,k+1) {
		vector<double> kands;
		FOR(j,i) kands.pb(P[j]);
		REP(j,n-(k-i),n-1) kands.pb(P[j]);
		res = max(res, tie(kands));
	}
	cout<<setprecision(20);
	cout<<res<<"\n";
}

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	for(int i=1; i<=t; i++) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}