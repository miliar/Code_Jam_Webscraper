#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
//#include <iostream>
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


const int INF = 1000000001;
const int MAX = 100000;

int n;

#define PARALLEL 1

/* UWAGA NA PAMIEC!
   Moze byc potrzebne nawet Z razy wiecej pamieci w trakcie dzialania,
   chyba ze bedzie sie ja alokowac i zwalniac w solve() wtedy moze byc
   potrzebne do <liczba rdzeni> razy wiecej.
   Kompilowac z --openmp
 */

class solver {
	public:
		// wczytujemy caly input dla jednego zestawu danych
		void input() {
			scanf("%d %d %d", &m, &n, &k);
			REP(i,k)
			{
				int x1, x2, y1, y2;
				scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
				A.PB({x1, y1});
				B.PB({x2, y2});
			}
		}
		
		bool dfs(int u) {
			if(u == t) return true;
			vis[u] = 1;
			REP(i,SIZE(G[u]))
			{
				int v = G[u][i];
				if(!vis[v] && dfs(v)) {
					G[v].PB(u);
					G[u][i] = G[u].back();
					G[u].pop_back();
					return true;
				}
			}
			return false;
		}
		
		// skminiamy rozwiazanie
		void solve() {
			int N = 2*n*m+2;
			G.assign(N, VI());
			s = 2*n*m;
			t = s+1;
			arr.assign(n, VI(m, 0));
			REP(i,k)
			{
				FOR(a,A[i].ST,B[i].ST)
					FOR(b,A[i].ND,B[i].ND)
						arr[a][b] = 1;
			}
			int dx[] = {0, 0, 1, -1};
			int dy[] = {1, -1, 0, 0};
			#define id(x, y) (m*(x)+y)
			// REP(i,n) { REP(j,m) printf("%d", arr[i][j]); printf("\n"); }
			REP(i,n)
				REP(j,m)
				{
					if(arr[i][j]) continue;
					REP(tt,4)
					{
						int x = i + dx[tt];
						int y = j + dy[tt];
						if(0 <= x && x < n && 0 <= y && y < m && !arr[x][y]) {
							G[2*id(i, j)+1].PB(2*id(x, y));
						}
					}
					G[2*id(i, j)].PB(2*id(i, j)+1);
				}
			REP(j,m)
			{
				G[s].PB(2*id(n-1, j));
				G[2*id(0, j)+1].PB(t);
			}
			res = 0;
			vis.assign(N, 0);
			while(dfs(s))
			{
				res++;
				vis.assign(N, 0);
			}
		}
		
		// wypisujemy output
		void output() {
			printf("%d\n", res);
		}
	private:
		int n, m, k;
		VPII A, B;
		int res;
		VVI G;
		int s, t;
		VVI arr;
		vector<bool> vis;
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
