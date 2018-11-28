#include <cstdio>
#include <cassert>

const int MAXN = 1005;

int N;
char s[MAXN];
void solve() {
  scanf("%d%s", &N, s);
  int now = 0, ret = 0;
  for(int i = 0; i <= N; i++) {
    assert(s[i] >= '0' && s[i] <= '9');
    int s_i = s[i] - '0';
    if (now < i) {
      ret += i - now;
      now = i;
    }
    now += s_i;
  }
  printf("%d\n", ret);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    solve();
  }
}
