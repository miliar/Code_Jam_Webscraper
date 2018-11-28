#include <algorithm>
#include <cstdlib>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <set>
#include <utility>
#include <vector>
#include <cassert>
#include <iterator>

int cntsmaller[1001][1001];

int solve_this(int n, std::vector<int> const& d) {
  for (int i=0; i<n; ++i) {
    int smaller=0;
    for (int j=i; j<n; ++j) {
      smaller += (d[j] < d[i]);
      cntsmaller[i][j] = smaller;
    }
    smaller=0;
    for (int j=i; j>=0; --j) {
      smaller += (d[j] < d[i]);
      cntsmaller[i][j] = smaller;
    }
    cntsmaller[i][i] = 0;
  }
  int minmoves=std::numeric_limits<int>::max();
  if (n==1) minmoves=0;
  for (int i=1; i<n; ++i) { // position of max
    int moves=0;
    for (int j=0; j<n; ++j) { // item to move
      moves += std::min(cntsmaller[j][i], cntsmaller[j][i-1]);
    }
    //std::cout << "to " << i<<": "<<moves<<'\n';
    minmoves = std::min(minmoves, moves);
  }
  return minmoves;
}

void solve() {
  int n; std::cin >> n;
  std::vector<int> d;
  std::copy_n(std::istream_iterator<int>(std::cin), n, std::back_inserter(d));

  int minmoves=solve_this(n, d);
  int delmoves=0;
  while (delmoves < minmoves) {
    if (d.size()<2)
      break;
    auto it=std::min_element(d.begin(), d.end());
    int pos = it-d.begin();
    delmoves += std::min(pos, (int)d.size()-pos-1);
    d.erase(it);
    minmoves = std::min(minmoves, delmoves+solve_this(d.size(), d));
  }
  std::cout << minmoves;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);

  int num_of_testcases; std::cin >> num_of_testcases;
  for (int testcase=1; testcase<=num_of_testcases; ++testcase) {
    std::cout << "Case #" << testcase << ": ";
    solve();
    std::cout << '\n';
  }
}

/*
 * Local variables:
 * mode:c++
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g -ggdb3 -O0 -Wall -Wextra -std=c++1y upanddown.cc -o upanddown-slow && g++ -std=c++1y -O3 upanddown.cc -o upanddown && for f in *.in; do echo \"--- $f -------------\"; ./upanddown-slow <$f; done"
 * end:
 */
