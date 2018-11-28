// {{{ C++ headers
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <forward_list>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <valarray>
#include <vector>
/// }}}

class Problem {
public:
  Problem(int case_num) : case_num_(case_num) {}
  ~Problem() {}

  void Input();
  void Solve();
  void Output() const;

  static void Initialize();
  static void Finalize();

private:
  int64_t GetBestPlace(int64_t team_num);
  int64_t GetWorstPlace(int64_t team_num);

  int case_num_;

  int64_t log_num_teams_;
  int64_t num_prizes_;

  int64_t max_must_;
  int64_t max_could_;

  int64_t num_teams_;
};

void Problem::Input() {
  std::cin >> log_num_teams_ >> num_prizes_;
}

void Problem::Solve() {
  num_teams_ = 1LL << log_num_teams_;

  {
    int64_t first = 0;
    int64_t length = num_teams_;
    while (length > 0) {
      int64_t half = length / 2;
      int64_t middle = first + half;
      if (num_prizes_ - 1 < GetWorstPlace(middle)) {
        length = half;
      } else {
        first = middle + 1;
        length -= half + 1;
      }
    }
    max_must_ = first - 1;
  }

  {
    int64_t first = 0;
    int64_t length = num_teams_;
    while (length > 0) {
      int64_t half = length / 2;
      int64_t middle = first + half;
      if (num_prizes_ - 1 < GetBestPlace(middle)) {
        length = half;
      } else {
        first = middle + 1;
        length -= half + 1;
      }
    }
    max_could_ = first - 1;
  }
}

void Problem::Output() const {
  std::cout << "Case #" << case_num_ << ": " << max_must_ << " " << max_could_ << std::endl;
}

void Problem::Initialize() {
}

void Problem::Finalize() {
}

int64_t Problem::GetBestPlace(int64_t team_num) {
  int64_t place = 0;
  int64_t num_better = team_num;
  for (int64_t size = num_teams_; size > 0; size /= 2) {
    if (num_better + 1 == size) {
      place += size / 2;
      num_better /= 2;
    } else {
      num_better = (num_better + 1) / 2;
    }
  }
  return place;
}

int64_t Problem::GetWorstPlace(int64_t team_num) {
  return num_teams_ - 1 - GetBestPlace(num_teams_ - 1 - team_num);
}

int main() {
  std::ios_base::sync_with_stdio(false);
  Problem::Initialize();
  int num_cases = 0;
  std::cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; case_num++) {
    Problem problem(case_num);
    problem.Input();
    problem.Solve();
    problem.Output();
  }
  Problem::Finalize();
}
