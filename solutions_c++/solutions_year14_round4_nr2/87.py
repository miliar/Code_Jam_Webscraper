#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1010;

int T, N;
int ar[MAXN];

int main() {
  scanf("%d", &T);

  for(int t = 1; t <= T; ++t) {
    scanf("%d", &N);
    for(int i = 0; i < N; ++i) {
      scanf("%d", ar + i);
    }

    int lft = 0, rgt = N;
    int ans = 0;
    while (lft < rgt) {
      int mn = lft;
      for(int i = lft; i < rgt; ++i) {
        if (ar[i] < ar[mn]) {
          mn = i;
        }
      }
      int d1 = mn - lft;
      int d2 = rgt - 1 - mn;
      if (d1 < d2) {
        while (mn > lft) {
          swap(ar[mn], ar[mn - 1]);
          --mn;
          ++ans;
        }
        ++lft;
      } else {
        while (mn + 1 < rgt) {
          swap(ar[mn], ar[mn + 1]);
          ++mn;
          ++ans;
        }
        --rgt;
      }
    }

    printf("Case #%d: %d\n", t, ans);
  }
}
