#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

set<double> n_set;
set<double> k_set;
set<double> n_set2;
set<double> k_set2;

int DeceitfulScore() {
  int wins = 0;

  while (!n_set2.empty()) {
    const auto iter = n_set2.begin();

    auto iter2 = k_set2.end();
    --iter2;

    auto iter3 = n_set2.upper_bound(*iter2);
    if (iter3 == n_set2.end()) {
      n_set2.erase(iter);
      k_set2.erase(iter2);
      continue;
    }

    ++wins;
    n_set2.erase(iter3);
    k_set2.erase(iter2);
  }

  return wins;
}

int OptimalScore() {
  int wins = 0;

  while (!n_set.empty()) {
    const auto iter = n_set.begin();

    auto iter2 = k_set.upper_bound(*iter);
    if (iter2 == k_set.end()) {
      iter2 = k_set.begin();
    }

    if (*iter > *iter2) {
      ++wins;
    }

    n_set.erase(iter);
    k_set.erase(iter2);
  }

  return wins;
}

int main() {
  int cases = 0;
  int sz = 0;

  cin >> cases;
  for (int c = 1; c <= cases; ++c) {
    cin >> sz;
    n_set.clear();
    k_set.clear();

    double value;
    for (int idx = 0; idx < sz; ++idx) {
      cin >> value;
      n_set.insert(value);
      n_set2.insert(value);
    }
    for (int idx = 0; idx < sz; ++idx) {
      cin >> value;
      k_set.insert(value);
      k_set2.insert(value);
    }

    cout << "Case #" << c << ": " << DeceitfulScore()
         << ' ' << OptimalScore() << '\n';
  }

  return 0;
}
