#include <bits/stdc++.h>
using namespace std;

const int MaxC = (int)1e9 + 7;
template<class T> class Flow{//f[i] <-> f[i][j] , c[i] <-> c[i][j]
public:
	struct Edge{
		int from, next, capicity, flow;
		T price;
		
		Edge(){}
		Edge(int x, int y, int c, T pri){
			from = x; next = y; capicity = c; flow = 0; price = pri; 
		}
	};
	int source, sink,cnt,V,E;				
	vector<Edge> edge; vector<int> v;
	vector< vector<int> > a;
	/**/vector<bool> inqueue; vector<T> dist; T cost;//*/
	Flow(){
		cnt=V=E=0; cost = 0; 
		edge.clear(); v.clear(); a.clear();
		/**/inqueue.clear(); dist.clear();//*/
	}		
	int addv() { 
		v.push_back(-1); a.resize(V+1);
		inqueue.push_back(false); dist.push_back(-1); 
		return V++; 
	}
	void adde(int x , int y , int c1 , int c2 = 0 , int price = 0/*option*/){
		edge.push_back( Edge(x,y,c1,price) ); a[x].push_back(E++);
		edge.push_back( Edge(y,x,c2,price) ); a[y].push_back(E++);	
	}
	int MaxFlowDFS(int i, int k = MaxC){ //find via dfs
		v[i] = -1;
		if (i == sink) return k;
		for( vector<int>::iterator p = a[i].begin(); p!=a[i].end(); ++p)
		if ( !v[ edge[*p].next ] && edge[*p].flow < edge[*p].capicity ){
			 int t = edge[*p].capicity - edge[*p].flow;
			 t = min(t , k);
			 t = min(t , MaxFlowDFS(edge[*p].next,t) );
			 if (t > 0){
				 edge[*p].flow += t;
				 edge[*p ^ 1].flow -= t;
				 return t;
			 }
		}
		return 0;
	}	
	int maxflow(){
		int k; do {fill(v.begin(), v.end(), 0); k=MaxFlowDFS(source); cnt += k;} while (k);
		return cnt;
	}
};

const int limit = 1000 + 5;
int a[limit][limit];
int din[limit][limit], dout[limit][limit];

int main(){
	freopen("file.inp","r",stdin);
	//freopen("data.txt","w",stdout);
	int test; scanf("%d",&test);
	for(int T = 1; T <= test; ++T){
		printf("Case #%d: ",T);
		
		int m,n,k;
		memset(a, 0, sizeof a);
		scanf("%d%d%d",&m,&n,&k);
		
		while (k--){
			int lr,hr,lc,hc;
			scanf("%d%d%d%d",&lr,&lc,&hr,&hc);
			for(int i = lr; i <= hr; ++i)
			for(int j = lc; j <= hc; ++j) a[i][j] = 1;
		}
		
		auto g = new Flow<int>;
		
		g->source = g->addv();
		for(int i = 0; i < m; ++i)
		for(int j = 0; j < n; ++j) {
			din[i][j] = g->addv();
			dout[i][j] = g->addv();
			g->adde(din[i][j], dout[i][j],1,0);
		}
		g->sink = g->addv();
		
		for(int i = 0; i < m; ++i)
			if (!a[i][0]) g->adde(g->source, din[i][0], 1);
			
		for(int i = 0; i < m; ++i)
		for(int j = 0; j < n; ++j) if (!a[i][j]) {
			if (j+1 < n && !a[i][j+1]) {
				g->adde(dout[i][j], din[i][j+1], 1);
				g->adde(dout[i][j+1], din[i][j], 1);
			}
			if (i+1 < m && !a[i+1][j]) {
				g->adde(dout[i][j], din[i+1][j], 1);
				g->adde(dout[i+1][j], din[i][j], 1);
			}
		}
		
		for(int i = 0; i < m; ++i)
			if (!a[i][n-1]) g->adde(dout[i][n-1],g->sink,1,0);
		
		printf("%d\n",g->maxflow());
		
	}

}