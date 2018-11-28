#include <stdio.h>
#include <assert.h>
#include <map>

#define MIN(a,b) (((a) < (b)) ? (a) : (b))

int main (void) {
  int T = 0;
  (void) scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    std::map<int,int> diners;
    int n = 0;
    (void) scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      int tmp = 0;
      (void) scanf("%d", &tmp);
      diners[tmp]++;
    }
    int best = diners.rbegin()->first;
    int max = best;
    for (int l = max; l > 1; l--) {
      int sum = 0;
      for (std::map<int,int>::reverse_iterator it = diners.rbegin(); it->first > l && it != diners.rend(); it++) {
        int m = it->first;
        int num = it->second;
        sum += num * ((m-1)/l);
      }
      best = MIN(best, l + sum);
    }
    printf("Case #%d: %d\n", currentcase, best);
  }
  return 0;
}
