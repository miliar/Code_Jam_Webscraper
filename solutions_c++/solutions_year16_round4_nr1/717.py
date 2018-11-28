#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vec<int> vi;
const char eol = '\n';

string gen(int n, char init) {
  if (n == 0) return string() + init;

  string a, b;
  if (init == 'R') {
    a = gen(n - 1, 'R');
    b = gen(n - 1, 'S');
  } else if (init == 'P') {
    a = gen(n - 1, 'P');
    b = gen(n - 1, 'R');
  } else if (init == 'S') {
    a = gen(n - 1, 'P');
    b = gen(n - 1, 'S');
  } else {
    assert(false);
  }

  return min(a + b, b + a);
}

bool match(string str, int r, int p, int s) {
  int sr = 0, sp = 0, ss = 0;
  FOR(i, 0, sz(str)) {
    if (str[i] == 'R') sr += 1;
    else if (str[i] == 'P') sp += 1;
    else if (str[i] == 'S') ss += 1;
    else assert(false);
  }
  return sr == r && sp == p && ss == s;
}

void solve(int testcase) {
  cout << "Case #" << testcase << ": ";
  int n, r, p, s;
  cin >> n >> r >> p >> s;
  vec<string> wins = { gen(n, 'R'), gen(n, 'P'), gen(n, 'S') };
  sort(wins.begin(), wins.end());
  FOR(i, 0, sz(wins)) {
    if (match(wins[i], r, p, s)) {
      cout << wins[i] << eol;
      return;
    }
  }
  cout << "IMPOSSIBLE" << eol;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int testcases;
  cin >> testcases;
  FOR(testcase, 1, testcases + 1) {
    cerr << "Case " << testcase << "/" << testcases << endl;
    solve(testcase);
  }

  return 0;
}
