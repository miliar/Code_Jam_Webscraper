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

double solve() {
  int n, k; cin >> n >> k;
  vector<double> ps;
  double best = 0;
  copy_n(istream_iterator<double>(cin), n, back_inserter(ps));
  for (int mask=0; mask<(1<<n); ++mask) {
    if (__builtin_popcount(mask)!=k)
      continue;
    double dp[16] = {1};
    for (int i=0; i<n; ++i) {
      double p = ps[i];
      if (mask&(1<<i)) {
        for (int j=n-1; j>0; --j)
          dp[j] = p*dp[j-1] + (1-p)*dp[j];
        dp[0] *= (1-p);
      }
    }
    best = max(best, dp[k/2]);
  }
  return best;
}

int_ main() {
  int testcases; cin >> testcases;
  for (auto i : irange(int(1), testcases+1)) {;
    cout << "Case #" << i << ": " << setprecision(100) << solve() << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 b.cc -o b && for f in *.in; do echo \"--- $f -------------\"; ./b <$f; done"
 * end:
 */
