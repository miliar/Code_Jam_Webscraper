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
  struct Pair {
    int origin;
    int endpoint;
    int num_passengers;
  };

  int64_t ComputeGain(int64_t origin, int64_t endpoint, int64_t num_passengers);

  int case_num_;

  int num_stops_;
  int num_pairs_;
  std::vector<Pair> pairs_;

  int max_loss_;
};

void Problem::Input() {
  std::cin >> num_stops_;
  std::cin >> num_pairs_;
  pairs_.resize(num_pairs_);
  for (int i = 0; i < num_pairs_; i++) {
    std::cin >> pairs_[i].origin >> pairs_[i].endpoint >> pairs_[i].num_passengers;
  }
}

void Problem::Solve() {
  struct Event {
    int stop_num;
    int delta;
    Event(int stop_num, int delta) : stop_num(stop_num), delta(delta) {}
  };
  struct State {
    int stop_num;
    int num_passengers;
    State(int stop_num, int num_passengers) : stop_num(stop_num), num_passengers(num_passengers) {}
  };

  std::vector<Event> events;
  int64_t normal_gain = 0;
  for (const Pair& pair : pairs_) {
    events.emplace_back(pair.origin, pair.num_passengers);
    events.emplace_back(pair.endpoint, -pair.num_passengers);
    normal_gain += ComputeGain(pair.origin, pair.endpoint, pair.num_passengers);
  }
  std::sort(events.begin(), events.end(), [](const Event& lhs, const Event& rhs) {
    return lhs.stop_num < rhs.stop_num || (lhs.stop_num == rhs.stop_num && lhs.delta > rhs.delta);
  });

  std::deque<State> states;
  int64_t min_gain = 0;
  for (const Event& event : events) {
    if (event.delta > 0) {
      states.emplace_back(event.stop_num, event.delta);
    } else {
      int remaining = -event.delta;
      while (remaining > 0) {
        int take_away = std::min(remaining, states.back().num_passengers);
        min_gain += ComputeGain(states.back().stop_num, event.stop_num, take_away);
        remaining -= take_away;
        states.back().num_passengers -= take_away;
        if (states.back().num_passengers == 0) {
          states.pop_back();
        }
      }
    }
  }

  max_loss_ = static_cast<int>((normal_gain - min_gain) % 1000002013);
  if (max_loss_ < 0) {
    max_loss_ += 1000002013;
  }
}

void Problem::Output() const {
  std::cout << "Case #" << case_num_ << ": " << max_loss_ << std::endl;
}

void Problem::Initialize() {
}

void Problem::Finalize() {
}

int64_t Problem::ComputeGain(int64_t origin, int64_t endpoint, int64_t num_passengers) {
  int64_t delta = endpoint - origin;
  int64_t sum = (2 * num_stops_ - delta) * (delta + 1) / 2;
  return (sum % 1000002013) * num_passengers % 1000002013;
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
