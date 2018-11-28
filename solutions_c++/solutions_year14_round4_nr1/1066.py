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

#define dbg if(1) 
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

const int NMAX = 100000;

char c;
int tn, n, x, k, space, ans, t[NMAX], used[NMAX];

void compute(int ti) {
	SC2(n, x);
	REP(i, n) {
		SC(t[i]);
		used[i] = 0;
	}
	sort(t, t+n);
	reverse(t, t+n);
	ans = 0;
	
	REP(i, n) {
		if(used[i]) continue;
		used[i] = 1;
		space = x - t[i];
		
		k = 0;
		while(k < n && (t[k] > space || used[k]))
			++k;
		used[k] = 1;
		
		ans++;
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

