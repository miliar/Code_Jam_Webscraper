#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "A"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

bool IsGood(string s) {
  while (s.length() > 1) {
    string t = "";
    for (int i = 0; i < s.length(); i += 2) {
      if (s[i] == s[i + 1]) {
        return false;
      }
      if (s[i] == 'P') {
        if (s[i + 1] == 'R') {
          t += 'P';
        } else {
          t += 'S';
        }
      } else if (s[i] == 'R') {
        if (s[i + 1] == 'S') {
          t += 'R';
        } else {
          t += 'P';
        }
      } else {
        if (s[i + 1] == 'P') {
          t += 'S';
        } else {
          t += 'R';
        }
      }
    }
    s = t;
  }
  return true;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    /*string S;
    for (int i = 0; i < p; ++i) {
      S += 'P';
    }
    for (int i = 0; i < r; ++i) {
      S += 'R';
    }
    for (int i = 0; i < s; ++i) {
      S += 'S';
    }
    bool good = false;
    do {
      if (IsGood(S)) {
        good = true;
        break;
      }
    } while (next_permutation(S.begin(), S.end()));*/
    vector<string> minP(n + 1), minS(n + 1), minR(n + 1);
    minP[0] = "P";
    minR[0] = "R";
    minS[0] = "S";
    for (int i = 1; i <= n; ++i) {
      minP[i] = min(minP[i - 1] + minR[i - 1], minR[i - 1] + minP[i - 1]);
      minR[i] = min(minR[i - 1] + minS[i - 1], minS[i - 1] + minR[i - 1]);
      minS[i] = min(minP[i - 1] + minS[i - 1], minS[i - 1] + minP[i - 1]);
    }
    string S[3];
    S[0] = minP[n];
    S[1] = minR[n];
    S[2] = minS[n];
    string res = "IMPOSSIBLE";
    for (int i = 0; i < 3; ++i) {
      int cntp = count(S[i].begin(), S[i].end(), 'P');
      int cntr = count(S[i].begin(), S[i].end(), 'R');
      int cnts = count(S[i].begin(), S[i].end(), 'S');
      if (cntp == p && cntr == r && cnts == s && (res == "IMPOSSIBLE" || (res != "IMPOSSIBLE" && S[i] < res))) {
        res = S[i];
      }
    }
    cout << "Case #" << (test_index + 1) << ": " << res << endl;
    cerr << "Case #" << (test_index + 1) << ": " << res << endl;
  }
  return 0;
}
