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
#include <memory>

typedef int real_int;
#define int long long int
int n;

int max_count;
int num_max;

int cnt_trie(std::vector<std::string> strs) {
  std::set<std::string> set;
  for (auto& s : strs)
    for (int i=0; i<=(int)s.size(); ++i)
      set.insert(s.substr(0, i));
  return set.size();
}

void
bruteforce(std::vector<std::vector<std::string> > servers,
	   std::vector<std::string> left) {
  if (!left.empty()) {
    for (int i=0; i<n; ++i) {
      auto back=std::move(left.back()); left.pop_back();
      servers[i].push_back(back);
      bruteforce(servers, left);
      servers[i].pop_back();
      left.push_back(std::move(back));
    }
    return;
  }

  for (auto v : servers)
    if (v.empty())
      return;

  int cnt=0;
  for (auto const& v : servers)
    cnt += cnt_trie(v);
  if (max_count == cnt) {
    num_max++;
  } else if (cnt > max_count) {
    max_count=cnt;
    num_max=1;
  }
}

void solve() {
  max_count=0;
  num_max=0;

  int m; std::cin >> m >> n;
  std::vector<std::string> strs;
  std::copy_n(std::istream_iterator<std::string>(std::cin), m, std::back_inserter(strs));
  std::vector<std::vector<std::string> > servers(n);
  bruteforce(servers, strs);
  std::cout << max_count << " " << num_max%1000000007;
}

real_int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);

  int num_of_testcases; std::cin >> num_of_testcases;
  for (int testcase=1; testcase<=num_of_testcases; ++testcase) {
    std::cout << "Case #" << testcase << ": ";
    solve();
    std::cout << std::endl;
  }
}

/*
 * Local variables:
 * mode:c++
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g -ggdb3 -O0 -Wall -Wextra -std=c++1y trie.cc -o trie-slow && g++ -std=c++1y -O3 trie.cc -o trie && for f in *.in; do echo \"--- $f -------------\"; ./trie-slow <$f; done"
 * end:
 */
