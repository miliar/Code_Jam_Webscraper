#define ONLINE_JUDGE
#ifdef ONLINE_JUDGE
#include <bits/stdc++.h>
using namespace std;
#else
#include "header.h"
#include "debug.h"
#endif
#define sz(s) int((s).size())
#define clr(a) memset(a,0,sizeof(a))
#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int(i)=0; (i)<(n);++(i))
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
typedef pair <int,int> pii;
typedef long long LL;
template <class T> inline T gcd(T a,T b){return (!b? a : gcd(b,a%b));}
template <class T> inline T ABS(T x){return ((x)>0?(x):(-(x)));}
const int N = 200000;

bool hush [10];

bool check (LL t) {
  while (t > 0) {
    //show (t);
    hush [t % 10] = 1;
    t /= 10;
  }
  bool ret = 1;
  for (int i = 0; i < 10; ++i) {
    if (hush [i] == 0) {
      ret = 0;
      break;
    }
  }
  return ret;
}

int main () {
  #ifndef ONLINE_JUDGE
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
  #endif
  cin.sync_with_stdio (0); cin.tie (0);
  int tt;
  cin >> tt;
  for (int tc = 1; tc <= tt; ++tc) {
    cout << "Case #" << tc << ": ";
    LL n;
    cin >> n;
    for (int i = 0; i < 10; ++i) {
      hush [i] = 0;
    }
    bool ok = 0;
    LL ans = 0;
    for (int i = 1; i < 10001; ++i) {
      //pn;
      if (check (n*i)) {
        ok = 1;
        ans = n * i;
        break;
      }
    }
    if (ok) {
      cout << ans << '\n';
    } else {
      cout << "INSOMNIA\n";
    }
  }
}

