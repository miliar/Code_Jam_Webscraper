#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <limits>
#include <iostream>
#include <utility>

using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x); fflush(stdout))

#define gc getchar  //unlocked linux
#define all(v) (v).begin(), (v).end()
#define FU(i, a, b) for(decltype(b) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)
#define FD(i, a, b) for (decltype(b) i = (b)-1; i >= a; --i)
#define fd(i, n) FD(i, 0, n)
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define sz(c) int((c).size())
#define mk make_pair

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;

const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

int cmp_double(double a, double b, double eps = 1e-9){
  return a + eps > b ? b + eps > a ? 0 : 1 : -1;  //0 = iguais, 1 = a maior
}

inline void scanint(int &x){
  register int c = gc();
  x = 0;
  int neg = 0;
  for(;((c<48 || c>57) && c != '-');c = gc());
  if(c=='-') {neg=1;c=gc();}
  for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
  if(neg) x=-x;
}

int main(){
  int T;
  int cases = 1;
  cin >> T;
  while(T--){
    printf("Case #%d: ", cases++);
    ll N; cin >> N;
    if (N == 0) {
      printf("INSOMNIA\n");
    } else {
      map<ll, bool> m;
      bool ok = false;
      for (int j = 1; j < 1000; j++){
        ll v = N * (ll)j;
        while(v != 0){
          ll d = v % 10;
          m[d] = true;
          v = v/10;
        }
        if (m.size() >= 10) {
          printf("%lld\n", N*(ll)j);
          ok = true;
          break;
        }
      }
      if (!ok) printf("INSOMNIA\n");
    }
  }
  return 0;
}
