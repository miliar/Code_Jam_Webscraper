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
			scanf("%d %d", &n, &k);
			arr.resize(n);
			char tmp[1000];
			REP(i,n)
			{
				scanf("%s", tmp);
				arr[i] = string(tmp);
			}
		}
		
		VVI servers;
		
		int nodes(int ind) {
			VVI nxt(1, VI(26, -1));
			for(int x : servers[ind])
			{
				string s = arr[x];
				int v = 0;
				for(char c : s)
				{
					if(nxt[v][c-'A'] == -1) {
						nxt[v][c-'A'] = SIZE(nxt);
						nxt.PB(VI(26, -1));
					}
					v = nxt[v][c-'A'];
				}
			}
			return SIZE(nxt);
		}
		
		void solve(int ind) {
			if(ind == n) {
				int sum = 0;
				REP(i,k)
				{
					if(servers[i].empty()) return;
					sum += nodes(i);
				}
				if(sum > res.ST)
					res = {sum, 1};
				else if(sum == res.ST)
					res.ND++;
				return;
			}
			REP(i,k)
			{
				servers[i].PB(ind);
				solve(ind+1);
				servers[i].pop_back();
			}
		}
		
		// skminiamy rozwiazanie
		void solve() {
			res = {-1, 0};
			servers.assign(k, VI());
			solve(0);
		}
		
		// wypisujemy output
		void output() {
			printf("%d %d\n", res.ST, res.ND);
		}
	private:
		int n, k;
		PII res;
		vector<string> arr;
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
