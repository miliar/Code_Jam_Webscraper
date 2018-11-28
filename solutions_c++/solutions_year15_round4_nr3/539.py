#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

typedef unsigned long long Hash;
typedef pair<int, Hash> pih;

pih describe(const string &s) {
  Hash h = 0;
  for (char c : s)
    h = h * 33 + (c - 'a' + 1);
  return pih(s.size(), h);
}

typedef vector<pih> sentence;
vector<sentence> S;

#define MAXS 10
struct Set {
  vector<pih> s;
  Set() {
    s.reserve(1200);
  }
  inline void insert(pih t) {
    s.push_back(t);
  }
  inline void clean() {
    sort(s.begin(), s.end());
    s.resize(unique(s.begin(), s.end())-s.begin());
  }
  int intersect(Set &other) {
    int lans = 0;
    vector<pih>::iterator it = s.begin(), jt = other.s.begin();
    while (it != s.end() and jt != other.s.end()) {
      if (*it < *jt) {
        ++it;
      } else if (*jt < *it) {
        ++jt;
      } else {
        ++it;
        ++jt;
        ++lans;
      }
    }
    return lans;
  }
};

inline void fill(Set &c, sentence s) {
  for (pih &t : s)
    c.insert(t);
}

int solve() {
  int n;
  string s;
  cin >> n;
  getline(cin, s);
  S.assign(n, sentence());
  for (int i = 0; i < n; ++i) {
    getline(cin, s);
    stringstream ss(s);
    while (ss >> s)
      S[i].push_back(describe(s));
  }
  int limit = (1 << (n-2));
  vector<int> ans(limit);
# pragma omp parallel for num_threads(4)
  for (int mask = 0; mask < limit; ++mask) {
    Set lang[2];
    fill(lang[0], S[0]);
    fill(lang[1], S[1]);
    for (int i = 2; i < n; ++i) {
      int p = (mask & (1 << (i-2))) >> (i-2);
      fill(lang[p], S[i]);
    }
    lang[0].clean();
    lang[1].clean();
    ans[mask] = lang[0].intersect(lang[1]);
  }
  int r = ans[0];
  for (int i = 1; i < limit; ++i)
    r = min(r, ans[i]);
  return r;
}

int main() {
  ios::sync_with_stdio(0);
  int tc;
  cin >> tc;
  for (int cs = 1; cs <= tc; ++cs) {
    cout << "Case #" << cs << ": ";
    cout << solve();
    cout << endl;
  }
  return 0;
}

