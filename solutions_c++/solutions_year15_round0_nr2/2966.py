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
#define ritr reverse_iterator

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

const int NMAX = 1003;

char c;
int d, x, tn;
int mylog[NMAX];

void compute(int ti) {
  vi pan;
  SC(d);
  REP(i, d) {
    SC(x);
    pan.pb(x);
  }
  int out = NMAX;
  FORE(j, 1, NMAX) {
    int sum = 0;
    REP(i, d) {
      int parts = (pan[i] + j - 1) / j;
      sum += parts - 1;
    }
    out = min(out, j + sum);
  }  
  cout << "Case #" << ti << ": " << out << endl;
}

int main() {
  /*mylog[0] = mylog[1] = 0;
  FORE(i, 2, NMAX-1) {
    mylog[i] = NMAX;
    FORE(j, 1, i-1)
      mylog[i] = min(mylog[i], 1 + mylog[j] + mylog[*/
  
  cin >> tn;
  FORE(ti, 1, tn)
    compute(ti);
  return 0;
}

