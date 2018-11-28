#include <vector>
#include <iterator>
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>

using namespace std;

string solve(vector<int> & n_blocks, vector<int> & k_blocks) {
  sort(n_blocks.begin(), n_blocks.end());
  sort(k_blocks.begin(), k_blocks.end());

  ostringstream os;

  // deceiptful war
  {
    auto nbs_begin = n_blocks.begin();
    auto nbs_end   = n_blocks.end();

    auto kbs_begin = k_blocks.begin();
    auto kbs_end   = k_blocks.end();


    int score = 0;
    while (nbs_end != nbs_begin) {
      if (*nbs_begin > *kbs_begin) {
        ++score;
        ++kbs_begin;
        ++nbs_begin;
        continue;
      } else {
        ++nbs_begin;
        --kbs_end;
      }
    }

    os << score;
  }
  os << " ";
  // war
  {
    set<int> kbs;
    std::copy(k_blocks.begin(), k_blocks.end(), std::inserter(kbs, kbs.begin()));

    int score = 0;
    for (auto n_block : n_blocks) {
      auto k_it = kbs.upper_bound(n_block);
      if (k_it == kbs.end()) {
        ++score;
        // no need to delete from kbs, since next elements are larger too
        // FIXME: could break here too
      } else {
        kbs.erase(k_it);
      }
    }

    os << score;
  }
  return os.str();
}

int main() {
  int t;
  cin >> t;

  for (int test_case = 0; test_case < t; ++test_case) {
    auto read_blocks = [](int n) {
      int const five_k = 10e5;
      vector<int> res;
      for (int s = 0; s < n; ++s) {
        double val;
        cin >> val;
        res.push_back(val * five_k);
      }

      return res;
    };

    int n;
    cin >> n;

    auto n_blocks = read_blocks(n);
    auto k_blocks = read_blocks(n);

    std::cout
      << "Case #" << (test_case + 1) << ": "
      << solve(n_blocks, k_blocks)
      << "\n";
  }
}

