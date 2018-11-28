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

typedef long double LD;

class solver {
	public:
		// wczytujemy caly input dla jednego zestawu danych
		void input() {
			scanf("%d %lld %lld %lld %lld", &n, &p, &q, &r, &s);
		}
		
		LL mid(VLL arr) {
			LL pref = 0;
			LL suf = accumulate(ALL(arr), 0LL);
			int e = 0;
			LL m = 0;
			LL best = 0;
			REP(b,n)
			{
				while(e < n && m < max(pref, suf))
				{
					m += arr[e];
					suf -= arr[e];
					e++;
				}
				if(m >= max(pref, suf)) {
					best = max(best, pref+suf);
				}
				pref += arr[b];
				m -= arr[b];
			}
			return best;
		}
		
		LL pre(VLL arr) {
			LL pref = 0;
			LL m = 0;
			LL suf = accumulate(ALL(arr), 0LL);
			int e = 0;
			LL best = 0;
			REP(i,n)
			{
				while(e < n && m + arr[e] <= pref)
				{
					m += arr[e];
					suf -= arr[e];
					e++;
				}
				if(pref >= max(m, suf)) {
					best = max(best, m+suf);
				}
				pref += arr[i];
				m -= arr[i];
			}
			return best;

		}
		
		// skminiamy rozwiazanie
		void solve() {
			VLL arr(n, 0);
			REP(i,n)
				arr[i] = ((LL)i*p+q) % r + s;
			LL re = mid(arr);
			re = max(re, pre(arr));
			reverse(ALL(arr));
			re = max(re, pre(arr));
			res = (LD)re/accumulate(ALL(arr), 0LL);
		}
		
		// wypisujemy output
		void output() {
			printf("%.10Lf\n", res);
		}
	private:
		int n;
		LL p, q, r, s;
		LD res;
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
