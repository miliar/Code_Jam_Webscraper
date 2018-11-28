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

int main() {
  make(int, zz);
  RE (zzz, zz) {
    cout<<"Case #"<<zzz<<": ";
    make(int, n);
    vector<LD> nao, ken;
    RE (i, n) {
      make(LD, a);
      nao.PB(a);
    }
    RE (i, n) {
      make(LD, a);
      ken.PB(a);
    }
    sort(ALL(nao));
    sort(ALL(ken));
    int kl = 0, kp = n, faj = 0, aktc;
    while (kl <= kp) {
      aktc = (kl + kp) / 2;
      for (int i = n - aktc; i < n; i++) {
        if (ken[i - n + aktc] > nao[i]) {
          goto A;
        }
      }
      faj = aktc;
      kl = aktc + 1;
      continue;
      A: ;
      kp = aktc - 1;
    }
    cout<<faj<<" ";
    int left = 0, right = n - 1, score = 0;
    for (int i = n - 1; i >= 0; i--) {
      if (nao[i] < ken[right]) {
        right--;
        score++;
      }
    }
    cout<<n - score<<endl;
  }
  return 0;
}
    
  
  
  
  
  
  
  
  
  
  


