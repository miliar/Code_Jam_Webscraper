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


const int MAX_V=8;
int V;				//substitute!!
vector<int> G[MAX_V];
int match[MAX_V];
bool used[MAX_V];
void init(){
	rep(i,MAX_V) G[i].clear(); 
}
void add_edge(int u,int v){
	G[u].push_back(v);
	G[v].push_back(u);
}
bool dfs(int v){
	used[v]=true;
	rep(i,G[v].size()){
		int u=G[v][i],w=match[u];
		if(w<0 || (!used[w] && dfs(w))){
			match[v]=u;
			match[u]=v;
			return true;
		}
	}
	return false;
}
int nibu(){
	int res=0;
	memset(match,-1,sizeof(match));
	rep(v,V){
		if(match[v]<0){
			memset(used,0,sizeof(used));
			if(dfs(v)) res++;
		}
	}
	return res;
}

bool B(int x,int i){return (x>>i)&1;}
bool can[4][1<<16];
int inf=16;
int dp[4][1<<16];

void precalc(int N){
	V=N*2;
	rep(i,1<<(N*N)){
		bool a[4][4]={};
		bool intr=0;
		rep(j,N) rep(k,N) if(B(i,j*N+k)) a[j][k]=1;
		rep(j,N){	//kill j
			init();
			vector<int> ws;
			rep(k,N) if(a[j][k]) ws.pb(k);
			rep(k,N) if(k!=j){
				rep(l,ws.size()) if(a[k][ws[l]]) add_edge(k,N+ws[l]);
			}
			int tmp=nibu();
			if(tmp==ws.size()){
				intr=1;
				break;
			}
		}
		can[N-1][i]=!intr;
	}
	rep(i,1<<(N*N)){
		if(!can[N-1][i]) dp[N-1][i]=inf;
	}
	for(int i=(1<<(N*N))-1;i>=0;i--){
		rep(j,N*N) if(!B(i,j)) chmin(dp[N-1][i],dp[N-1][i|(1<<j)]+1);
	}
}

int N;
string s[4];
int solve(){
	cin>>N;
	rep(i,N) cin>>s[i];
	int I=0;
	rep(i,N) rep(j,N) if(s[i][j]=='1') I|=(1<<(i*N+j));
	return dp[N-1][I];
}
int main(){
	rep(i,4) precalc(i+1);
	int T;
	cin>>T;
	rep1(tt,T){
		printf("Case #%d: %d\n",tt,solve());
	}
}
