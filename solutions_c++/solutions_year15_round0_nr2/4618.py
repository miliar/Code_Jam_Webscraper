#include <iostream>
#include <vector>
#include <algorithm>

bool desc (int i, int j) { return (i>j); }

void min_time(std::vector<int> peps, int &best, int elapsed, int takeout) {
  peps[0] -= takeout;
  peps.push_back(takeout);
  std::sort(peps.begin(), peps.end(), desc);
  best = std::min(best, peps[0] + elapsed);
  ++elapsed;
  if (elapsed >= best) return;
  for (int i = 1; i <= peps[0] / 2; ++i) min_time(peps, best, elapsed, i);
}

int pancakes() {
  int D;
  std::cin >> D;
  std::vector<int> peps(D);
  for (int i = 0; i < D; ++i) std::cin >> peps[i];
  std::sort(peps.begin(), peps.end(), desc);
  int best = peps[0];
  min_time(peps, best, 0, 0);
  return best;
}

int main() {
  int t = 1, T;
  std::cin >> T;

  while (t <= T) {
    std::cout << "Case #" << t << ": " << pancakes() << '\n';
    ++t;
  }
}
