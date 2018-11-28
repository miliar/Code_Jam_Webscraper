#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
#include <boost/range.hpp>
#include "../../prettyprint.hpp"
using namespace std;
using boost::irange;
using boost::make_iterator_range;

using int_ = int;
#define int int_fast64_t

struct salfun {
  // time, inc
  map<int, int> sweep;
  void clip_and_inc(int min, int max) {
    map<int, int> next;
    int time=numeric_limits<int>::min(), val=0;
    sweep[min] += 1;
    sweep[max+1] -= 1;
    for (auto it=sweep.begin(); it!=sweep.end() && it->first <= max; ++it) {
      int t=it->first;
      if (t >= min && time < min)
        next[min] = val;
      if (min <= t && t <= max)
        next[t] += it->second;
      time = t;
      val += it->second;
    }
    next[max+1] -= val;
    sweep = move(next);
  }
  void merge(salfun const& o) {
    for (auto& p : o.sweep)
      sweep[p.first] += p.second;
  }
  int maximum() {
    int best=0, val=0;
    for (auto& p : sweep) {
      val += p.second;
      best = max(best, val);
    }
    return best;
  }
};

vector<vector<int> > g;
vector<int> sal;
int d;

salfun dfs(int i) {
  salfun res;
  for (auto& c : g[i])
    res.merge(dfs(c));
  res.clip_and_inc(sal[i]-d, sal[i]);
  return res;
}

int solve() {
  int n, d; cin >> n >> d;
  int s0, as, cs, rs; cin >> s0 >> as >> cs >> rs;
  int m0, am, cm, rm; cin >> m0 >> am >> cm >> rm;

  sal.clear(); sal.reserve(n); sal.push_back(s0);
  vector<int> par; par.reserve(n); par.push_back(m0);
  for (int i=1; i<n; ++i) {
    sal.push_back((as*sal.back() + cs)%rs);
    par.push_back((am*par.back() + cm)%rm);
  }
  ::d = d;
  g.clear();
  g.resize(n);
  
  par[0]=0;
  for (int i=1; i<n; ++i) {
    par[i] %= i;
    g[par[i]].push_back(i);
  }
  return dfs(0).maximum();
}

int_ main() {
  int testcases; cin >> testcases;
  for (auto i : irange(int(1), testcases+1)) {;
    cout << "Case #" << i << ": " << solve() << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 a.cc -o a && for f in *.in; do echo \"--- $f -------------\"; ./a <$f; done"
 * end:
 */

