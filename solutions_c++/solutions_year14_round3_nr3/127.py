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

#define REP(i, n) for(int i = 0; i< n; ++i)
#define SC(a) scanf("%d", &a)
#define SCC(a) scanf("%c", &a)
#define SC2(a, b) scanf("%d%d", &a, &b)
#define SC3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define PR(a) printf("%d\n", a)
#define FORE(c, a, b) for(int c=int(a); c<= int(b); ++c)
#define FORD(c, a, b) for(int c=int(a); c>= int(b); --c)
#define FORIT(cont_t, cont, it) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it) 
#define ALL(a) a.begin(), a.end()

#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define itr iterator

#define dbg if(0) 
#define prd dbg printf
#define koniec dbg {SCC(c);SCC(c);} return 0;

using namespace std;

typedef vector<int> vi;
typedef set<char> sc;
typedef multiset<int> msi;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vpi;
typedef pair<pi, string> psi;
typedef pair<int, psi> ipsi;
typedef vector<psi> vpsi;
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

const int NMAX = 24;

char c;
int n, m, p, tn, k, ans, dx, dy;
char t[NMAX][NMAX];
vpi d;

bool correct(int x, int y) {
	return (x >= 0 && x < n && y >= 0 && y < m);
}

void compute(int ti) {
  cin >> n >> m >> k;
  p = n*m;
  ans = p;
  
  REP(mask, (1<<p)) {
  	int st = 0;
  	REP(i, p) {
  		if((1<<i) & mask) {
  			t[i%n][i/n] = 1;
			++st;
		}
		else
			t[i%n][i/n] = 0;
	}
	int enc = 0;
	//prd("%d\n", enc);
	REP(i,n) REP(j,m) {
		int shit = 0;
		REP(h, 4) {
			dx = d[h].xx;
			dy = d[h].yy;
			int i1 = i, j1 = j;
			while(correct(i1,j1) && t[i1][j1] != 1) {
				i1 += dx;
				j1 += dy;
			}
			if(!correct(i1,j1)) {
				shit=1;
				break;
			}
		}
		if(!shit) ++enc;
		if(!shit && t[i][j] == 0) t[i][j] = 2;
	}
	if(enc >= k) ans = min(ans, st);
	dbg if(ans == st) {
		printf("setting %d\n", enc);
		REP(i,n) {
			REP(j,m) printf("%d", t[i][j]);
			printf("\n");
		}
		scanf("%d", &dx);
	}
}
  cout << "Case #" << ti << ": " << ans << endl;
  cerr << "Case #" << ti << ": " << ans << endl;
}

int main() {
  d.pb(mp(0,1));
  d.pb(mp(0,-1));
  d.pb(mp(1,0));
  d.pb(mp(-1,0));
  cin >> tn;
  FORE(ti, 1, tn)
    compute(ti);
  return 0;
}

