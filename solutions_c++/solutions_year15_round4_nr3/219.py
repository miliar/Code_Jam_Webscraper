#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <numeric>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
//#include <cmath>
#include <set>
#include <map>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,b,e) for(int i=(b);i<=(e);++i)
#define FOReach(it,V) for(__typeof((V).begin()) it=(V).begin();it!=(V).end();++it)
#define FORD(i,b,e) for(int i=(b);i>=(e);--i)

#define PB push_back
#define ALL(V) (V).begin(),(V).end()
#define SIZE(V) ((int)(V).size())

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
	#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
	#define debug(...)
#endif

int __stmp;
#define scanf __stmp=scanf


const int MAX = 100000;

#define PARALLEL 1

/* UWAGA NA PAMIEC!
   Moze byc potrzebne nawet Z razy wiecej pamieci w trakcie dzialania,
   chyba ze bedzie sie ja alokowac i zwalniac w solve() wtedy moze byc
   potrzebne do <liczba rdzeni> razy wiecej.
   Kompilowac z --openmp
 */

const long long INF = 1000000000000000001LL;

class graph {
	public:
		void init(int _n, int _s, int _t) {
			n = _n, s = _s, t = _t;
			G.assign(n, vector<edge>());
			E.resize(n);
		}
		void add_edge(int u, int v, long long c, long long c_rev=0) {
			G[u].push_back(edge(v, c));
			G[v].push_back(edge(u, c_rev));
			G[u].back().rev_ind = G[v].size()-1;
			G[v].back().rev_ind = G[u].size()-1;
		}
		long long compute_flow() {
			long long flow = 0;
			while(bfs())
			{
				for(int i=0;i<n;++i) E[i] = G[i].begin();
				long long f = 0;
				do
				{
					flow += f;
				} while((f = dfs(s, INF)));
			}
			return flow;
		}
	private:
		struct edge {
			int v;
			long long cap, flow;
			int rev_ind;
			edge() {}
			edge(int _v, long long _cap) : v(_v), cap(_cap), flow(0) {}
		};
		int n, s, t;
		vector< vector<edge> > G;
		vector<vector<edge>::iterator> E;
		vector<int> dis;
		
		bool bfs() {
			dis.assign(n, 0);
			deque<int> Q;
			Q.push_back(t);
			dis[t] = 1;
			while(!Q.empty() && !dis[s])
			{
				int v = Q.front(); Q.pop_front();
				for(vector<edge>::iterator e=G[v].begin();e!=G[v].end();++e)
					if(!dis[e->v] && G[e->v][e->rev_ind].flow < G[e->v][e->rev_ind].cap) {
						dis[e->v] = dis[v] + 1;
						Q.push_back(e->v);
					}
			}
			return dis[s];
		}
		
		long long dfs(int v, long long c) {
			if(v == t) return c;
			long long flow = 0;
			for(vector<edge>::iterator &e=E[v];e!=G[v].end();++e)
				if(dis[v] - 1 == dis[e->v] && e->flow < e->cap) {
					long long f = dfs(e->v, min(c-flow, e->cap - e->flow));
					flow += f;
					e->flow += f;
					G[e->v][e->rev_ind].flow -= f;
					if(flow == c) return flow;
				}
			return flow;
		}
};

class solver {
	public:
		// wczytujemy caly input dla jednego zestawu danych
		void input() {
			scanf("%d\n", &n);
			S.resize(n);
			map<string, int> hash;
			REP(i,n)
			{
				string line;
				getline(cin, line);
				stringstream ss(line);
				string word;
				while(ss >> word)
				{
					if(hash.find(word) == hash.end()) {
						int h = hash.size();
						hash[word] = h;
					}
					S[i].PB(hash[word]);
				}
			}
			cnt = hash.size();
		}
		
		// skminiamy rozwiazanie
		void solve() {
			graph G;
			G.init(n+2*cnt, 0, 1);
			REP(i,cnt) G.add_edge(n+i, n+cnt+i, 1);
			REP(i,n)
			{
				set<int> s(ALL(S[i]));
				REP(j,i)
				{
					FOReach(c,S[j])
						if(s.count(*c) == 1) {
							G.add_edge(i, n+*c, 1000000000);
							G.add_edge(n+cnt+*c, j, 1000000000);
							
							G.add_edge(j, n+*c, 1000000000);
							G.add_edge(n+cnt+*c, i, 1000000000);
						}
				}
			}
			res = G.compute_flow();
		}
		
		// wypisujemy output
		void output() {
			printf("%d\n", res);
		}
	private:
		int n;
		VVI S;
		int res;
		int cnt;
};

int main(int argc, char *argv[]) {
	int case_id = argc == 2 ? atoi(argv[1])-1 : -1;
	int Z;
	scanf("%d", &Z);
	vector<solver> S(Z);
	REP(z,Z) S[z].input();
	if(case_id == -1) {
		#if PARALLEL == 1
			#pragma omp parallel for schedule(dynamic)
		#endif
		REP(z,Z) S[z].solve();
	} else {
		S[case_id].solve();
	}
	REP(z,Z)
	{
		if(case_id == -1 || z == case_id) {
			printf("Case #%d: ", z+1);
			S[z].output();
		}
	}
	return 0;
}
