//nathanajah's template
//28-11-2012
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <map>
#include <ctime>
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define LL long long
#define ULL unsigned LL
#define INF 0x3FFFFFFF
#define INFLL 0x3FFFFFFFFFFFFFFF
#define SZ(a) (int)(a).size()
#define ALL(a) (a).begin(),(a).end()
#ifdef DEBUG
	#define debug(...) \
	fprintf(stderr,__VA_ARGS__)
#else
	#define debug(...) 
#endif
using namespace std;

inline string GetString()
{
	char GS[1000005];
	scanf("%s",GS);string ret=GS;
	return ret;
}

inline char getc()
{
	char c=' ';
	while (c==' ' || c=='\t' || c=='\r' || c=='\n')
		c=getchar();
	return c;
}
//ENDOFTEMPLATE

struct Edge {
	int cap,flow,to,rev,from;
	Edge(int _from, int _to, int _flow, int _cap, int _rev) {
		from = _from;
		to = _to;
		flow = _flow;
		cap = _cap;
		rev = _rev;
	}
};

struct FlowGraph {
	vector <vector<Edge> > adj;
	vector <Edge*> prev;
	int n;
	void clear() {
		prev.clear();
		adj.clear();
	}
	void clearFlow() {
		int i,j;
		for (i=0;i<SZ(adj);++i)
			for (j=0;j<SZ(adj[i]);++j)
				adj[i][j].flow = 0;
	}
	FlowGraph(int new_n) {
		adj.resize(new_n);
		prev.resize(new_n);
		n = new_n;
	}
	void addEdge(int v1, int v2, int w) {
		adj[v1].push_back(Edge(v1,v2,0,w,adj[v2].size()));
		adj[v2].push_back(Edge(v2,v1,0,0,adj[v1].size()-1));
	}
	LL blockingFlow(int source, int sink) {
		fill(prev.begin(),prev.end(),(Edge*)NULL);
		prev[source] = (Edge*)1;
		queue <int> bfs;
		bfs.push(source);
		while (!bfs.empty()){
			int now = bfs.front();bfs.pop();
			for (int i = 0; i < SZ(adj[now]);++i) {
				Edge &x = adj[now][i];
				if (prev[x.to]==NULL && x.cap - x.flow > 0) {
					prev[x.to] = &x;
					bfs.push(x.to);
				}
			}
		}
		if (prev[sink] == NULL) return 0;
		LL flow = 0;
		for (int i = 0; i < SZ(adj[sink]); i++) {
			LL fnow = 1000000000000000000LL;
			Edge* now = &adj[adj[sink][i].to][adj[sink][i].rev];
			while (now != prev[source]) {
				if (now==NULL) { fnow = 0; break;}
				fnow = min(fnow,(LL)( now->cap - now->flow));
				now = prev[now->from];
			}
			if (fnow==0)
				continue;
			now = &adj[adj[sink][i].to][adj[sink][i].rev];
			while (now!=prev[source]) {
				now->flow += fnow;
				adj[now->to][now->rev].flow -= fnow;
				now = prev[now->from];
			}
			flow += fnow;
		}
		return flow;
	}
	
	LL maxflow(int s, int t) {
		LL res = 0;
		while (LL flow = blockingFlow(s,t))
			res += flow;
		return res;
	}
	
	void transfer(vector <vector<LL> > &array) {
		array.clear();
		int i,j;
		array.resize(n);
		for (i = 0; i < n; i++) {
			array[i].resize(n);
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < SZ(adj[i]); ++j) {
				array[adj[i][j].from][adj[i][j].to] += adj[i][j].flow;
			}
		}
	}
	
	void transfer (map <pair<LL,LL>,LL> &array) {
		array.clear();
		int i,j;
		for (i = 0; i < n; i++) {
			for (j = 0; j < SZ(adj[i]); ++j) 
				if (adj[i][j].flow > 0)
					array[make_pair(adj[i][j].from,adj[i][j].to)] = adj[i][j].flow;
		}
	}
};

int n,m,i,j,k;
int b;
bool occup[600][600];
int t;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int getNum(int x, int y) {
	return m*x + y;
}
int main()
{
	scanf("%d",&t);
	int cs = 0;
	while (t--) {
		int xx0,xx1, yy0, yy1;
		scanf("%d %d %d",&n,&m,&b);
		memset(occup,0,sizeof(occup));
		while (b--) {
			scanf("%d %d %d %d",&xx0, &yy0, &xx1, &yy1);
			for (i=xx0; i<=xx1; i++)
				for (j=yy0; j<=yy1; j++)
					occup[i][j] = true;
		}
		FlowGraph g = FlowGraph(2*n*m+2);
		for (i=0;i<n;++i)
			for (j=0;j<m;++j) {
				for (k=0;k<4;++k) {
					if (i+dx[k] >=0 && i+dx[k] <n && j+dy[k]>=0 && j+dy[k] < m) {
						g.addEdge(getNum(i,j) + n*m + 2, getNum(i+dx[k], j+dy[k]) + 2,1);
					}
				}
			}
		for (i=0;i<n;++i)
			for (j=0;j<m;++j)
				if (!occup[i][j])
					g.addEdge(getNum(i,j) + 2, getNum(i,j) + n*m + 2,1);
		for (i=0;i<n;++i) {
			g.addEdge(0,getNum(i,0) + 2,1);
			g.addEdge(getNum(i,m-1) + n*m + 2, 1,1);
		}
		printf("Case #%d: %I64d\n",++cs, g.maxflow(0,1));
	}
}
