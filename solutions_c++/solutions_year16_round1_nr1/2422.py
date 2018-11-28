#include <bits/stdc++.h>

using namespace std;

template<class T> inline T sqr(const T& a) {
  return a * a;
}

template<class T> inline T middle(const T &a, const T &b) {
  return (a + b) / 2;
}

template<class T> inline int len(const T &c) {
  return static_cast<int>(c.size());
}

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 100;

void HandleCase() {
  string s;
  getline(cin, s);
  int n = len(s);
  vector<int> pmax(n, 0);
  for (int i = 1; i < n; ++i) {
    int prev = pmax[i - 1];
    if (s[prev] > s[i]) {
      pmax[i] = prev;
    } else {
      pmax[i] = i;
    }
  }
  int j = n;
  string ans;
  string suf;
  while (j >= 0) {
    int next = j > 0 ? pmax[j - 1] : -1;
    if (j < n) {
      ans.push_back(s[j]);
    }
    if (next >= 0 && j - next > 1) {
      suf = s.substr(next + 1, j - next - 1) + suf;
    }
    j = next;
  }
  ans += suf;
  printf("%s\n", ans.c_str());
}

int main() {
  int tests;
  scanf("%d\n", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d: ", test);
    HandleCase();
  }
  return 0;
}
