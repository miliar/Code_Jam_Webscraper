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

void solve() {
  int n, x; std::cin >> n >> x;
  std::vector<int> d;
  std::copy_n(std::istream_iterator<int>(std::cin), n, std::back_inserter(d));
  std::sort(d.rbegin(), d.rend());
  
  int disks_used=0;
  std::multiset<int> disks;
  for (int s : d) {
    auto it = disks.lower_bound(s);
    if (it != disks.end() && *it >= s) {
      disks.erase(it);
      disks_used++;
    } else {
      disks.insert(x - s);
    }
  }
  disks_used += disks.size();
  std::cout << disks_used;
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
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g -ggdb3 -O0 -Wall -Wextra -std=c++1y datapacking.cc -o datapacking-slow && g++ -O3 datapacking.cc -o datapacking && for f in *.in; do echo \"--- $f -------------\"; ./datapacking-slow <$f; done"
 * end:
 */
