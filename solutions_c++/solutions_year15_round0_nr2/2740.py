#include <iostream>
#include <algorithm>
#include <vector>
#include <limits>
#include <cmath>

// pancake count
typedef int pcount_t;
typedef std::vector<pcount_t> pcount_container_t;

int calc_distribution_cost(const pcount_container_t& counts, int alpha) {
  int special_minutes = 0;
  for (pcount_t count : counts) {
    while (count > alpha) {
      count -= alpha;
      ++ special_minutes;
    }
  }
  return special_minutes + alpha;
}

int calc_optimal_time(const pcount_container_t& counts) {
  int best = std::numeric_limits<int>::max();
  int biggest_plate = *max_element(counts.begin(), counts.end());
  for (int i = 1; i <= biggest_plate; ++i) {
    int trial = calc_distribution_cost(counts, i);
    if (trial < best) {
      best = trial;
    }
  }
  return best;
}

pcount_container_t collect_counts() {
  pcount_container_t counts;
  int num_counts;
  std::cin >> num_counts;
  for (int i = 0; i < num_counts; ++i) {
    pcount_t count;
    std::cin >> count;
    counts.push_back(count);
  }
  return counts;
}

typedef pcount_container_t testcase_t;
typedef std::vector<testcase_t> testcase_container_t;

testcase_container_t collect_testcases() {
  int testcase_count;
  testcase_container_t testcases;
  std::cin >> testcase_count;
  for (int i = 0; i < testcase_count; ++i) {
    testcase_t testcase = collect_counts();
    testcases.push_back(testcase);
  }
  return testcases;
}

void run_testcases(const testcase_container_t& testcases) {
  for (int i = 0; i < testcases.size(); ++i) {
    std::cout << "Case #" << i + 1 << ": "
              << calc_optimal_time(testcases[i])
              << std::endl;
  }
}

int main() {
  testcase_container_t testcases = collect_testcases();
  run_testcases(testcases);
}
