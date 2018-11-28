// Author: Chi-Kit (George) LAM
#include <cstdio>
#include <cinttypes>
#include <cstring>
#include <algorithm>
using namespace std;
int T;
void solve(int T) {
  int64_t N, ans = 0, count=0;
  bool b[10];
  memset(b,0,sizeof(b));
  scanf("%" SCNd64 "\n", &N);
  if (N > 0) {
    for (int i=0; i<10; ++i) {
      b[i] = false;
    }
    while (count != 10) {
      ans += N;
      int x = ans;
      while (x>0) {
        if (!b[x%10]) {
          b[x%10] = true;
          ++count;
        }
        x /= 10;
      }
    }
    printf("Case #%d: %" PRId64 "\n", T, ans);
  } else {
    printf("Case #%d: INSOMNIA\n", T);
  }
  return;
}
int main(){
  scanf("%d\n", &T);
  for (int i=1; i<=T; ++i) {
    solve(i);
  }
  return 0;
}
