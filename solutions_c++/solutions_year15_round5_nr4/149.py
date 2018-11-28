#include <bits/stdc++.h>
using namespace std;
map<int, int> counts;
int a[10005], b[10005], c[20];
int main() {
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    int p;
    scanf("%d", &p);
    counts.clear();
    for (int i = 0; i < p; i++) {
      scanf("%d", &a[i]);
    }
    int sum = 0;
    for (int i = 0; i < p; i++) {
      scanf("%d", &b[i]);
      counts[a[i]] = b[i];
      sum += b[i];
    }
    int n = 0;
    for (int i = 1; i <= 20; i++) {
      if (sum == (1 << i)) {
        n = i;
      }
    }
    counts[0]--;
    for (int i = 0; i < n; i++) {
      while (counts.begin()->second == 0) {
        counts.erase(counts.begin());
      }
      c[i] = counts.begin()->first;
      counts.begin()->second--;
      int m = 1 << i;
      for (int j = 1; j < m; j++) {
        int sum2 = 0;
        for (int k = 0; k < i; k++) {
          if (j & (1 << k)) {
            sum2 += c[k];
          }
        }
        counts[sum2 + c[i]]--;
      }
    }
    printf("Case #%d:", tt);
    for (int i = 0; i < n; i++) {
      printf(" %d", c[i]);
    }
    printf("\n");
  }
  return 0;
}


