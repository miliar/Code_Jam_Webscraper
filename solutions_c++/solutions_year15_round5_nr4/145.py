#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
#include <boost/range.hpp>
using namespace std;
using boost::irange;
using boost::make_iterator_range;

using int_ = int;
#define int int_fast64_t

vector<int> elems;

void doit(vector<int> v) {
  assert(v[0] == 0);
  if (v.size() == 1)
    return;
  assert(!v.empty());
  assert(is_sorted(v.begin(), v.end()));
  auto x = v[1];
  queue<int> has_no_x;
  vector<int> next;
  for (int i=v.size()-1; i>=0; --i) {
    if (!has_no_x.empty() && v[i] == has_no_x.front()) {
      has_no_x.pop();
      next.push_back(v[i]);
    } else {
      has_no_x.push(v[i] - x);
    }
  }
  reverse(next.begin(), next.end());
  elems.push_back(x);
  doit(next);
}

void solve() {
  int p; cin >> p;
  vector<pair<int, int> > freq(p);
  for (int i : irange(int(0), p))
    cin >> freq[i].first;
  for (int i : irange(int(0), p))
    cin >> freq[i].second;
  vector<int> v;
  for (auto& p : freq) {
    for (int _ : irange(int(0), p.second)) {
      (void)_;
      v.push_back(p.first);
    }
  }
  assert(is_sorted(v.begin(), v.end()));
  elems.clear();
  doit(v);
  assert(is_sorted(elems.begin(), elems.end()));
  for (auto x : elems)
    cout << ' ' << x;
}

int_ main() {
  int testcases; cin >> testcases;
  for (auto i : irange(int(1), testcases+1)) {;
    cout << "Case #" << i << ":";
    solve();
    cout << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 d.cc -o d && for f in *.in; do echo \"--- $f -------------\"; ./d <$f; done"
 * end:
 */

