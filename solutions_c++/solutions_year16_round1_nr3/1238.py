#include <algorithm>
#include <iostream>
#include <vector>

#include <omp.h>

int main() {
  size_t T;
  std::cin >> T;
#pragma omp parallel for
  for (int t = 1; t <= T; ++t) {
    size_t N;
    std::cin >> N;

    std::vector<size_t> BFF(N);
    std::vector<size_t> arrangments(N);

    for (size_t i = 0; i < N; ++i) {
      std::cin >> BFF[i];
      --BFF[i];
      arrangments[i] = i;
    }

    size_t best_bff_count = 0;

    do {
      std::vector<size_t> copied_arrangments = arrangments;
      while (true && copied_arrangments.size() > best_bff_count) {
        bool removed = false;
        for (size_t i = 0; i < copied_arrangments.size(); ++i) {
          size_t bff = BFF[copied_arrangments[i]];
          size_t l = copied_arrangments[(i - 1 + copied_arrangments.size()) % copied_arrangments.size()];
          size_t r = copied_arrangments[(i + 1) % copied_arrangments.size()];
          bool has_bff = bff == l || bff == r;
          if (!has_bff) {
            copied_arrangments.erase(copied_arrangments.begin() + i);
            removed = true;
            break;
          }
        }
        if (!removed) {
          break;
        }
      }
      best_bff_count = std::max(copied_arrangments.size(), best_bff_count);
    } while (std::next_permutation(arrangments.begin(), arrangments.end()));

    std::cout << "Case #" << t << ": " << best_bff_count << "\n";
  }
  return 0;
}
