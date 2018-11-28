#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);

void rd() { }
template<typename... T> void rd(int &h, T &... t) { scanf("%d", &h); rd(t...); }
template<typename... T> void rd(long long &h, T &... t) { scanf("%lld", &h); rd(t...); }
template<typename... T> void rd(double &h, T &... t) { scanf("%lf", &h); rd(t...); }

int tests;
int n, r, p, s;

char win(char x, char y) {
  if (x == y) return -1;
  if (x == 'R') {
    if (y == 'S') return x;
    return y;
  }
  if (x == 'S') {
    if (y == 'R') return y;
    return x;
  }
  if (x == 'P') {
    if (y == 'R') return x;
    return y;
  }
}

bool check(string s) {
  string cur = s;
  while (cur.length() != 1) {
    string reduce;
    for (int i = 0; i < cur.length(); i += 2) {
      char t = win(cur[i], cur[i + 1]);
      if (t < 0) return false;
      reduce += t;
    }
    cur = reduce;
  }
  return true;
}

int main() {
  freopen("A-small-attempt0.in", "r", stdin);

  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    rd(n, r, p, s);
    n = 1 << n;
    string x;
    for (int i = 1; i <= r; ++i) x += 'R';
    for (int i = 1; i <= p; ++i) x += 'P';
    for (int i = 1; i <= s; ++i) x += 'S';
    sort(x.begin(), x.end());
    string answer;
    do {
      if (check(x)) {
        if (answer.empty() || x < answer) answer = x;
      }
    } while (next_permutation(x.begin(), x.end()));
    printf("Case #%d: ", tt);
    if (answer.empty()) puts("IMPOSSIBLE");
    else cout << answer << endl;
  }

  return 0;
}
