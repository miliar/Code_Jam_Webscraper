#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  int T, D, P, mp, time, sp_time;
  std::vector<int> vi(1001);

  std::cin >> T;

  for (int n_case = 1; n_case <= T; n_case++) {
    std::cin >> D;
    mp = 0;
    std::fill (vi.begin(), vi.end(), 0);
    for (int i = 0; i < D; i++) {
      std::cin >> P;
      vi[P]++;
      if (P > mp) mp = P;
    }

    time = mp;
    for (int final_value = 2; final_value < mp - 1; final_value++) {
      sp_time = 0;
      int i;
      for (i = mp; i > final_value+1; i--) {
        if (vi[i] == 0) continue;
        sp_time += vi[i] * ((i-1)/final_value);
        if (sp_time+final_value > time) break;
      }
      if (vi[i] == 0) i--;
      if (time > sp_time+i) time = sp_time+i;
    }
    std::cout << "Case #" << n_case << ": " << time << '\n';
  }

  return 0;
}
