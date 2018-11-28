#include <iostream>
#include <vector>
#include <algorithm>

void solve() {
  int T, N;
  int rst1, rst2, ptr1, ptr2;
  float weight;
  std::cin >> T;
  for (int i = 0; i < T; ++i) {
    std::cin >> N;
    std::vector<float> naomi, ken;
    for (int n = 0; n < N; ++n) {
      std::cin >> weight;
      naomi.push_back(weight);
    }
    std::sort(naomi.begin(), naomi.end());

    for (int n = 0; n < N; ++n) {
      std::cin >> weight;
      ken.push_back(weight);
    }
    std::sort(ken.begin(), ken.end());

    rst1 = 0;
    ptr1 = 0;
    ptr2 = 0;
    for (int n = 0; n < N; ++n) {
      //std::cout << naomi[n] << ", " << ken[n] << std::endl;
      if (naomi[ptr1] > ken[ptr2]) {
        ptr1++;
        ptr2++;
        rst1++;
      } else {
        ptr1++;
      }
    }

    rst2 = 0;
    ptr1 = 0;
    ptr2 = 0;
    for (int n = 0; n < N; ++n) {
      if (naomi[ptr1] < ken[ptr2]) {
        ptr1++;
        ptr2++;
      } else {
        ptr2++;
        rst2++;
      }
    }
    std::cout << "Case #" << i + 1 << ": " << rst1 << " " << rst2 << "\n";
  }
}

int main(int argc, char *argv[]) {
  solve();
  return 0;
}
