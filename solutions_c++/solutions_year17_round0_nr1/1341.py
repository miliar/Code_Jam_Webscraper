#include <cstdio>
#include <cstring>
using namespace std;

char buf[1007];

void solve() {
  int K;
  scanf("%s %d", buf, &K);
  int N = strlen(buf);
  int ans = 0;

  for (int i = 0; i < N-K+1; i++) {
    if (buf[i] == '-') {
      // flip
      ans++;
      for (int j = 0; j < K; j++) {
        if (buf[i+j] == '-')
          buf[i+j] = '+';
        else
          buf[i+j] = '-';
      }
    }
  }

  for (int i = N-K; i < N; i++) {
    if (buf[i] != '+') {
      printf("IMPOSSIBLE\n");
      return;
    }
  }

  printf("%d\n", ans);
}

int main() {
    int T;
    scanf("%d ", &T);
    for (int t = 0; t < T; t++) {
      printf("Case #%d: ", t+1);
      solve();
    }
}