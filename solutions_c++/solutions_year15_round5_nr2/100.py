#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <vector>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define FOREACH(i, c) for(auto i = (c).begin(); i != (c).end(); ++i)
#define BIT(n, m) (((n) >> (m)) & 1)

template <typename S, typename T> ostream &operator<<(ostream &out, const pair<S, T> &p) {
  out << "(" << p.first << ", " << p.second << ")";
  return out;
}

template <typename T> ostream &operator<<(ostream &out, const vector<T> &v) {
  out << "[";
  REP(i, v.size()){
    if (i > 0) out << ", ";
    out << v[i];
  }
  out << "]";
  return out;
}

typedef long long ll;

const ll inf = 1e15;
const ll mod = 1000 * 1000 * 1000 + 7;
const double eps = 1e-9;

void solve(){
  int N, K;
  cin >> N >> K;
  vector<ll> S(N - K + 1);
  REP(i, N - K + 1) cin >> S[i];

  ll res = 0;
  ll rest1 = 0;
  ll rest2 = 0;
  vector<ll> L(K), R(K);
  REP(i, K){
    ll v = i;
    ll s = 0;
    ll min_x = 0;
    ll max_x = 0;
    while (v + K < N){
      s += S[v + 1] - S[v];
      v += K;
      min_x = min(min_x, s);
      max_x = max(max_x, s);
    }
    L[i] = min_x;
    R[i] = max_x;
    res = max(res, R[i] - L[i]);
    rest1 += -L[i];
  }
  cerr << res << endl;
  // cout << L << " " << R << endl;
  rest2 = rest1;
  REP(i, K){
    rest2 += res - (R[i] - L[i]);
  }
  // cout << rest1 << " " << rest2 << endl;
  ll x = (S[0] - rest1) / K;
  cerr << x << endl;
  cerr << x * K + rest1 << " " << (x + 1) * K  + rest1<<  " " << S[0] << endl;

  while (x * K + rest1 > S[0]) x--;
  while ((x + 1) * K + rest1 <= S[0]) x++;
  assert(x * K + rest1 <= S[0]);
  assert((x + 1) * K + rest1 > S[0]);

  if (S[0] > x * K + rest2) res++;
  cout << res << endl;
}
 
int main(){
  int T;
  cin >> T;
  REP(t, T){
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
