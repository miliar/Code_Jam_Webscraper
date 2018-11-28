#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

struct Game {
  int r, p, s;
  int w;
  bool operator<(const Game& second) const {
    if (r != second.r) {
      return r < second.r;
    } else if (p != second.p) {
      return p < second.p;
    } else if (s != second.s) {
      return s < second.s;
    } else {
      return w < second.w;
    }
  }
};

const std::string kFail = "IMPOSSIBLE";

map<Game, std::string> dp;

std::string DFS(const Game& g) {
  if (dp.count(g)) {
    return dp[g];
  }
  if (g.w == 0 && g.r == 0) {
    return kFail;
  }
  if (g.w == 1 && g.p == 0) {
    return kFail;
  }
  if (g.w == 2 && g.s == 0) {
    return kFail;
  }
  int total = g.r + g.p + g.s;
  if (total == 1) {
    if (g.r == 1 && g.w == 0) {
      return "R";
    } else if (g.p == 1 && g.w == 1) {
      return "P";
    } else if (g.s == 1  && g.w == 2) {
      return "S";
    } else {
      return kFail;
    }
  }
  if (2 * g.s > total || 2 * g.r > total || 2 * g.p > total) {
    return kFail;
  }
  string answer = "Z";
  for (int r = total / 2 - g.p - g.s; r <= std::min(total / 2, g.r); ++r) {
    for (int p = total / 2 - r - g.s; p <= g.p && p + r <= total / 2; ++p) {
      if (total / 2 - r - p > g.s) {
        continue;
      }
      Game g2 = {r, p, total / 2 - r - p, 0};
      Game g3 = {g.r - r, g.p - p, g.s - g2.s, 0};
      if (g.w == 0) {
        g2.w = 0;
        g3.w = 2;
      } else if (g.w == 1) {
        g2.w = 1;
        g3.w = 0;
      } else {
        g2.w = 2;
        g3.w = 1;
      }
      std::string s1 = DFS(g2);
      std::string s2 = DFS(g3);
      if (s1 != kFail && s2 != kFail) {
        answer = min(answer, std::min(s1 + s2, s2 + s1));
      }
      swap(g2.w, g3.w);
      s1 = DFS(g2);
      s2 = DFS(g3);
      if (s1 != kFail && s2 != kFail) {
        answer = min(answer, min(s1 + s2, s2 + s1));
      }
    }
  }
  return dp[g] = (answer != "Z" ? answer : kFail);
}

std::string sol[5044][3];

void Solve() {
  int n, r, p, s;
  cin >> n >> r >> p >> s;
  /*
  cerr << "Start";
  n = 4096;
  r = rand() % 4096;
  p = rand() % 4096;
  s = n - r - p;
  Game g1 = {r, p, s, 0};
  Game g2 = {r, p, s, 1};
  Game g3 = {r, p, s, 2};
  string a1 = DFS(g1);
  string a2 = DFS(g2);
  string a3 = DFS(g3);
  string answer = "Z";
  if (a1 != kFail) {
    answer = min(answer, a1);
  }
  if (a2 != kFail) {
    answer = min(answer, a2);
  }
  if (a3 != kFail) {
    answer = min(answer, a3);
  }
  if (answer == "Z") {
    answer = kFail;
  }
  cout << answer << std::endl;*/
  sol[0][0] = "R"; 
  sol[0][1] = "P"; 
  sol[0][2] = "S";
  for (int i = 0; i < 15 ; i++) {
    sol[i + 1][0] = std::min(sol[i][0] + sol[i][2], sol[i][2] + sol[i][0]);
    sol[i + 1][1] = std::min(sol[i][1] + sol[i][0], sol[i][0] + sol[i][1]);
    sol[i + 1][2] = std::min(sol[i][2] + sol[i][1], sol[i][1] + sol[i][2]);
  }
  string ans = "Z";
  for (int i = 0; i < 3; ++i) {
    int qr = 0, qp = 0, qs = 0;
    for (int j = 0; j < sol[n][i].size(); ++j) {
      if (sol[n][i][j] == 'R') {
        ++qr;
      } else if (sol[n][i][j] == 'S') {
        ++qs;
      } else {
        ++qp;
      }
    }
    if (qr == r && qp == p && qs == s) {
      ans = min(ans, sol[n][i]);
    }
  }
  if (ans == "Z") {
    ans = kFail;
  }
  cout << ans << std::endl;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
