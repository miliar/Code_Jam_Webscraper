
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iomanip>

double greedy(int y, int n, const std::vector<double>& p, size_t left, size_t right) {
  if (y == 0) {
    if (n == 0) {
      return 1.0;
    }
    return (1.0 - p[left]) * greedy(0, n-1, p, left+1, right);
  }
  if (n == 0) {
    return p[right] * greedy(y-1, 0, p, left, right-1);
  }
  if (1.0 - p[left] > p[right]) {
    if (p[left] > 0.0) {
      return (1.0 - p[left]) * greedy(y, n-1, p, left+1, right) + (p[left]) * greedy(y-1, n, p, left+1, right);
    }
    return greedy(y, n-1, p, left+1, right);
  }
  if (p[right] < 1.0) {
    return (1.0 - p[right]) * greedy(y, n-1, p, left, right-1) + (p[right]) * greedy(y-1, n, p, left, right-1);
  }
  return greedy(y-1, n, p, left, right-1);
}

double compute(int y, int n, const std::vector<double>& p, size_t i)
{
  if (i == p.size()) {
    return 1.0;
  }
  if (y == 0) {
    if (n == 0) {
      return 1.0;
    }
    return (1.0 - p[i]) * compute(0, n-1, p, i+1);
  }
  if (n == 0) {
    return (p[i]) * compute(y-1, 0, p, i+1);
  }
  if (p[i] == 0.0) {
    return compute(y, n-1, p, i+1);
  }
  if (p[i] == 1.0) {
    return compute(y-1, n, p, i+1);
  }
  return (1.0 - p[i]) * compute(y, n-1, p, i+1) + p[i] * compute(y-1, n, p, i+1);
}

std::string solve(const std::string& problem, const std::string& problem2) {
  int n;
  int k;
  std::istringstream iss(problem);
  iss >> n;
  iss >> k;
  std::vector<double> p;
  std::istringstream iss2(problem2);
  for (int i = 0; i < n; ++i) {
    double tmp;
    iss2 >> tmp;
    p.push_back(tmp);
  }
  std::sort(p.begin(), p.end());
  double max = 0.0;
  for (size_t left_count = 0;left_count <= k; ++left_count) {
    std::vector<double> tmp;
    for (size_t left = 0; left < left_count; ++left) {
      tmp.push_back(p[left]);
    }
    std::vector<double>::reverse_iterator riter = p.rbegin();
    while (tmp.size() < k) {
      tmp.push_back(*(riter++));
    }
    double res = compute(k/2, k/2, tmp, 0);
    if (max < res) {
      max = res;
    }
  }
  std::ostringstream oss;
  oss << max;
  return oss.str();
}

int main()
{
  int lineNumber = 0;
  std::string l;
  int problemCount;
  std::getline(std::cin, l);
  {
    std::istringstream ss(l);
    ss >> problemCount;
  }
  while (std::getline(std::cin, l)) {
    std::string r;
    std::getline(std::cin, r);
    std::cout << "Case #" << ++lineNumber << ": " << solve(l,r) << std::endl;
  }
  return 0;
}
