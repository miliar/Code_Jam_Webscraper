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

#define PARALLEL 1

/* UWAGA NA PAMIEC!
   Moze byc potrzebne nawet Z razy wiecej pamieci w trakcie dzialania,
   chyba ze bedzie sie ja alokowac i zwalniac w solve() wtedy moze byc
   potrzebne do <liczba rdzeni> razy wiecej.
   Kompilowac z --openmp
 */

void remax(int &a, int b) { if(b > a) a = b; }

class solver {
	public:
		// wczytujemy caly input dla jednego zestawu danych
		void input() {
			scanf("%d %d %d", &D, &T, &n);
			H.resize(n);
			G.resize(n);
			REP(i,n) scanf("%d %d", &H[i], &G[i]);
			H.PB(201);
			G.PB(0);
		}
		
		// skminiamy rozwiazanie
		void solve() {
			VI dp[n+2][10*n+3][202];
			REP(i,n+2) REP(j,10*n+3) REP(k,202) dp[i][j][k].assign(2, -INF);
			dp[0][0][H[0]][0] = 0;
			REP(i,n)
				FORD(h,200,0)
					REP(s,10*n+3)
					{
						if(dp[i][s][h][0] >= 0) { // moj ruch
							{ // skip
								remax(dp[i][s+1][h][1], dp[i][s][h][0]);
							}
							if(s > 0) { // strzelam z opoznienia
								if(h <= D) { // zabijam
									remax(dp[i+1][s-1][H[i+1]][0], dp[i][s][h][0] + G[i]);
								} else {
									remax(dp[i][s-1][h-D][0], dp[i][s][h][0]);
								}
							}
							{ // strzelam w turze
								if(h <= D) {
									remax(dp[i+1][s][H[i+1]][1], dp[i][s][h][0] + G[i]);
								} else {
									remax(dp[i][s][h-D][1], dp[i][s][h][0]);
								}
							}
						}
						
						if(dp[i][s][h][1] >= 0) { // ruch wiezy
							if(h <= T) {
								remax(dp[i+1][s][H[i+1]][0], dp[i][s][h][1]);
							} else {
								remax(dp[i][s][h-T][0], dp[i][s][h][1]);
							}
						}
					}
			res = 0;
			REP(s,20*n+3)
				REP(h,202)
					REP(t,2)
						remax(res, dp[n][s][h][t]);
		}
		
		// wypisujemy output
		void output() {
			printf("%d\n", res);
		}
	private:
		int n, D, T;
		VI H, G;
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
