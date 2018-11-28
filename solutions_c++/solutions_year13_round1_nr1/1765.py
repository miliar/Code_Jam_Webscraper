#include <iostream>
#include <math.h>
using namespace std;

#define rep(i,n) for(int i = 0;i<n;i++)

int r, t;

int solve() { // 描ける黒円の最大値を返す
  int ans = 0, t2;
  t2 = 0;
  while(t2 <= t) {
    t2 = 2 * r + 1; // 半径r to (r + 1)の円で必要なpaintの量
    if (t2 <= t) ans++;
    r = r + 2;
    t = t - t2;
  }

  return ans;
}

int main() {
  int test;
  cin >> test;
  rep(i,test) {
    cin >> r >> t;
    int ans = solve();
    printf("Case #%d: %d\n", i+1, ans);
  }

  return 0;
}
