#include <iostream>

using namespace std;

string op[30];

bool nop[30][30];
bool go(int cur, int N, bool* taken, int* order) {
  if (cur == N) {
    return true;
  }
  bool ret = true;
  bool found = false;
  for (int i = 0; i < N; i++) {
    if (nop[order[cur]][i] && !taken[i]) {
      found = true;
      taken[i] = true;
      ret &= go(cur + 1, N, taken, order);
      taken[i] = false;
    }
  }
  return found && ret;
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N; cin >> N;
    for (int i = 0; i < N; i++) {
      cin >> op[i];
    }

    int best = N*N;
    for (int mask = 0; mask < (1<<(N*N)); mask++) {
      for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
          nop[i][j] = (op[i][j] == '1' || (mask & (1<<(i*N+j))));

      bool ok = true;
      int order[N];
      for (int i = 0; i < N; i++) order[i] = i;
      do {
        bool taken[N];
        memset(taken, 0, N);
        ok &= go(0, N, taken, order);
      } while (ok && next_permutation(order, order+N));

      if (ok) {
        best = min(best, __builtin_popcount(mask));
      }
    }

    printf("Case #%d: %d\n", t, best);
  }
}
