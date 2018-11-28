#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)

#define pb push_back
#define eb emplace_back

#define fi first
#define se second

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<ld, ld> pld;
typedef vector<ld> vld;
typedef vector<pld> vpld;

const ld eps = 1e-9;
const ld pi = acosl(-1.0);

template<typename T> bool uin(T& a, T b) { if (b < a) { a = b; return true; } return false; }
template<typename T> bool uax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

vld go(const vld& p) {
  int n = p.size();
  vld r(n + 1, 0.0);
  r[0] = 1.0;
  for(ld x: p) {
    vld nr(n + 1, 0.0);
    forn(i, n) {
      nr[i] += r[i] * (1 - x);
      if (i + 1 < n) nr[i + 1] += r[i] * x;
    }
    r = nr;
  }
  return r;
}

void solve() {
  int n, k;
  cin >> n >> k;
  vld a(n);
  forn(i, n) cin >> a[i];
  ld ans = 0;
  forn(m, (1 << n)) {
    if (k == __builtin_popcount(m)) {
      vld p;
      forn(i, n) if((m >> i)&1) p.pb(a[i]);
      auto r = go(p);
      uax(ans, r[k / 2]);
    }
  }
  cout << ans << '\n';
}

int main() {
  cout << fixed;
  cout.precision(15);
  int T;
  cin >> T;
  forn(t, T) {
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
