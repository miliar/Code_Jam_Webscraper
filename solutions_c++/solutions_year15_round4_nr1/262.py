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

// actual code

const int NMAX = 200, OUTMAX = 1000000;

int tt, r, c, out;
char t[NMAX][NMAX];

void solve(int ti) {
	cin >> r >> c;
	REP(ri, r)
		cin >> t[ri];
	out = 0;
	
	REP(ri, r) { 
		REP(ci, c) if(t[ri][ci] != '.') {
			int up = 0, down = 0, left = 0, right = 0;
			
			FORE(ri1, 0, ri-1) if(t[ri1][ci] != '.') up = 1;
			FORE(ri1, ri+1, r-1) if(t[ri1][ci] != '.') down = 1;
			FORE(ci1, 0, ci-1) if(t[ri][ci1] != '.') left = 1;
			FORE(ci1, ci+1, c-1) if(t[ri][ci1] != '.') right = 1;
			
			prd("[%d, %d] %c up %d down %d left %d right %d\n", ri, ci, t[ri][ci], up, down, left, right);
			if(t[ri][ci] == '^' && up) continue;
			if(t[ri][ci] == 'v' && down) continue;
			if(t[ri][ci] == '<' && left) continue;
			if(t[ri][ci] == '>' && right) continue;
			
			out++;
			if(up + down + left + right == 0)
				out = OUTMAX;
		}
	}
	if(out < OUTMAX)
		cout << "Case #" << ti << ": " << out << endl;
	else
		cout << "Case #" << ti << ": IMPOSSIBLE" << endl;
}

int main() {
	cin >> tt;
	REP(ti, tt)
		solve(ti + 1);
	return 0;
}
