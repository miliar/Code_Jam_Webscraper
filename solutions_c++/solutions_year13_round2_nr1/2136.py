#include <cstdlib>
#include <iostream>
#include <tr1/memory>
#include <vector>
#include <map>

unsigned int solve (
    unsigned int depth,
    unsigned int index,
    unsigned long long armin,
    const std::vector<unsigned long long> &motes) {

  if (index == motes.size()) {
    return depth;
  }
  if (armin > motes[index]) {
    return solve(depth, index + 1, armin + motes[index], motes);
  } else {
    unsigned long long newArmin = ((armin << 1) - 1);
    if (newArmin == armin) {
      return solve(depth + 1, index + 1, armin, motes);
    } else {
      return std::min(
          solve(depth + 1, index, (armin << 1) - 1, motes),
          solve(depth + 1, index + 1, armin, motes)
      );
    }
  }
}

int main (int argc, char** argv) {

  int T;
  std::cin >> T;

  for (unsigned int t = 0; t < T; ++t) {

    unsigned long long A, N;
    std::cin >> A >> N;
    std::vector<unsigned long long> motes;
    for (unsigned int n = 0; n < N; ++n) {
      unsigned long long mote;
      std::cin >> mote;
      motes.push_back(mote);
    }

    std::sort(motes.begin(), motes.end());

    unsigned int answer = solve(0, 0, A, motes);

    std::cout << "Case #" << t + 1 << ": ";
    std::cout << answer << std::endl;
  }

  return EXIT_SUCCESS;
}

