#include <iostream>
#include <vector>
#include <algorithm>

int solve(const std::vector<int> &p)
{
  const int worst = *std::max_element(p.cbegin(), p.cend());
  int best = worst;
  for (int e = 1; e < worst; ++e) {
    int s = 0;
    for (const auto i : p) {
      s += i/e;
      if (i%e == 0) {
        --s;
      }
    }
    best = std::min(best, s+e);
  }
  return best;
}

int main()
{
  int nprobs;
  std::cin >> nprobs;
  for (int i = 1; i <= nprobs; ++i) {
    int d;
    std::vector<int> p;
    std::cin >> d;
    while (d > 0) {
      --d;
      int x;
      std::cin >> x;
      p.push_back(x);
    }
    std::cout << "Case #" << i << ": " << solve(p) << '\n';
  }
  return 0;
}
