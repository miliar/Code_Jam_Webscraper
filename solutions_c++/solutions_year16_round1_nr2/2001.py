#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

void solve_case(int case_num)
{
  std::map<int, int> m;
  int n, x;

  std::cin >> n;
  for (int i = 0; i < 2 * n - 1; i++) {
    for (int j = 0; j < n; j++) {
      std::cin >> x;
      m[x] += 1;
    }
  }

  std::cout << "CASE #" << case_num << ":";

  std::vector<int> v;
  for (auto& kv : m) {
    if (kv.second & 1) {
      v.push_back(kv.first);
    }
  }
  std::sort(v.begin(), v.end());
  for (int& x : v) {
    std::cout << ' ' << x;
  }
  std::cout << std::endl;
}

int main()
{
  int num_cases;

  std::cin >> num_cases;
  for (int i = 1; i <= num_cases; i++) {
    solve_case(i);
  }
  
  return 0;
}
