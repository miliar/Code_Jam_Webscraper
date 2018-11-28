#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <cstdio>
#include <iostream>
#include <complex>
#include <cassert>
#define rep(i, n) for (int i = 0; i < n; i++)
#define irep(i, n) for (int i = n-1; i >= 0; i--)
#define rep1(i, n) for (int i = 1; i <= n; i++)
#define irep1(i, n) for (int i = n; i >= 1; i--)
#define sz(c) int((c).size())
#define mset(c, v) memset(c, v, sizeof(c))
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define trace(x...) x
#define print(x...) trace(fprintf(stderr, x))
#define watch(x) trace({auto _VAL = (x); cerr << #x << " = " << _VAL << endl;})
using namespace std;
using ll = long long;
using vi = vector<int>;
using vl = vector<ll>;
using vd = vector<double>;
using point = complex<double>;

template<class K, class V> ostream& operator<<(ostream& out, const pair<K,V>& v) { out<<'('<<v.first<<','<<v.second<<')'; return out;}
template<class C, class=typename C::iterator> struct _cprint { using type = void;}; template<> struct _cprint<string> {};
template<class C, class=typename _cprint<C>::type> ostream& operator<<(ostream& out, const C& v) {for(auto x : v) out<<x<<' '; return out;}
template<class C> inline void chmax(C& x, const C& a) { if (x < a) x = a;}
template<class C> inline void chmin(C& x, const C& a) { if (x > a) x = a;}
template<class C> inline C mod(C a, C b) { return (a%b+b)%b;}
int inv(int a, int p) { return a == 1 ? 1 : ll(p-p/a) * inv(p%a, p) % p;}

template<class C> vi order(C& c) {
  vector<pair<typename C::value_type, int>> seq;
  int cnt = 0;
  for (auto x : c) seq.eb(x, cnt++);
  sort(all(seq));
  vi ret;
  for (auto x : seq) ret.pb(x.second);
  return ret;
}

struct segtree {
  vi val, aux;
  int n;

  segtree(int N) {
    for (n = 1; n < N; n *= 2);
    val.resize(2*n-1);
    aux.resize(2*n-1);
  }

  void delta(int l, int r, int d) { delta(l, r, d, 0, 0, n);}
  void delta(int l, int r, int d, int u, int L, int R) {
    if (l >= R || r <= L || l >= r) return;
    if (l <= L && r >= R) val[u] += d;
    else {
      int M = (L+R)/2;
      delta(l, r, d, 2*u+1, L, M);
      delta(l, r, d, 2*u+2, M, R);
    }

    if (val[u] > 0) aux[u] = R-L;
    else aux[u] = R-L>1 ? aux[2*u+1] + aux[2*u+2] : 0;
  }

  int query(int l, int r) { return query(l, r, 0, 0, n);}
  int query(int l, int r, int u, int L, int R) {
    if (l >= R || r <= L || l >= r) return 0;
    if (l <= L && r >= R) return aux[u];

    if (val[u] > 0) return min(r, R) - max(l, L);
    int M = (L+R)/2;
    return query(l, r, u*2+1, L, M) + query(l, r, u*2+2, M, R);
  }
};

int main() {
  int T;
  cin >> T;
  for (int case_no = 1; case_no <= T; case_no++) {
    int N;
    vi A;
    cin >> N;
    for (int i = 0; i < N; i++) {
      int t;
      cin >> t;
      A.push_back(t);
    }

    vi B = order(A);
    segtree tree(N);
    int ans = 0;
    for (int i : B) {
      ans += min(i - tree.query(0, i), N - 1 - i - tree.query(i, N));
      tree.delta(i, i+1, 1);
    }
    cout << "Case #" << case_no << ": " << ans << endl;
  }
}
