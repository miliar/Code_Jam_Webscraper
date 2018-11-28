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
const int N = 4e3;
ll g[N], h[N];
int need[N];
ll dp[N][N];
const ll INF = 1e9;
int main() {
  // nie zapomnij o ll
  ios_base::sync_with_stdio(0);
  cout << fixed << setprecision(10);
  double beg = 1.0 * clock() / CLOCKS_PER_SEC;
  
  make(int, t);
	RE (tt, t) {
    cout<<"Case #"<<tt<<": ";
    make3(ll, p, q, n);
    //cerr<<p<<" "<<q<<" "<<n<<endl;
    RE (i, n) {
      cin>>h[i]>>g[i];
      //cerr<<h[i]<<" "<<g[i]<<endl;
      for (int k = 1; ; k++) {
        for (int j = 0; ; j += q) {
          //debug(j);
          if (h[i] > j && h[i] <= j + k * p) {
            need[i] = k;
            //cerr<<j<<"<"<<h[i]<<"<="<<j + k * p<<endl;
            goto A;
          }
          if (h[i] < j) {
            break;
          }
        }
      }
      A: ;
      //cerr<<need[i]<<" ";
    }
    cerr<<endl;
    dp[0][1] = 0;
    for (int i = 2; i <= N; i++) {
      dp[0][i] = -INF;
    }
    dp[0][0] = 0;
    for (int i = 1; i <= n; i++) {
      for (int s = 0; s <= N - 2; s++) {
        dp[i][s] = -INF;
      }
      for (int s = 0; s <= N / 2; s++) {
        dp[i][s + (h[i] + q - 1) / q] = dp[i - 1][s]; 
      }
      for (int s = 0; s <= N / 2; s++) {
        int tow = max(0ll, (h[i] - p * (need[i] - 1) + q - 1) / q);
        if (p * (need[i] - 1) + q * tow >= h[i]) {
          tow--;
        }
        maxi(dp[i][s], dp[i - 1][max(0, s + need[i] - tow)] + g[i]);
      }
          
        
        
      for (int s = N / 2; s >= 0; s--) {
        maxi(dp[i][s], dp[i][s + 1]);
      }
      /* for (int s = 0; s <= 6; s++) {
        cerr<<i<<" "<<s<<" ";
        debug(dp[i][s]);
      } */
    }
    ll best = 0;
    for (int i = 0; i <= N - 2; i++) {
      maxi(best, dp[n][i]);
    }
    cout<<best<<endl;
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  // nie zapomnij o ll
  return 0;
}
