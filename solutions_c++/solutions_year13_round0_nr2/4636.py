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
#define FORE(a, b, c) for(int c=int(a); c<= int(b); ++c)
#define FORD(a, b, c) for(int c=int(a); c>= int(b); --c)
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
typedef set<int> si;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

const int sto = 103;

char c;
int n, m, tn;
int t[sto][sto], imax[sto], jmax[sto];

void compute(int ti) {
  SC2(n, m);
  REP(i, sto) imax[i] = jmax[i] = 0;
  REP(i, n) REP(j, m) {
    SC(t[i][j]);
    imax[i] = max(imax[i], t[i][j]);
    jmax[j] = max(jmax[j], t[i][j]);
  }
  int ok = 1;
  REP(i, n) REP(j, m) {
    prd("%d %d %d\n", t[i][j], imax[i], jmax[j]);
    if((t[i][j] < imax[i]) && (t[i][j] < jmax[j]))
      ok = 0;
  }
  
  if (ok) printf("Case #%d: YES\n", ti);
  else printf("Case #%d: NO\n", ti);
  fprintf(stderr, "Case #%d\n", ti);
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
    compute(ti);
  return 0;
}

