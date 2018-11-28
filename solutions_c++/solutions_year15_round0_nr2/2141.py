#include <stdio.h>
#include <vector>

#define PMAX 1001

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  for (int ncase = 0; ncase < T; ncase++) {
    int D;
    scanf("%d", &D);
    vector<int> v;
    for (int i = 0; i < D; i++) {
      int p;
      scanf("%d", &p);
      v.push_back(p);
    }
    int best = PMAX;
    for (int p = 1; p < PMAX; p++) {
      int cost = 0;
      for (int i = 0; i < D; i++)
        cost += (v[i] - 1) / p;
      best = min(best, cost + p);
    }
    printf("Case #%d: %d\n", ncase + 1, best);
  }
  return 0;
}
