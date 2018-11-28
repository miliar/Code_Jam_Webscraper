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

set<vector<bool> > Good;

const int N = 30;
bool a[N][N];
int n;
bool used_a[N];
bool used_b[N];

bool good(int i) {
  if (i == n) return true;
  forn(w, n) if (!used_a[w]) {
    int cb = 0;
    forn(b, n) if (a[w][b] && !used_b[b]) {
      used_a[w] = true;
      used_b[b] = true;

      bool r = good(i + 1);
      ++cb;

      used_a[w] = false;
      used_b[b] = false;

      if (!r) return false;
    }
    if (!cb) return false;
  }
  return true;
}

void init() {
  fore(n, 1, 4) {
    forn(m, (1 << (n*n))) {
      vector<bool> a(n * n);
      forn(i, n * n) a[i] = (m >> i) & 1;
      forn(i, n) forn(j, n) ::a[i][j] = a[i * n + j];
      ::n = n;
      if (good(0)) {
        Good.insert(a);
      }
    }
  }
}

void solve() {
  int n;
  cin >> n;
  vector<bool> a(n*n);
  forn(i, n) {
    string s;
    cin >> s;
    forn(j, n) a[i * n + j] = s[j] == '1';
  }
  int ans = n * n;
  for(const auto& b: Good) if (b.size() == a.size()) {
    int cans = 0;
    forn(i, n * n) {
      if (a[i] && !b[i]) { cans = -1; break; }
      if (!a[i] && b[i]) { cans += 1; }
    }
    if (cans >= 0) uin(ans, cans);
  }
  cout << ans << '\n';
}

int main() {
  init();
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
