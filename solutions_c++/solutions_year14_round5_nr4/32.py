#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
vector<int> way[82][82];
bool ro[82][82][82][82];
vector<int> gr[82];
//pint dp[82][82][82][82][2];
int co[82],to[82];
int inf=100000000,N;
inline int cal(int a,int b,int c,int d,int e){
	int f=0,g=0,ret=-inf;
	if(e==1) ret=-ret;
	rep(j,gr[b].size()){
		int x=gr[b][j];
		if(ro[a][b][b][x] || ro[c][d][b][x]) continue;
		f=1;
		if(e==0) ret=max(ret,cal(a,x,c,d,1));
	}
	rep(j,gr[d].size()){
		int x=gr[d][j];
		if(ro[a][b][d][x] || ro[c][d][d][x]) continue;
		g=1;
		if(e==1) ret=min(ret,cal(a,b,c,x,0));
	}
	if(f<1 && g<1){
		ret=0;
		vector<int> v=way[a][b],w=way[c][d];
		int n=v.size(),m=w.size();
		rep(j,N) to[j]=1;
		rep(j,max(n,m)){
			if(j<n && to[v][j]){ret+=co[v[j]];to[v[j]]=0;}
			if(j<m && to[w][j]){ret-=co[w[j]];to[w[j]]=0;}
		}
		//cerr<<a<<b<<c<<d<<' '<<ret<<endl;
		return ret;
	}
	if(f<1 && e==0) ret=max(ret,cal(a,b,c,d,1));
	if(g<1 && e==1) ret=min(ret,cal(a,b,c,d,0));
	//cerr<<a<<b<<c<<d<<' '<<ret<<endl;
	return ret;
}
int main()
{
	int t,n,a;
	cin>>t;
	rep(i,t){
		cerr<<i<<endl;
		cin>>n;N=n;
		rep(j,82) gr[j].clear();
		rep(j,82) rep(k,82) way[j][k].clear();
		//rep(j,n+2) rep(k,n+2) rep(l,n+2) rep(m,n+2) ro[j][k][l][m]=false;
		//rep(j,n+2) rep(k,n+2) rep(l,n+2) rep(m,n+2) dp[j][k][l][m]=mp(inf,inf);
		rep(j,n) cin>>co[j];
		rep(j,n-1){
			cin>>a;a--;gr[a].pb(j);gr[j].pb(a);
		}
		rep(j,n){
			queue<vector<int> > q;
			vector<int> v;v.pb(j);way[j][j]=v;q.push(v);
			while(!q.empty()){
				v=q.front();q.pop();
				int x=v[v.size()-1];
				rep(k,gr[x].size()){
					int y=gr[x][k];
					if(way[j][y].size()) continue;
					way[j][y]=v;way[j][y].pb(y);q.push(way[j][y]);
				}
			}
		}
		/*rep(j,n) rep(k,n){
			cerr<<j<<' '<<k<<endl;
			rep(l,way[j][k].size()) cerr<<way[j][k][l]<<endl;
		}*/
		rep(j,n) rep(k,n) rep(l,way[j][k].size()-1){
			int x=way[j][k][l],y=way[j][k][l+1];
			ro[j][k][x][y]=ro[j][k][y][x]=true;
		}
		int out=-inf;
		rep(j,n){
			int ret=inf;
			rep(k,n) ret=min(ret,cal(j,j,k,k,0));
			out=max(out,ret);
		}
		printf("Case #%d: %d\n",i+1,out);
		rep(j,n) rep(k,n) rep(l,way[j][k].size()-1){
			int x=way[j][k][l],y=way[j][k][l+1];
			ro[j][k][x][y]=ro[j][k][y][x]=false;
		}
	}
}
