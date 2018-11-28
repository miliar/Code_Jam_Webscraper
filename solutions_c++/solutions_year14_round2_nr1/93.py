#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdio>
#include <utility>
#include <iomanip>
#include <assert.h>
#define MP make_pair
#define PB push_back
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define RE(i, n) FOR(i, 1, n)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#ifdef LOCAL
#define debug(x) {cerr <<#x <<" = " <<x <<"\n"; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<"\n"; }}
#else
#define debug(x)
#define debugv(x)
#endif
#define make(type, x) type x; cin>>x;
#define make2(type, x, y) type x, y; cin>>x>>y;
#define make3(type, x, y, z) type x, y, z; cin>>x>>y>>z;
using namespace std;
typedef long long ll;
typedef long double LD;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef vector<int> VI;
typedef vector<ll> VLL;
typedef vector<pair<int, int> > VPII;
typedef vector<pair<ll, ll> > VPLL;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

const int N = 1e6 + 5;
vector<int> occ[N];
char letters[N];
int main() {
  // nie zapomnij o ll
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(10);
  
  make(int, tt);
  RE (ttt, tt) {
    cout<<"Case #"<<ttt<<": ";
    make(int, n);
    string input;
    int parts = 0;
    bool failed = 0;
    RE (i, N - 2) {
      occ[i].clear();
    }
    getline(cin, input);
    RE (i, n) {
      int pos = 0;
      getline(cin, input);
      int len = input.length();
      REP (j, len) {
        //debug(j);
        //debug(len);
        if (j == 0 || input[j] != input[j - 1]) {
          pos++;
          occ[pos].PB(0);
          if (i > 1) {
            if (pos > parts) {
              failed = 1;
            }
            if (letters[pos] != input[j]) {
              failed = 1;
            }
          }
          letters[pos] = input[j];
        }
        occ[pos].back()++;
      }
      if (i > 1 && parts != pos) {
        failed = 1;
      }
      parts = pos;
    }
    ll res = 0;
    if (failed) {
      cout<<"Fegla Won"<<endl;
    } else {
      RE (i, parts) {
        sort(ALL(occ[i]));
        //debugv(occ[i]);
        int med_ind = n / 2;
        for (auto h : occ[i]) {
          res += abs(h - occ[i][med_ind]);
        }
      }
      cout<<res<<endl;
    }
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  // nie zapomnij o ll
  return 0;
}
