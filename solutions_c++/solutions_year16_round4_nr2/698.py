#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep1(i,n) for(int i=1;i<=(int)(n);i++)
#define all(c) c.begin(),c.end()
#define pb push_back
#define fs first
#define sc second
#define show(x) cout << #x << " = " << x << endl
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)
using namespace std;
template<class S,class T> ostream& operator<<(ostream& o,const pair<S,T> &p){return o<<"("<<p.fs<<","<<p.sc<<")";}
template<class T> ostream& operator<<(ostream& o,const vector<T> &vc){o<<"sz = "<<vc.size()<<endl<<"[";for(const T& v:vc) o<<v<<",";o<<"]";return o;}
bool B(int x,int i){return (x>>i)&1;}
double solve(){
	int N,K;
	double p[16];
	cin>>N>>K;
	rep(i,N) cin>>p[i];
	double ans=0;
	rep(i,1<<N){
		int c=0;
		rep(j,N) if(B(i,j)) c++;
		if(c!=K) continue;
		double dp[17][17]={};
		dp[0][0]=1;
		int J=0;
		rep(j,N) if(B(i,j)){
			rep(k,K+1){
				if(k!=K) dp[J+1][k+1]+=dp[J][k]*p[j];
				dp[J+1][k]+=dp[J][k]*(1-p[j]);
			}
			J++;
		}
		chmax(ans,dp[K][K/2]);
	}
	return ans;
}
int main(){
	int T;
	cin>>T;
	rep1(tt,T){
		printf("Case #%d: %.12f\n",tt,solve());
	}
}
