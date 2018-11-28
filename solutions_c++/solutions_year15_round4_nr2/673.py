#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<LD, LD> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &rout, pair<T1, T2> pair) { return rout << "(" << pair.X << ", " << pair.Y << ")";}

LD EPS = 1e-10;

void solve(int t) {
  printf("Case #%d: ", t+1);

  int n; cin >> n;
  LD vv, xx; cin >> vv >> xx;

  double cc = 0; 
  vector<PII> smaller;
  vector<PII> bigger;

  REP(i, n) {
    LD x, c; cin >> c >> x;
    if (x > xx + EPS) { bigger.PB(MP(x, c)); }
    else if (x < xx - EPS) { smaller.PB(MP(x, c)); }
    else { cc += c; }
  }

  if (cc < EPS && (smaller.empty() || bigger.empty())) {
    printf("IMPOSSIBLE\n");
    return; 
  } 

  sort(ALL(smaller));
  reverse(ALL(smaller));
  sort(ALL(bigger));

  while (!smaller.empty() && !bigger.empty()) {
    PII p1 = smaller.back(); smaller.pop_back();
    PII p2 = bigger.back(); bigger.pop_back();


    LD a = p1.Y * (xx - p1.X);
    LD b = p2.Y * (p2.X - xx);
    LD m = min(a, b);
    
    LD aa = m / (xx - p1.X);
    LD bb = m / (p2.X - xx);

    cc += aa + bb;
    p1.Y -= aa;
    p2.Y -= bb;
    
    if (p1.Y > EPS) {
      smaller.PB(p1);
    }
    if (p2.Y > EPS) {
      bigger.PB(p2);
    }
  }

  printf("%.6Lf\n", vv / cc);
}

int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);

    int t; cin >> t;
    for (int i=0; i<t; ++i) {
      solve(i);
    }
    return 0;
}
