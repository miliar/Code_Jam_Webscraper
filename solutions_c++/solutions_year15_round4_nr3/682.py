#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
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
int go(map<string, int> &ms, int& k, string s) {
  auto it = ms.find(s);
  if (it == ms.end()) {
    ms[s] = k;
    k += 1;
    return k - 1;
  }
  return it->second;
}

vector<int> cw[300][300];

void solve() {
  int n;
  map<string, int> ms;
  cin >> n;
  string ss;
  getline(cin, ss);
  vector<vi> a(n);
  int k = 0;
  forn(i, n) {
    getline(cin, ss);
    stringstream z(ss);
    while (z >> ss) {
      a[i].pb(go(ms, k, ss));
    }
  }
  // forn(i, n) {
  //   for(int x: a[i]) cout << x << ',';
  //   cout << '\n';
  // }
  forn(i, n) forn(j, n) cw[i][j].clear();
  forn(i, n) forn(j, n) {
    set<int> ss(all(a[i]));
    for(int x: a[j]) if (ss.find(x) != ss.end())
      cw[i][j].pb(x);
  }
  int mans = 1e9;
  forn(mask, (1<<n)) {
    if ((mask&3) != 1) {
      continue;
    }
    vector<bool> mm(n);
    forn(i, n) mm[i] = (mask >> i) & 1;
    vi ans;
    forn(i, n) forn(j, i)
      if (mm[i] != mm[j]) {
        for(int x: cw[i][j]) ans.pb(x);
      }
    sort(all(ans));
    int cans = unique(all(ans)) - ans.begin();
    mans = min(mans, cans);
  }
  cout << mans << '\n';
}

int main() {
  int T;
  cin >> T;
  forn(t, T) {
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
