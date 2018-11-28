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
			scanf("%d %d", &n, &m);
			REP(i,n)
			{
				char asd[m+1];
				scanf("%s", asd);
				arr.PB(string(asd));
			}
		}
		
		// skminiamy rozwiazanie
		void solve() {
			VI row(n), col(m);
			VVI rowID(n, VI(m, -1));
			VVI colID(n, VI(m, -1));
			REP(i,n)
				REP(j,m)
					if(arr[i][j] != '.') {
						rowID[i][j] = row[i];
						colID[i][j] = col[j];
						row[i]++;
						col[j]++;
					}
			REP(i,n)
				REP(j,m)
					if(arr[i][j] != '.' && row[i] == 1 && col[j] == 1) {
						res = -1;
						return;
					}

			res = 0;
			REP(i,n)
				REP(j,m)
					if(arr[i][j] == '<') {
						res += rowID[i][j] == 0;
					} else if(arr[i][j] == '>') {
						res += rowID[i][j] == row[i]-1;
					} else if(arr[i][j] == 'v') {
						res += colID[i][j] == col[j]-1;
					} else if(arr[i][j] == '^') {
						res += colID[i][j] == 0;
					}
			
		}
		
		// wypisujemy output
		void output() {
			if(res == -1) printf("IMPOSSIBLE\n");
			else printf("%d\n", res);
		}
	private:
		int n, m;
		vector<string> arr;
		int res;
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
