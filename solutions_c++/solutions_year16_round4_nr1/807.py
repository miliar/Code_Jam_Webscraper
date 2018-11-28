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

char get_loser(char c) {
  if (c == 'P') {
    return 'R';
  } else if (c == 'S') {
    return 'P';
  } else {
    return 'S';
  }
}

string dfs(char seed, int N) {
  if (N == 1) {
    string s = "";
    s += seed;
    s += get_loser(seed);
    sort(s.begin(), s.end());
    return s;
  }
  string a = dfs(seed, N - 1);
  string b = dfs(get_loser(seed), N - 1);
  if (a < b) {
    return a + b;
  }
  return b + a;
}

string construct(string seed, int N) {
  while (N--) {
    string next = "";
    for (int i = 0; i < seed.size(); ++i) {
      next += seed[i];
      if (seed[i] == 'P') {
        next += 'R';
      } else if (seed[i] == 'S') {
        next += 'P';
      } else {
        next += 'S';
      }
    }
    seed = next;
  }
  return seed;
}

string solve(int N, int R, int P, int S) {
  string seeds = "RSP";
  for (char seed : seeds) {
    string c = dfs(seed, N);
    int r = 0, s = 0, p = 0;
    for (char cc : c)
      if (cc == 'R')
        r++;
      else if (cc == 'S')
        s++;
      else
        p++;
    if (R == r && S == s && P == p) return c;
  }

  return "IMPOSSIBLE";
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  // for (int i = 1; i <= 12; ++i) {
  //   cout << construct("R", i) << endl;
  // }

  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    cout << "Case #" << testcase << ": " ;
    string ans = solve(N, R, P, S);
    cout << ans << endl;
  }
}
