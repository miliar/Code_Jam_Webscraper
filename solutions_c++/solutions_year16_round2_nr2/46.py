#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

string s, t;
LL X, Y;

void fill(string &s, LL n) {
  for (int i = s.size() - 1; i >= 0; --i) {
    s[i] = '0' + n % 10;
    n /= 10;
  }
}

const LL inf = 1ll << 60;
struct Node {
  LL mx, a, b;
  Node(): mx(inf), a(inf), b(inf) {}
  Node(LL u, LL v, LL w): mx(u), a(v), b(w) {}
  bool operator < (const Node &rhs) const {
    return mx < rhs.mx || (mx == rhs.mx && a < rhs.a) || (mx == rhs.mx && a == rhs.a && b < rhs.b);
  }
  void upd() {
    if (mx < abs(X - Y) || (mx == abs(X - Y) && a < X) || (mx == abs(X - Y) && a == X && b < Y)) X = a, Y = b;
  }
} dp[20][2];


void solve1() {
  for (int i = 0; i < 20; ++i) dp[i][0] = dp[i][1] = Node();
  dp[0][0].mx = dp[0][0].a = dp[0][0].b = 0;
  int n = s.size();
  for (int i = 0; i < n; ++i) {
    for (int e = 0; e < 2; ++e) {
      if (dp[i][e].mx == inf) continue;
      for (int ds = 0; ds < 10; ++ds) {
        if (s[i] != '?' && ds != s[i] - '0') continue;
        for (int dt = 0; dt < 10; ++dt) {
          if (t[i] != '?' && dt != t[i] - '0') continue;
          if (e == 0 && ds < dt) continue;
          int o = e | ds > dt;
          Node now = Node(dp[i][e].mx * 10 + ds - dt,
                          dp[i][e].a * 10 + ds,
                          dp[i][e].b * 10 + dt);
          if (now < dp[i + 1][o]) dp[i + 1][o] = now;
        }
      }
    }
  }
  dp[n][0].upd(); dp[n][1].upd();
}

void solve2() {
  for (int i = 0; i < 20; ++i) dp[i][0] = dp[i][1] = Node();
  dp[0][0].mx = dp[0][0].a = dp[0][0].b = 0;
  int n = s.size();
  for (int i = 0; i < n; ++i) {
    for (int e = 0; e < 2; ++e) {
      if (dp[i][e].mx == inf) continue;
      for (int ds = 0; ds < 10; ++ds) {
        if (s[i] != '?' && ds != s[i] - '0') continue;
        for (int dt = 0; dt < 10; ++dt) {
          if (t[i] != '?' && dt != t[i] - '0') continue;
          if (e == 0 && ds > dt) continue;
          int o = e | ds < dt;
          Node now = Node(dp[i][e].mx * 10 + dt - ds,
                          dp[i][e].a * 10 + ds,
                          dp[i][e].b * 10 + dt);
          if (now < dp[i + 1][o]) dp[i + 1][o] = now;
        }
      }
    }
  }
  dp[n][0].upd(); dp[n][1].upd();
}

void run(int cas) {
  printf("Case #%d: ", cas);
  cin >> s >> t;
  X = 0, Y = inf;
  solve1();
  solve2();
  fill(s, X); fill(t, Y);
  printf("%s %s\n", s.c_str(), t.c_str());
}

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) run(cas);
  return 0;
}
