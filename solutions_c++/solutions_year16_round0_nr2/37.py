// Author: Chi-Kit (George) LAM
#include <cstdio>
#include <cinttypes>
#include <algorithm>
using namespace std;
int T;
void solve(int T) {
  int x = 0, ans = 0;
  int c = getchar();
  while (c == '-' || c == '+') {
    if (x != 0 && x != c) {
      ++ans;
    }
    x = c;
    c = getchar();
  }
  if (x == '-') {
    ++ans;
  }
  printf("Case #%d: %d\n", T, ans);
  return;
}
int main(){
  scanf("%d\n", &T);
  for (int i=1; i<=T; ++i) {
    solve(i);
  }
  return 0;
}
