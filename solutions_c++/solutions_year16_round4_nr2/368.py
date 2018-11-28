#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define MP make_pair
#define PB push_back

using namespace std;

using ll = long long;

int read(){
	int i;
	scanf("%d",&i);
	return i;
}

const int Nmax=200;

int n,k;
double p[Nmax];

void Input(){
	n=read(),k=read();
	REP(i,n)
		scanf("%lf",p+i);
}

double dp[Nmax+1];

void Solve(){
	double ans=0;
	sort(p,p+n);
	for(int i=0;i<=k;i++){
		fill(dp,dp+k+1,0.0);
		dp[0]=1;
		REP(s,i){
			double x=p[s];
			for(int j=k/2;j>0;j--)
				dp[j]=dp[j]*(1.0-x)+dp[j-1]*x;
			dp[0]*=(1.0-x);
		}
		FOR(s,n-k+i,n){
			double x=p[s];
			for(int j=k/2;j>0;j--)
				dp[j]=dp[j]*(1.0-x)+dp[j-1]*x;
			dp[0]*=(1.0-x);
		}
		ans=max(ans,dp[k/2]);
	}
	printf("%.10f\n",ans);
}

int main(){
	int t=read();
	REP(caseNumber,t){
		Input();
		printf("Case #%d: ",caseNumber+1);
		Solve();
	}
}