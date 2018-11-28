#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<queue>
#include<sstream>
#include<ctime>
using namespace std;

typedef long long Int;
#define FOR(i,a,b) for(int i=(a); i<=(b);++i)
#define mp make_pair
#define pb push_back
#define sz(s) (int)((s).size())
const int inf = 1000000000;
const int MOD = 1000000007;
const double pi=acos(-1.0);

template<int maxFlowSize> 
class MaxFlow {
public:
	class Edge {
	public:
		int from, to, upper, flow;
		Edge(int _from, int _to,int _upper) {
			from = _from;
			to = _to;
			upper = _upper;
			flow = 0;
		}
	};

	vector<int> g[maxFlowSize];
	vector<Edge> e;

	void Clear() {
		e.clear();
		// vector<Edge> tmp; tmp.swap(e); // ONLY IF NEEDED
		for(int i=0; i<maxFlowSize; ++i)g[i].clear();
	}

	void addEdge(int from,int to,int upper) {
		Edge e1 = Edge(from, to, upper);
		Edge e2 = Edge(to, from, 0);
		g[from].push_back(e.size());e.push_back(e1);
		g[to].push_back(e.size());e.push_back(e2);
	}

	int source, sink; // be sure you set up these values

	int d[maxFlowSize];
	int q[maxFlowSize];
private: bool bfs() {
			 memset(d,63,sizeof(d));
			 int qh=0,qt=0;
			 d[source]=0;
			 q[qt++]=source;
			 while(qh<qt) {
				 int v=q[qh++];
				 for(int i=0;i<g[v].size();++i) {
					 int eid = g[v][i];
					 if(e[eid].flow<e[eid].upper) {
						 int to = e[eid].to;
						 if(d[to]>d[v]+1) {
							 d[to]=d[v]+1;
							 q[qt++]=to;
						 }
					 }
				 }
			 }
			 return d[sink]<maxFlowSize+1;
		 }


private:
	int ptr[maxFlowSize];
	int dfs(int v,int cur) {
		if(cur==0 || v==sink)return cur;
		for(;ptr[v]<g[v].size();++ptr[v]) {
			int eid = g[v][ptr[v]];
			int to = e[eid].to;
			if(d[to]!=d[v]+1)continue;
			int add = dfs(to, min(cur, e[eid].upper-e[eid].flow));
			if(add) {
				e[eid].flow+=add;
				e[eid^1].flow-=add;
				return add;
			}
		}
		return 0;
	}
public: int getMaxFlow() {
			int ans=0;
			for(;;) {
				if(!bfs())break;
				memset(ptr,0,sizeof(ptr));
				for(;;) {
					int cur = dfs(source, 1000000000);
					ans+=cur;
					if(!cur)break;
				}
			}
			return ans;
		}
};

bool bad[555][555];
MaxFlow<2*505*101> net;
int in[555][555], out[555][555];

int get() {
	int n,m,b;
	cin>>n>>m>>b;
	memset(bad, false, sizeof(bad));
	FOR(i,1,b) {
		int x0, y0, x1, y1;
		cin>>x0>>y0>>x1>>y1;
		FOR(x,x0,x1)FOR(y,y0,y1) bad[x][y]=true;
	}

	FOR(i,0,n-1)FOR(j,0,m-1) {
		in[i][j]=m*i+j+1;
		out[i][j]=in[i][j]+n*m;
	}

	net.Clear();
	net.source=0;
	net.sink=2*n*m+1;
	FOR(i,0,n-1)FOR(j,0,m-1) if(!bad[i][j]) {
		FOR(dx,-1,1)FOR(dy,-1,1) if(abs(dx)+abs(dy)==1){
			int fx=i+dx;
			int fy=j+dy;
			if(fx>=0 && fx<n && fy>=0 && fy<m) {
				if(bad[fx][fy]) continue;
				net.addEdge(out[i][j], in[fx][fy], 1);
			}
		}
		if(j==0) net.addEdge(net.source, in[i][j], 1);
		if(j==m-1) net.addEdge(out[i][j], net.sink, 1);

		net.addEdge(in[i][j], out[i][j], 1);
	}
	return net.getMaxFlow();
}

int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;cin>>t;
	FOR(tt,1,t) {
		cout<<"Case #"<<tt<<": ";
		int ans=get();
		cout<<ans<<endl;
		cerr<<tt<<endl;
	}
}