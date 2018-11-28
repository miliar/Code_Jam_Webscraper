#include<cstdio>
#include<algorithm>
#include<utility>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<iostream>

// macros

#define SC(n) scanf("%d", &n)
#define SC2(n, m) scanf("%d %d", &n, &m)
#define SCC(c) scanf(" %c", &c)
#define FORE(c, a, b) for(int c=a; c<= int(b); ++c)
#define FORD(c, a, b) for(int c=a; c>= int(b); --c)
#define FORIT(it, cont, cont_t) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it)
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define ALL(a) a.begin(), a.end() 
#define PR(n) printf("%d ", (int) (n)) 
#define PRL(n) printf("%lld ", (ll) (n)) 

#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define itr iterator

#define dbg if(0)
#define prd dbg printf

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef vector<vi> vvi;

// actual code

const int NMAX = 10000;
int tt, n, k, summ, suma;
int mini[NMAX], maxi[NMAX], sum[NMAX];

void solve(int ti) {
	SC2(n, k);
	REP(i, n-k+1)
		SC(sum[i]);
	summ = sum[0];
	
	REP(i, k) {
		mini[i] = maxi[i] = 0;
		suma = 0;
		for(int j = i; j < n-k; j += k) {
			suma += sum[j+1] - sum[j];
			mini[i] = min(suma, mini[i]);
			maxi[i] = max(suma, maxi[i]);
		}
		prd("%d: %d %d\n", i, mini[i], maxi[i]);
		summ += mini[i];
		maxi[i] -= mini[i];
	}
	sort(maxi, maxi + k);
	int out = 0, k1 = summ % k;
	if(k1 < 0) k1 += k;
	prd("summ %d k1 %d\n", summ, k1);
	
	REP(i, k)
		out = max(out, maxi[i]);
	REP(i, k)
		k1 -= (out - maxi[i]);
	if(k1 > 0) ++out;
	printf("Case #%d: %d\n", ti, out);
}

int main() {
	SC(tt);
	REP(ti, tt)
		solve(ti + 1);
	return 0;
}
