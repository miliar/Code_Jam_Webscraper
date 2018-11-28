// Enjoy your stay.

#include <bits/stdc++.h>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(auto it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define mt make_tuple
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)(x).size())

using namespace std;

typedef istringstream iss;
typedef long long ll;
typedef pair<ll,ll> pi;
typedef stringstream sst;
typedef vector<ll> vi;

int P,Q,N;
int H[111],G[111];

int dp[111][1111];

int f(int cur,int left){
	int& res = dp[cur][left];
	if(res != -1)return res;
	res = 0;
	if(cur == N) return res = 0;

	int q, r;
	if(H[cur] % Q == 0){
		q = H[cur] / Q - 1;
		r = Q;
	}else{
		q = H[cur] / Q;
		r = H[cur] % Q;
	}

	int need = (r + P - 1) / P;
	res = max(res, f(cur+1, left + q + 1));
	int nleft = left + q - need;
	if(nleft >= 0){
		res = max(res, G[cur] + f(cur+1, nleft));
	}
	return res;
}

void main2(){
	cin>>P>>Q>>N;
	rep(i,N)cin>>H[i]>>G[i];
	memset(dp,-1,sizeof(dp));
	cout<<f(0,1)<<endl;
}

int main(){
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	
	
	
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		main2();
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
