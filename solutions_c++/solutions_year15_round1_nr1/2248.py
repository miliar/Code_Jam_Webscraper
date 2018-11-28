#include <string>
#include <vector>
#include <iostream>
#include <cassert>
#include <algorithm>

typedef std::vector<int> interval_container_t;
typedef std::vector<int> testcase_t;
typedef std::vector<testcase_t> testcase_container_t;

int min_mushroom_interval(const interval_container_t& input) {
  int minimum = 0;
  for (int i = 0; i < input.size() - 1; ++i) {
    minimum += std::max(input[i] - input[i + 1], 0);
  }
  return minimum;
}

int min_mushroom_continuous(const interval_container_t& input) {
  int minimum = 0;
  int max_delta = 0;
  for (int i = 0; i < input.size() - 1; ++i) {
    int delta = input[i] - input[i + 1];
    if (delta > max_delta) {
      max_delta = delta;
    }
  }
  for (int i = 0; i < input.size() - 1; ++i) {
    minimum += std::min(input[i], max_delta);
  }
  return minimum;
}

testcase_container_t collect_testcases() {
  int num_testcases;
  int num_time_intervals;
  testcase_container_t testcases;
  std::cin >> num_testcases;
  for (int i = 0; i < num_testcases; ++i) {
    testcase_t testcase;
    int interval;
    std::cin >> num_time_intervals;
    for (int i = 0; i < num_time_intervals; ++i) {
      std::cin >> interval;
      testcase.push_back(interval);
    }
    testcases.push_back(testcase);
  }
  return testcases;
}

void run_testcases(const testcase_container_t& testcases) {
  for (int i = 0; i < testcases.size(); ++i) {
    std::cout << "Case #" << i + 1 << ": "
            << min_mushroom_interval(testcases[i]) << ' '
            << min_mushroom_continuous(testcases[i])
            << std::endl;
  }
}

int main() {
  testcase_container_t testcases = collect_testcases();
  run_testcases(testcases);
}
