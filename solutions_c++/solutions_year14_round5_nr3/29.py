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

int N,m;
char c[1010];
int a[1010];

int dp[16][1<<15][16];

int f(int cur,int mask,int other){
	int& res = dp[cur][mask][other];
	if(res != -1)return res;
	res = -2;

	if(cur == N){
		return res = __builtin_popcount(mask) + other;
	}

	if(c[cur] == 'E'){
		if(a[cur] == -1){
			rep(i,m)if(!(mask >> i & 1)){
				int res2 = f(cur+1, mask | (1<<i), other);
				if(res2 != -2){
					return res = res2;
				}
			}
			int res2 = f(cur+1, mask, other+1);
			if(res2 != -2){
				return res = res2;
			}
		}else{
			if(mask >> a[cur] & 1){
				return res = -2;
			}
			return res = f(cur+1,mask | (1<<a[cur]),other);
		}
	}
	else{
		if(a[cur] == -1){
			rep(i,m)if((mask >> i & 1)){
				int res2 = f(cur+1, mask ^ (1<<i), other);
				if(res2 != -2){
					return res = res2;
				}
			}
			if(other >= 1){
				int res2 = f(cur+1, mask, other-1);
				if(res2 != -2){
					return res = res2;
				}
			}
		}else{
			if(!(mask >> a[cur] & 1)){
				return res = -2;
			}
			return res = f(cur+1,mask ^ (1<<a[cur]),other);
		}
	}

	return res;
}

void main2(){
	cin>>N;
	rep(i,N)cin>>c[i]>>a[i];
	map<int,int> ZIP;
	ZIP[0] = -1;
	rep(i,N){
		if(ZIP.find(a[i]) == ZIP.end()){
			int sz = sz(ZIP);
			ZIP[a[i]] = sz - 1;
		}
		a[i] = ZIP[a[i]];
	}
	m = sz(ZIP) - 1;
	vector<int> masks[16];
	rep(mask,1<<m){
		masks[__builtin_popcount(mask)].pb(mask);
	}
	memset(dp,-1,sizeof(dp));
	rep(i,m+1)rep(j,sz(masks[i]))rep(k,N+1){
		int res = f(0,masks[i][j],k);
		if(res != -2){
			cout<<res<<endl;
			return;
		}
	}
	cout<<"CRIME TIME"<<endl;	
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
