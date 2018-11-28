#include <queue>
#include <cstdio>
using namespace std;

int main() {
  int T, D, P;
  scanf(" %d", &T); 
  for (int t=1; t<=T; t++) {
    fprintf(stderr, "Case #%d\n", t);
    scanf(" %d", &D);
    vector<int> v(D);
    for (int d=0; d<D; d++) {
      scanf(" %d", &v[d]);
    }
    sort(v.rbegin(), v.rend());

    int best = v[0];
    for (int m=v[0]; m>=1; m--) {
      int special = 0;
      for (int d=0; d<D; d++) {
        if (v[d] < m || special+m >= best) break;
        special += (v[d]-1)/m;
      }
      best = min(best, m+special);
    }
    printf("Case #%d: %d\n", t, best);
  }
}
