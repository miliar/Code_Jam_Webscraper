#include <cstdio>

int T, tt;
char S[2000];

int solve() {
  int m;
  scanf("%d %s", &m, S);

  int res = 0;
  int acc = 0;
  for(int i = 0; i <= m; ++i) {
    int num = S[i]-'0';
    if(acc < i) {
      res += (i-acc);
      acc = i;
    }
    acc += num;
  }
  return res;
}


int main() {

  scanf("%d", &T);
  for(tt = 1; tt <= T; ++tt) {
    int res = solve();
    printf("Case #%d: %d\n", tt, res);
  }
  return 0;
}
