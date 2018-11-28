#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")

#include <bits/stdc++.h>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = int64_t;

const string kFail = "ZZZ";

struct State {
  int n, r, p, s;

  bool operator<(const State& other) const {
    if (n != other.n) return n < other.n;
    if (r != other.r) return r < other.r;
    if (p != other.p) return p < other.p;
    return s < other.s;
  }
};

using Result = map<char, string>;

map<State, Result> cache;

char get_winner(char x, char y) {
  assert(x != y);
  if (x > y) swap(x, y);
  if (x == 'P') {
    if (y == 'R') return 'P';
    else return 'S';
  } else {
    assert(x == 'R' && y == 'S');
    return 'R';
  }
}

Result rec(int n, int r, int p, int s) {
  assert(r >= 0 && p >= 0 && s >= 0);
  assert(r + p + s == (1 << n));
  State state{n, r, p, s};
  if (cache.count(state)) return cache[state];
  Result results;

  {
    results['R'] = kFail;
    results['P'] = kFail;
    results['S'] = kFail;
  }

  if (n == 0) {
    if (r != 0) results['R'] = "R";
    else if (p != 0) results['P'] = "P";
    else results['S'] = "S";
  } else {
    int below = (1 << (n - 1));
    for (int rl = 0; rl <= below && rl <= r; rl++) {
      for (int pl = 0; rl + pl <= below && pl <= p; pl++) {
        int sl = below - rl - pl;
        if (sl > s) continue;
        assert(sl <= s);
        auto left = rec(n - 1, rl, pl, sl);
        auto right = rec(n - 1, r - rl, p - pl, s - sl);
        for (const auto& p0 : left) {
          for (const auto& p1 : right) {
            if (p0.first != p1.first && p0.second != kFail && p1.second != kFail) {
              auto winner = get_winner(p0.first, p1.first);
              auto res = p0.second + p1.second;
              results[winner] = min(results[winner], p0.second + p1.second);
            }
          }
        }
      }
    }
  }

  return cache[state] = results;
}

void solve() {
  int n, r, p, s;
  cin >> n >> r >> p >> s;
  Result results = rec(n, r, p, s);
  string res = kFail;
  for (auto p : results)
    res = min(res, p.second);
  cout << (res == kFail ? "IMPOSSIBLE" : res) << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;

  for (int test = 1; test <= tests; test++) {
    cout << "Case #" << test << ": ";
    solve();
  }

  return 0;
}
