#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
#include <boost/range.hpp>
#include "../../prettyprint.hpp"
using namespace std;
using boost::irange;
using boost::make_iterator_range;

#ifdef NDEBUG
#include <boost/iostreams/stream.hpp>
#include <boost/iostreams/device/null.hpp>
boost::iostreams::stream<boost::iostreams::null_sink> logs((boost::iostreams::null_sink()));
#else
auto& logs = cerr;
#endif

using int_ = int;
#define int int_fast64_t

template <typename C>
bool is_good(int n, C& c) {
  for (int i=0; i<n; ++i) {
    bitset<8> nbs = 0;
    bitset<8> conflicts = 0;
    for (int j=0; j<n; ++j)
      if (c[i][j]) {
        nbs[j] = true;
      }
    for (int j=0; j<n; ++j) {
      if (nbs[j]) {
        for (int k=0; k<n; ++k) {
          if (c[k][j])
            conflicts[k] = true;
        }
      }
    }
    if (conflicts.count() > nbs.count())
      return false;
    if (nbs.count() == 0)
      return false;
  }
  return true;
}

int solve() {
  int n; cin >> n;
  assert(n <= 4);
  array<bitset<4>, 4> bs{};
  for (int i=0; i<n; ++i)
    for (int j=0; j<n; ++j) {
      char x; cin >> x;
      bs[i][j] = x=='1';
    }

  // array<bitset<4>, 4> verybest{};

  int mincost = n*n;
  for (int mask=0; mask<(1<<(n*n)); ++mask) {
    array<bitset<4>, 4> bbs{};
    int cost=0;
    for (int i=0; i<n; ++i)
      for (int j=0; j<n; ++j) {
        if (mask&(1<<(n*i + j))) {
          if (!bs[i][j])
            cost += 1;
          bbs[i][j] = true;
        } else if (bs[i][j]) {
          goto next;
        }
      }
    if (is_good(n, bbs)) {
      // if (cost < mincost)
      //   verybest = bbs;
      mincost = min(mincost, cost);
    }
  next:;
  }
  // for (auto& x : verybest)
  //   cout << x << '\n';
  return mincost;
}

int_ main() {
  int testcases; cin >> testcases;
  for (auto i : irange(int(1), testcases+1)) {;
    cout << "Case #" << i << ": ";
    auto res = solve();
    if (res == -1) cout << "IMPOSSIBLE";
    else cout << res;
    cout << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 d.cc -o d && for f in *.in; do echo \"--- $f -------------\"; ./d <$f; done"
 * end:
 */
