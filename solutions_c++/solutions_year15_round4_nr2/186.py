#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
#include <boost/range.hpp>
#include "../../prettyprint.hpp"
#include <boost/rational.hpp>
using namespace std;
using boost::irange;
using boost::make_iterator_range;

#define NDEBUG
#ifdef NDEBUG
#include <boost/iostreams/stream.hpp>
#include <boost/iostreams/device/null.hpp>
boost::iostreams::stream<boost::iostreams::null_sink> logs((boost::iostreams::null_sink()));
#else
auto& logs = cerr;
#endif

using real_int = int;
#define int int64_t

//const double eps = 1e-10;

template <typename T> int sign(T val) {
    return (T(0) < val) - (val < T(0));
}

using rat = boost::rational<int>;

rat read_rat() {
  string s; cin >> s;
  auto p = s.find('.');
  if (p == string::npos)
    return stoi(s);
  int a = stoi(s.substr(0, p) + s.substr(p+1));
  int b = stoi("1" + string(s.size() - p - 1, '0'));

  //logs << "read " << s << " as " << a<< "/" << b << '\n';
  return rat(a, b);
}

double solve() {
  int n; cin >> n;
  rat v=read_rat(), x=read_rat();
  rat totrate = 0, tottemp=0;
  //             temp, rate
  vector<tuple<rat, rat> > sources;
  for (int _ : irange<int>(0, n)) {
    (void)_;
    rat r=read_rat(), c=read_rat();
    c -= x;
    totrate += r;
    tottemp += r*c;
    sources.emplace_back(c, r);
  }
  sort(sources.begin(), sources.end());
  // if (-eps <= tottemp && tottemp <= eps)
  //   return v/totrate;
  auto i     = tottemp<0 ? 0 : (int)sources.size() - 1;
  auto last  = tottemp<0 ? (int)sources.size() : -1;
  auto delta = tottemp<0 ? 1 : -1;
  logs << '\n';
  for (; i != last; i += delta) {
    if (tottemp == 0) {
      return boost::rational_cast<double>(v/totrate);
    }
    rat temp, rate;
    tie(temp, rate) = sources[i];
    logs << "got total temp/rate of " << tottemp << "/" << totrate <<" and try to remove " << temp << "/" << rate << '\n';
    if (temp == 0 || sign(temp) != sign(tottemp))
      return -1;
    rat superflous = min(static_cast<rat>(1), tottemp/(temp*rate));
    logs << superflous << " " << tottemp - temp*rate << "!\n";
    totrate -= superflous*rate;
    tottemp -= superflous*temp*rate;
    logs << "remove " << superflous << " and get " << ' ' << tottemp << ' ' << totrate << '\n';
    if (tottemp == 0) {
      if (totrate == 0)
         return -1;
      return boost::rational_cast<double>(v/totrate);
    }
    assert(superflous==1);
  }
  return -1;
}

real_int main() {
  int testcases; cin >> testcases;
  for (auto i : irange<int>(1, testcases+1)) {;
    cout << "Case #" << i << ": ";
    double x = solve();
    if (x == -1)
      cout << "IMPOSSIBLE";
    else
      cout << setprecision(20) << fixed << x;
    cout << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 kiddie.cc -o kiddie && for f in *.in; do echo \"--- $f -------------\"; ./kiddie <$f; done"
 * end:
 */

