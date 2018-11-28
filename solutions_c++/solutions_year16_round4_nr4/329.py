/*{{{*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <unordered_map>
#include <unordered_set>
#include <cassert>
using namespace std;
typedef pair<int, int> PP;
typedef long long LL;
#define pb push_back
#define fr first
#define sc second
#define bitcnt __builtin_popcount
#define all(x) x.begin(), x.end()
inline int ri() {int x; scanf("%d", &x); return x;}
#define rep2(i, n, ...) for (int i = 0; i < (n); i ++) 
#define rep3(i, a, b, ...) for (int i = (a); i < (b); i ++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define rep(...) GET_MACRO(__VA_ARGS__, rep3, rep2)(__VA_ARGS__)
#define drep2(i, n, ...) for (int i = (n) - 1; i >= 0; i --)
#define drep3(i, a, b) for (int i = (a) - 1; i >= (b); i --)
#define drep(...) GET_MACRO(__VA_ARGS__, drep3, drep2)(__VA_ARGS__)
template<typename T>inline bool smax(T&a, T b){if(a<b){a=b;return true;}return false;} 
template<typename T>inline bool smin(T&a, T b){if(a>b){a=b;return true;}return false;} 
/*}}}*/




bool check(vector<int> v) {
  if (v.size() == 0) return false;
  vector<int> c;
  rep(i, 4) c.pb(i);
  do {
    int ok = 1;
    rep(i, v.size()) {
      if (!(1 & v[i] >> c[i])) ok = 0;
    }
    if (ok) return false;
  } while (next_permutation(c.begin(), c.end()));
  return true;
}

void solve() {
  int mask = 0, n = 0;
  cin >> n;
  rep(i, n) rep(j, n) {
    char c; cin >> c;
    mask = mask * 2 + (c - '0');
  }
  int res = 10000000;
  //cout << (15 & mask) << endl;
  rep(i, (1 << (n * n))) if ((i & mask) == mask) {
    int ok = 1;
    rep(w, n) {
      vector<int> v;
      rep(m, n) {
        if (1 & (i >> (w * n + m))) {
          int k = 0;
          rep(ow, n) if (ow != w && (1 & (i >> (ow * n + m)))) k |= (1 << ow);
          v.pb(k);
        }
      }
      //rep(i, v.size()) cout << v[i] << ' '; cout << endl;
      if (!check(v)) {
        ok = 0;
      }
    }
    if (ok) smin(res, (int)(bitcnt(i) - bitcnt(mask)));
  }
  cout << res << endl;
}

int main() {
  #ifdef _TEST_
  freopen("input.txt", "r", stdin);
  //freopen("out.txt", "w", stdout);
    
  #endif
  int Q; cin >> Q;
  rep(i, Q) {
    cout << "Case " << "#" << i + 1 << ": ";
    solve();
    //break;
  }
  return 0;
}
