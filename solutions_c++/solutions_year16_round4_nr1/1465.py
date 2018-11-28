#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cassert>

using namespace std;

string solve(int N, int R, int P, int S) {
  cout<< N << ", " << R << ", " << P << ", " << S << endl;
  if (N == 0) {
    if (R) return "R";
    if (P) return "P";
    if (S) return "S";
    assert(0);
  }
  long long mn = (1 << N) / 4;
  long long mx = (1 << N) / 2;

  int pr = mn / 2;
  int ps = mn / 2;
  int rs = mn / 2;
  if (N == 2) {
    pr = P / 2 + R / 2;
    ps = P / 2 + S / 2;
    rs = R / 2 + S / 2;
  }

  P -= pr + ps;
  R -= pr + rs;
  S -= ps + rs;
  while (P > 0 && R > 0) {
    P--;
    R--;
    pr++;
  }
  while (P > 0 && S > 0) {
    P--;
    S--;
    ps++;
  }
  while (R > 0 && S > 0) {
    R--;
    S--;
    rs++;
  }

  string B = solve(N - 1, rs, pr, ps);

  string str;
  for (int i = 0; i < B.size(); i++) {
    if (B[i] == 'R') {
      str += "RS";
    } else if (B[i] == 'P') {
      str += "PR";
    } else {
      str += "PS";
    }
  }
  return str;
}

int main() {
  int T; cin >> T;
  map<string, string> mp;
  mp["PR"] = "P";
  mp["PS"] = "S";
  mp["RS"] = "R";
  mp["RP"] = "P";
  mp["SP"] = "S";
  mp["SR"] = "R";

  for (int t = 1; t <= T; t++) {
    long long N, R, P, S;
    cin >> N >> R >> P >> S;
    cout << "Case #" << t << ": ";

    string str;
    for (int i = 0; i < P; i++) {
      str += "P";
    }
    for (int i = 0; i < R; i++) {
      str += "R";
    }
    for (int i = 0; i < S; i++) {
      str += "S";
    }

    bool found = false;
    do  {
      string T = str;
      bool fail = false;
      while (T.size() > 1) {
        string Q;
        for (int i = 0; i < T.size(); i += 2) {
          string add = mp[T.substr(i, 2)];
          fail |= add.size() == 0;
          Q += add;
        }
        T = Q;
      }
      if (!fail) {
        cout << str << endl;
        found = true;
        break;
      }
    } while(next_permutation(str.begin(), str.end()));

    if (!found) {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
