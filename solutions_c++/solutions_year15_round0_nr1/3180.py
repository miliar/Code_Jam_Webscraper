#include <iostream>
#include <vector>


int solve(const std::vector<char> level)
{
  int fri = 0;
  int all = 0;
  for (int s = 0; s < static_cast<int>(level.size()); ++s) {
    if (s > all) {
      fri += s - all;
      all = s;
    }
    all += + level[s];
  }
  return fri;
}

int main()
{
  int nprobs;
  std::cin >> nprobs;
  for (int i = 1; i <= nprobs; ++i) {
    int s;
    std::vector<char> level;
    std::cin >> s;
    while (s >= 0) {
      --s;
      std::cin >> std::ws;
      level.push_back(std::cin.get()-'0');
    }
    std::cout << "Case #" << i << ": " << solve(level) << '\n';
  }
  return 0;
}
