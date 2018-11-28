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
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.first << ", " << pair.second << ")";}
const int N = 2e6;
ll dev[N];
int main() {
  // nie zapomnij o ll
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(10);
  double beg = 1.0 * clock() / CLOCKS_PER_SEC;
  
  make(int, t);
	RE (tt, t) {
    cout<<"Case #"<<tt<<": ";
    make(int, n);
    make2(ll, p, q);
    make2(ll, r, s);
    
    ll sum = 0;
    ll max_dev = 0;
    RE (i, n) {
      dev[i] = (((i - 1) * p + q) % r + s);
      sum += dev[i];
      maxi(max_dev, dev[i]);
      //cerr<<dev[i]<<" ";
    }
    if (sum == 0) {
      cout<<"0.0"<<endl;
      continue;
    }
    ll kl = max_dev, kp = sum, aktc, faj = sum;
    while (kl <= kp) {
      int completed = 0;
      ll in_this = 0;
      aktc = (kl + kp) / 2;
      RE (i, n) {
        in_this += dev[i];
        if (in_this > aktc) {
          completed++;
          in_this = dev[i];
        }
      }
      if (completed >= 3) {
        kl = aktc + 1;
      } else {
        kp = aktc - 1;
        faj = aktc;
      }
    }
    //debug(faj);
    cout<<1.0 * (sum - faj) / sum<<endl;
    
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  // nie zapomnij o ll
  return 0;
}
