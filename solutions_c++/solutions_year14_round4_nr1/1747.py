#include <cstdio>
#include <algorithm>
using namespace std;

int n, X;
int sp[12000];
int ans;

void input() {
  scanf("%d%d", &n, &X);
  for (int i = 0; i < n; ++ i){
    scanf("%d", sp + i);
  }
}

void solve(){
  sort(sp, sp + n);
  int l = 0, r = n - 1;
  ans = 0;
  while (l < r) {
    if (sp[r] + sp[l] <= X) {
      ++ ans;
      ++ l, -- r;
    } else {
      ++ ans;
      -- r;
    }
  }
  if (l == r) ++ ans;
}


int main() {
  int T;
  scanf("%d", &T);
  for (int ca = 1; ca <= T; ++ ca) {
    input();
    solve();
    printf("Case #%d: %d\n", ca, ans);
  }
  return 0;
}