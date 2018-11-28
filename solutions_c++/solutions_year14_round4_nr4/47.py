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

int M,N;
string s[1010];
vector<string> v[5];
int maxi, ways;

void dfs(int cur){
	if(cur == M){
		int sum = 0;
		rep(i,N){
			if(sz(v[i]) == 0)return;
			set<string> S;
			rep(j,sz(v[i])){
				rep(k,sz(v[i][j])+1){
					S.insert(v[i][j].substr(0,k));
				}
			}
			sum += sz(S);
		}
		if(sum > maxi){
			maxi = sum;
			ways = 0;
		}
		if(sum == maxi)ways++;
		return;
	}
	rep(i,N){
		v[i].pb(s[cur]);
		dfs(cur + 1);
		v[i].pop_back();
	}
}

void main2(){
	cin>>M>>N;
	rep(i,M){
		cin>>s[i];
	}
	maxi = -1, ways = 0;
	dfs(0);
	cout<<maxi<<" "<<ways<<endl;
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
