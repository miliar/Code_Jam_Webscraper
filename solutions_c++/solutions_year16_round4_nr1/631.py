#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

void count (const string &s, int &a, int &b, int &c) {
  a = b = c = 0;
  for (int i = 0; i < s.size(); ++i) {
    a += (s[i] == 'P');
    b += (s[i] == 'R');
    c += (s[i] == 'S');
  }
}

void move(string &s) {
  string t = "";
  for (int i = 0; i < s.size(); ++++i) {
    if (s[i] == 'P' && s[i + 1] == 'R')
      t += "PRRS";
    if (s[i] == 'P' && s[i + 1] == 'S')
      t += "PRPS";
    if (s[i] == 'R' && s[i + 1] == 'S')
      t += "PSRS";
  }
  s = t;
}

string find(const int &n, const int &p, const int &r, const int &s) {
  string u = "PR";
  for (int i = 1; i < n; ++i) {
    move(u);
  }
  int a, b, c;
  count (u, a, b, c);
  if (a == p && b == r && c == s)
    return u;
  u = "PS";
  for (int i = 1; i < n; ++i) {
    move(u);
  }
  count (u, a, b, c);
  if (a == p && b == r && c == s)
    return u;
  u = "RS";
  for (int i = 1; i < n; ++i) {
    move(u);
  }
  return u;
}

string order(string &s) {
  for (int i = 1; i < s.size(); i *= 2) {
    for (int j = 0; j < s.size(); j += 2 * i) {
      if (!lexicographical_compare(s.begin()+j, s.begin()+j+i, s.begin()+j+i, s.begin()+j+2*i)) {
        string t = s.substr(j, i);
        s.replace(j, i, s.substr(j + i, i));
        s.replace(j + i, i, t);
      }
    }
  }
  return s;
}

int main() {

#ifdef LocalHost
  //freopen("input", "rt", stdin);
  //freopen("A-small-attempt3.in", "rt", stdin);
  freopen("A-large.in", "rt", stdin);
  freopen("outputAL.txt", "w", stdout);
#endif

  int test; cin >> test;
  for (int t = 0; t < test; ++t) {
    int n, p, r, s;
    cin >> n >> r >> p >> s;
    bool bad;
    bad = ((p - r) < 2 && (p - s) < 2 &&(s - r) < 2 &&(s - p) < 2 && (r - p) < 2 && (r - s) < 2);
    string ans;
    if (bad) {
      ans = find(n, p, r, s);
      ans = order(ans);
    } else {
      ans = "IMPOSSIBLE";
    }
    printf("Case #%d: ", t + 1);
    cout << ans;
    printf("\n");
  }
  return 0;
}
