#include <bits/stdc++.h>
using namespace std;

constexpr size_t kMax = 200;

int main() {
  int z;
  scanf("%d\n", &z);
  for (int zz = 1; zz <= z; ++zz) {
    vector<bool> state;
    {
      array<char, kMax+1> line;
      scanf("%s\n", line.data());
      for (int i = 0; line[i] == '+' || line[i] == '-'; ++i)
        state.push_back(line[i] == '+');
    }

    int l = state.size() - 1;
    int moves = 0;
    for (;;) {
      while (l >= 0 && state[l]) --l;
      if (l < 0) break;

      if (state[0]) {
        ++moves;
        for (size_t i = 0; state[i]; ++i) state[i] = false;
      }
      ++moves;
      reverse(begin(state), begin(state) + l + 1);
      for (size_t i = 0; i <= l; ++i) state[i] = !state[i];
    }

    printf("Case #%d: %d\n", zz, moves);
  }

  return 0;
}
