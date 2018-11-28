#include <stdio.h>


#include <algorithm>
#include <vector>
#include <utility>


using std::min;
using std::vector;
using std::pair;


bool DFS(int n, int i, int bits, int used_peo, int used_pos) {
  if (n == i) {
    return true;
  }
  for (int peo = 0; peo < n; ++peo) {
    if ((used_peo >> peo) & 1) {
      continue;
    }
    bool deep = false;
    for (int pos = 0; pos < n; ++pos) {
      if ((bits >> peo * n + pos) & 1) {
        if ((used_pos >> pos) & 1) {
          continue;
        }
        deep = true;
        if (!DFS(n, i + 1, bits,
                 used_peo | (1 << peo), used_pos | (1 << pos))) {
          return false;
        }
      }
    }
    if (!deep) {
      return false;
    }
  }
  return true;
}


bool Check(int n, int bits) {
  return DFS(n, 0, bits, 0, 0);
}


int main(void) {
  vector<int> all[5];
  for (int n = 2; n <= 4; ++n) {
    for (int i = 0, i_end = 1 << n * n; i < i_end; ++i) {
      if (Check(n, i)) {
        all[n].push_back(i);
      }
    }
  }

  int num_cases;
  scanf("%d", &num_cases);

  for (int case_idx = 1; case_idx <= num_cases; ++case_idx) {
    int n;
    scanf("%d", &n);

    int bits = 0;
    for (int i = 0; i < n; ++i) {
      char s[100];
      scanf("%s", s);

      for (int j = 0; j < n; ++j) {
        bits |= (s[j] - '0' << i * n + j);
      }
    }

    printf("Case #%d: ", case_idx);

    if (n == 1) {
      printf("%d\n", 1 - bits);
      continue;
    }

    int ans = n * n;
    for (auto k : all[n]) {
      if ((k & bits) != bits) continue;

      int cost = 0;
      for (int x = k - bits; x != 0; x >>= 1) cost += (x & 1);

      ans = min(ans, cost);
    }

    printf("%d\n", ans);
  }

  return 0;
}
