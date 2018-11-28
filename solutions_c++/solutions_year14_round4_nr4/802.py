#include <cstdio>
#include <cassert>

#include <set>
#include <iostream>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x" = " << x << endl
#define _ << " _ " <<

typedef long long llint;

int M, N;
string s[20];

int ans, cnt;
vector<string> v[20];

int calc(vector<string> v) {
  set<string> s;
  s.insert("");
  for (auto w : v)
    REP(i, (int) w.size() + 1)
      s.insert(w.substr(0, i));
  return s.size();
}

void rec(int x) {
  if (x == M) {
    bool ok = true;
    REP(i, N) if (v[i].empty()) ok = false;
    if (!ok) return;

    int cost = 0;
    REP(i, N) cost += calc(v[i]);

    if (cost > ans) {
      ans = cost;
      cnt = 0;
    }
    if (cost == ans) ++cnt;
    return;
  }

  REP(i, N) {
    v[i].push_back(s[x]);
    rec(x + 1);
    v[i].pop_back();
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tt = 1; tt <= T; ++tt) {
    cin >> M >> N;
    REP(i, M) cin >> s[i];
    sort(s, s+M);

    ans = -1;
    rec(0);

    printf("Case #%d: %d %d\n", tt, ans, cnt);
  }
  return 0;
}
