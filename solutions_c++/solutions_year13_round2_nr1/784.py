#include<cstdio>
#include<algorithm>
#include<utility>
#include<string>
#include<vector>
#include<map>
#include<set>
//#include<multiset>
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

#define dbg if(1) 
#define prd dbg printf
#define koniec dbg {SCC(c);SCC(c);} return 0;

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef multiset<int> msi;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

const int DUZO = 1003;

char c;
int a, n, out, moves, tn, t[DUZO];

void compute(int ti) {
  SC2(a, n);
  out = n;
  FORE(0, n-1, i) SC(t[i]);
  sort(t, t+n);
  
  if (a==1)
    out = n;
  else {
    moves = 0;
    FORE(0, n-1, i) {
    	out = min(out, moves + (n-i));
    	while(a <= t[i]) {
    		a = 2*a - 1;
    		moves++;
    	}
    	a += t[i];
    }
    out = min(out, moves);
  }
  
  printf("Case #%d: %d\n", ti, out);
  fprintf(stderr, "Case #%d: %d\n", ti, out);
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
    compute(ti);
  return 0;
}

