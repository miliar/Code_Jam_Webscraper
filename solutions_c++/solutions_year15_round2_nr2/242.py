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
typedef queue<pair<ll, int> > qll;

// actual code

int r, c, n, ans, tt;
int cols[2], boks[2][5];

void compute(int ki) {
	cin >> r >> c >> n;
	
	cols[0]  = cols[1] = 0;
	REP(i, 2) REP(j, 5)
		boks[i][j] = 0;
		
	REP(ir, r) REP(ic, c) {
		int col = (ir + ic) % 2;
		int boki = 0;
		if(ir > 0) boki++;
		if(ir < r - 1) boki++;
		if(ic > 0) boki++;
		if(ic < c - 1) boki++;
		
		cols[col]++;
		boks[col][boki]++;
	}
	
	ans = r*c*4;
	REP(i, 2) {
		int tmp = 0, m = n;
		int ii = !i;
		m -= cols[i];
		
		FORE(j, 1, 4) {		
			if(m > 0) {
				tmp += j * min(m, boks[ii][j]);
				m -= boks[ii][j];
			}
		}
		
		ans=min(ans, tmp);
	}

	cout << "Case #" << ki << ": " << ans << endl;
	cerr << "Case #" << ki << ": " << ans << endl;
}
		

int main() {
	cin >> tt;
	REP(ti, tt)
		compute(ti + 1);
	return 0;
}
