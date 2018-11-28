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

int id;
map<int, string> M[3];
set<string> S;

string go(vi a) {
  forn(i, 3) {
    for(auto e: M[i]) {
      vi b(3);
      for(char c: e.second) {
        if (c == 'R') b[0] += 1;
        if (c == 'P') b[1] += 1;
        if (c == 'S') b[2] += 1;
      }
      if (b == a) return e.second;
    }
  }
  return "";
}

void f(string s) {
  if (s.length() > 8) return ;
  if (!S.insert(s).second) return ;
  auto it = M[id].find(s.length());
  if (it == M[id].end()) M[id][s.length()] = s;
  else uin(it->second, s);
  int n = s.length();
  forn(m, (1 << n)) {
    string t;
    forn(i, n) {
      char c = s[i];
      if (c == 'R') { if ((m >> i)&1) t += "RS"; else t += "SR"; }
      if (c == 'P') { if ((m >> i)&1) t += "PR"; else t += "RP"; }
      if (c == 'S') { if ((m >> i)&1) t += "SP"; else t += "PS"; }
    }
    f(t);
  }
}


void init() {
  id = 0; f("R");
  id = 1; f("P");
  id = 2; f("S");
  forn(i, 3) {
    for(auto e: M[i]) {
      cerr << e.first << ' ' << e.second << '\n';
    }
  }
}

void solve() {
  int n;
  cin >> n;
  vi a(3);
  forn(i, 3) cin >> a[i];
  string r = go(a);
  if (r == "") r = "IMPOSSIBLE";
  cout << r << '\n';
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
