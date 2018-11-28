/*
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            pass System Test!
*/
#include <bits/stdc++.h>
using namespace std;
typedef tuple<uint64_t, int, uint64_t, uint64_t> P;
template <typename T>
std::ostream &operator<<(std::ostream &out, const std::vector<T> &v) {
  if (!v.empty()) {
    out << '[';
    std::copy(v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
    out << "\b\b]";
  }
  return out;
}
template <typename T1, typename T2>
std::ostream &operator<<(std::ostream &out, const std::pair<T1, T2> &p) {
  out << "[" << p.first << ", " << p.second << "]";
  return out;
}
template <class T, class U>
void chmin(T &t, U f) {
  if (t > f) t = f;
}
template <class T, class U>
void chmax(T &t, U f) {
  if (t < f) t = f;
}
template <typename T>
void uniq(vector<T> &v) {
  v.erase(unique(v.begin(), v.end()), v.end());
}

uint64_t pow10(int e) {
  uint64_t ret = 1;
  uint64_t cur = 10;
  while (e) {
    if (e & 1) ret *= cur;
    cur *= cur;
    e >>= 1;
  }
  return ret;
}

pair<int64_t, int64_t> dp[19][10][10][3];
const int SAME = 0, SLARGE = 1, TLARGE = 2;

string solve(const string &S, const string &T) {
  int N = S.size();
  for (int i = 0; i < 19; ++i)
    for (int j = 0; j < 10; ++j)
      for (int k = 0; k < 10; ++k)
        for (int l = 0; l < 3; ++l) dp[i][j][k][l] = {-1, -1};
  dp[0][0][0][0] = {0, 0};
  for (int i = 0; i < N; ++i) {
    for (int s = 0; s < 10; ++s) {
      for (int t = 0; t < 10; ++t) {
        for (int u = 0; u < 3; ++u) {
          if (dp[i][s][t][u].first < 0) continue;
          int64_t ss, tt;
          tie(ss, tt) = dp[i][s][t][u];
          for (int ds = 0; ds < 10; ++ds) {
            if (S[i] != '?') ds = S[i] - '0';

            for (int dt = 0; dt < 10; ++dt) {
              if (T[i] != '?') dt = T[i] - '0';

              int64_t ns = ss * 10 + ds;
              int64_t nt = tt * 10 + dt;
              int64_t cost = abs(ns - nt);
              int nu;
              if (ns == nt)
                nu = SAME;
              else if (ns > nt)
                nu = SLARGE;
              else
                nu = TLARGE;

              int fi, se;
              tie(fi, se) = dp[i + 1][ds][dt][nu];
              if (fi < 0 || abs(fi - se) > cost ||
                  (abs(fi - se) == cost && fi > ns) ||
                  (abs(fi - se) == cost && fi == ns && se > nt)) {
                dp[i + 1][ds][dt][nu] = {ns, nt};
              }

              if (T[i] != '?') break;
            }

            if (S[i] != '?') break;
          }
        }
      }
    }
  }
  int64_t mi = 1e18;
  for (int s = 0; s < 10; ++s) {
    for (int t = 0; t < 10; ++t) {
      for (int u = 0; u < 3; ++u) {
        int fi, se;
        tie(fi, se) = dp[N][s][t][u];
        if (fi < 0) continue;
        chmin(mi, abs(fi - se));
      }
    }
  }

  vector<pair<int64_t, int64_t>> ans;
  for (int s = 0; s < 10; ++s) {
    for (int t = 0; t < 10; ++t) {
      for (int u = 0; u < 3; ++u) {
        int fi, se;
        tie(fi, se) = dp[N][s][t][u];
        if (fi < 0) continue;
        if (abs(fi - se) == mi) ans.push_back({fi, se});
      }
    }
  }
  sort(ans.begin(), ans.end());
  assert(!ans.empty());
  string rS = to_string(ans[0].first);
  while (rS.size() < N) rS = "0" + rS;
  string rT = to_string(ans[0].second);
  while (rT.size() < N) rT = "0" + rT;

  return rS + " " + rT;
}

bool check(const string &S, const int i) {
  string tmpi = to_string(i);
  if (tmpi.size() > S.size()) return false;
  while (tmpi.size() < S.size()) tmpi = "0" + tmpi;
  for (int si = 0; si < S.size(); ++si) {
    if (S[si] != tmpi[si] && S[si] != '?') return false;
  }
  return true;
}

string naive_solve(const string &S, const string &T) {
  vector<tuple<int, int, int>> ans;
  for (int i = 0; i < 1000; ++i) {
    if (!check(S, i)) continue;
    for (int j = 0; j < 1000; ++j) {
      if (!check(T, j)) continue;
      ans.emplace_back(abs(i - j), i, j);
    }
  }
  sort(ans.begin(), ans.end());
  int x, s, t;
  tie(x, s, t) = ans[0];
  string rS = to_string(s);
  while (rS.size() < S.size()) rS = "0" + rS;
  string rT = to_string(t);
  while (rT.size() < S.size()) rT = "0" + rT;

  return rS + " " + rT;
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    string S, T;
    cin >> S >> T;

    cout << "Case #" << testcase << ": ";
    if (solve(S, T) != naive_solve(S, T)) {
      cerr << S << " " << T << endl;
      cerr << solve(S, T) << endl;
      cerr << naive_solve(S, T) << endl;
      assert(false);
    }
    cout << solve(S, T) << endl;
  }
}
