#include <bits/stdc++.h>
using namespace std;

#define dump(n) cout<<"# "<<#n<<'='<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;

const int INF=1e9;
const int MOD=1e9+7;
const double EPS=1e-9;

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}
template<typename T>
ostream& operator<<(ostream& os,const vector<T>& a){
	os<<'[';
	rep(i,a.size()) os<<(i?" ":"")<<a[i];
	return os<<']';
}

struct Edge{
	int src,dst,flow,capacity,next;
	Edge(){}
	Edge(int s,int d,int f,int c,int n):src(s),dst(d),flow(f),capacity(c),next(n){}
};

void AddEdge(vector<Edge>& es,vi& head,int src,int dst,int flow,int capacity)
{
	es.push_back(Edge(src,dst,flow,capacity,head[src]));
	head[src]=es.size()-1;
}

vi BFS(const vector<Edge>& es,const vi& head,int begin)
{
	int size=head.size();
	vi label(size,size);
	queue<pii> q;
	q.push(mp(begin,0));
	while(q.size()){
		pii cur=q.front(); q.pop();
		if(label[cur.first]<=cur.second)
			continue;
		label[cur.first]=cur.second;
		for(int i=head[cur.first];i!=-1;i=es[i].next)
			if(es[i].capacity-es[i].flow>0)
				q.push(mp(es[i].dst,cur.second+1));
	}
	return label;
}

int DFS(vector<Edge>& es,vi& head,int v,int end,const vi& label,int f)
{
	if(v==end)
		return f;
	for(int& i=head[v];i!=-1;i=es[i].next){
		Edge& e=es[i];
		if(label[e.src]>=label[e.dst])
			continue;
		int residue=e.capacity-e.flow;
		if(residue<=0)
			continue;
		int augment=DFS(es,head,e.dst,end,label,min(residue,f));
		if(augment>0){
			e.flow+=augment;
			es[i^1].flow-=augment;
			return augment;
		}
	}
	return 0;
}

int Dinic(vector<Edge>& es,const vi& head,int begin,int end)
{
	int size=head.size();
	for(;;){
		vi label=BFS(es,head,begin);
		if(label[end]==size)
			break;
		vi temp=head;
		while(DFS(es,temp,begin,end,label,INF))
			;
	}
	int res=0;
	for(int i=head[begin];i!=-1;i=es[i].next)
		res+=es[i].flow;
	return res;
}

void solve()
{
	int w,h,b; cin>>w>>h>>b;
	vvi grid(h,vi(w)); // 0:water,1:block
	rep(k,b){
		int x0,y0,x1,y1; cin>>x0>>y0>>x1>>y1;
		repi(i,y0,y1+1) repi(j,x0,x1+1) grid[i][j]=1;
	}
	
	int n=h*w;
	vector<Edge> es;
	vi head(n+n+2,-1);
	int tap=n+n,sink=tap+1;
	
	rep(i,h) rep(j,w){
		int v=i*w+j;
		AddEdge(es,head,v,n+v,0,1);
		AddEdge(es,head,n+v,v,0,0);
	}
	rep(i,h) rep(j,w) if(!grid[i][j]){
		rep(k,4){
			int ni=i+"\xff\x1\0\0"[k],nj=j+"\0\0\xff\x1"[k];
			if(ni<0 || h<=ni || nj<0 || w<=nj || grid[ni][nj]) continue;
			int u=i*w+j,v=ni*w+nj;
			AddEdge(es,head,n+u,v,0,1);
			AddEdge(es,head,v,n+u,0,0);
		}
	}
	rep(i,w) if(!grid[0][i]){
		AddEdge(es,head,tap,i,0,1);
		AddEdge(es,head,i,tap,0,0);
	}
	rep(i,w) if(!grid[h-1][i]){
		int v=(h-1)*w+i;
		AddEdge(es,head,n+v,sink,0,1);
		AddEdge(es,head,sink,n+v,0,0);
	}
	
	cout<<Dinic(es,head,tap,sink)<<endl;
}

int main()
{
	int T; scanf("%d",&T);
	rep(i,T){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
