// Enjoy your stay.

#include <bits/stdc++.h>

#define long long long
#define LOOPVAR_TYPE long

#define all(x) (x).begin(), (x).end()
#define sz(x) ((LOOPVAR_TYPE)(x).size())
#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define _rep(i, n) _rep2(i, 0, n)
#define _rep2(i, a, b) for(LOOPVAR_TYPE i = (LOOPVAR_TYPE)(a); i < (LOOPVAR_TYPE)(b); i++)
#define rep(...) GET_MACRO(__VA_ARGS__, _rep2, _rep)(__VA_ARGS__)

#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pb push_back

const double EPS = 1e-9;
const double PI = acos(-1.0);
const long INF = 1070000000LL;
const long MOD = 1000000007LL;

using namespace std;

typedef istringstream iss;
typedef stringstream sst;
typedef pair<LOOPVAR_TYPE, LOOPVAR_TYPE> pi;
typedef vector<LOOPVAR_TYPE> vi;

#include <sys/time.h>
long getTime(){
	struct timeval t;
	gettimeofday(&t, NULL);
	return t.tv_sec * 1000000LL + t.tv_usec;
}

const int MN = 8010;
struct dinic{
	struct edge{
		int to;long cap;int rev;
		edge(int to,long cap,int rev): to(to),cap(cap),rev(rev){}
	};

	vector<edge> G[MN];
	long level[MN];
	int iter[MN];
	
	void init(int N){
		rep(i,N)G[i].clear();
	}
	
	void add_edge(int from,int to,long cap){
		G[from].pb(edge(to,cap,sz(G[to])));
		G[to].pb(edge(from,0,sz(G[from])-1));
	}
	
	void bfs(int s){
		memset(level,-1,sizeof(level));
		queue<int> que;
		level[s]=0;
		que.push(s);
		while(!que.empty()){
			int v=que.front(); que.pop();
			rep(i,sz(G[v])){
				edge &e = G[v][i];
				if(e.cap>0 && level[e.to]<0){
					level[e.to] = level[v]+1;
					que.push(e.to);
				}
			}
		}
	}
	
	long dfs(int v,int t,long f){
		if(v==t)return f;
		for(int &i=iter[v]; i<sz(G[v]); i++){
			edge &e = G[v][i];
			if(e.cap>0 && level[v] < level[e.to]){
				long d=dfs(e.to,t,min(f,e.cap));
				if(d>0){
					e.cap-=d;
					G[e.to][e.rev].cap+=d;
					return d;
				}
			}
		}
		return 0;
	}
	
	int max_flow(int s,int t){
		long flow=0;
		for(;;){
			bfs(s);
			if(level[t]<0)return flow;
			memset(iter,0,sizeof(iter));
			int f;
			while((f=dfs(s,t,INF*INF))>0){
				flow+=f;
			}
		}
	}
};

int N;
map<string, int> M;

void main2(){
	M.clear();
	cin>>N;
	string st;
	getline(cin,st);
	vector<vector<int>> input;
	rep(i,N){
		getline(cin,st);
		iss is(st);
		string t;
		vector<int> v;
		while(is>>t){
			if(M.find(t) == M.end()){
				int id = sz(M);
				M[t] = id;
			}
			v.pb(M[t]);
		}
		input.pb(v);
	}
	dinic dnc;
	int m = sz(M);
	assert(2*m + 2 <= MN);
	dnc.init(2*m + 2);
	int s = 2*m, t = 2*m+1;
	rep(i,sz(input[0])){
		dnc.add_edge(s, input[0][i], INF);
	}
	rep(i,sz(input[1])){
		dnc.add_edge(m+input[1][i], t, INF);
	}
	rep(i,m){
		dnc.add_edge(i,i+m,1);
	}
	rep(i,2,sz(input)){
		rep(j,sz(input[i]))rep(k,j+1,sz(input[i])){
			//dnc.add_edge(input[i][j], m+input[i][k], 1);
			//dnc.add_edge(input[i][k], m+input[i][j], 1);
			dnc.add_edge(m+input[i][j], input[i][k], 1);
			dnc.add_edge(m+input[i][k], input[i][j], 1);
		}
	}
	cout<<dnc.max_flow(s, t)<<endl;
}

int main(){
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	
	
	int T;
	cin >> T;
	long start = getTime(), pre = start;
	rep(tc, 1, T + 1){
		cout << "Case #" << tc << ": ";
		main2();
		long now = getTime();
		cerr << tc << "/" << T << ": " << (now - pre) / 1000000. << endl;
		if(tc == T){
			cerr << "Total: " << (now - start) / 1000000. << endl;
			cerr << "  Ave: " << (now - start) / 1000000. / T << endl;
		}
		pre = now;
	}
}
