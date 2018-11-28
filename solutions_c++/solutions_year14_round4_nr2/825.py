#include <bits/stdc++.h>

using namespace std;

int n;
int a[1001], work[1001];

int main() {
  freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);
  int t; scanf("%d", &t);
  for(int tst = 1; tst <= t; ++tst) {
    scanf("%d", &n);
    for(int i = 0; i < n; ++i)
      scanf("%d", a + i);
    memcpy(work, a, sizeof a);
    sort(a, a + n);
    int ans = 0;
    int left = 0, right = n - 1;
    for(int i = 0; i < n; ++i) {
      int pos = find(work, work + n, a[i]) - work;
      int distToLeft = abs(pos - left);
      int distToRight = abs(pos - right);
      if(distToLeft < distToRight) {
        ans += distToLeft;
        while(distToLeft--) {
          swap(work[pos], work[pos - 1]);
          --pos;
        }
        left++;
      }else {
        ans += distToRight;
        while(distToRight--) {
          swap(work[pos], work[pos + 1]);
          ++pos;
        }
        --right;
      }
    }
    printf("Case #%d: %d\n", tst, ans);
  }
  return 0;
}
