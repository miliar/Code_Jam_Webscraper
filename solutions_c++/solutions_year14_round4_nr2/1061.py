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
#define FORIT(it, cont, cont_t) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it) 
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
typedef set<int> si;
typedef multiset<int> msi;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef pair<pi, string> psi;
typedef pair<int, psi> ipsi;
typedef vector<psi> vpsi;
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

const int NMAX = 10003;

char c;
int n, m, p, tn, ans, x, y;
int t[NMAX], inv[NMAX], inv2[NMAX];
pi s[NMAX];

void compute(int ti) {
	SC(n);
	REP(i, n) {
		SC(t[i]);
		s[i] = mp(t[i], i);
	}
	
	sort(s, s+n);
	ans = 0, x = 0, y = n - 1;
	REP(i, n) {
		int j = s[i].yy;
		if(j - x < y - j) {
			ans += j - x;		
			REP(ii, n)
				if(x <= s[ii].yy && s[ii].yy < j)
					s[ii].yy++;
			s[i].yy = x;
			x++;	
		}
		else {
			ans += y - j;	
			REP(ii, n)
				if(j < s[ii].yy && s[ii].yy <= y)
					s[ii].yy--;
			s[i].yy = y;
			--y;		
		}
		prd("move %d to %d\n", j, s[i].yy);
	}
			
  cout << "Case #" << ti << ": " << ans << endl;
  cerr << "Case #" << ti << ": " << ans << endl;
}

int main() {
  cin >> tn;
  FORE(ti, 1, tn)
    compute(ti);
  return 0;
}

