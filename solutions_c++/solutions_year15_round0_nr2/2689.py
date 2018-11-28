#include <cstdio>
#include <algorithm>

int pans[1002];

void tcase(int t) {
  int n; scanf("%d", &n);
  for (int i = 0; i < n; i++)
    scanf("%d", &pans[i]);

  int maxpan = *std::max_element(pans, pans + n);
  int best = maxpan;
  for (int b = 1; b < maxpan; b++) {
    int newplates = 0;
    for (int i = 0; i < n; i++)
      newplates += (pans[i] - 1) / b;
    best = std::min(newplates + b, best);
  }

  printf("Case #%d: %d\n", t, best);
}

int main() {
  int t; scanf("%d", &t);
  for (int i = 1; i <= t; i++)
    tcase(i);
}
