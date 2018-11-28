#include <iostream>

using namespace std;

typedef long long ll;

ll solve(ll N) {
  bool taken[10] = {false};
  int cnt = 0;
  ll acc = N;
  while (1) {
    ll temp = acc;
    while (temp) {
      int x = temp % 10;
      if (!taken[x]) {
        taken[x] = true;
        cnt++;
      }
      temp /= 10;
    }
    if (cnt == 10) {
      return acc;
    }
    acc += N;
  }
  return -1;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int qq = 1; qq <= T; qq++) {
    printf("Case #%d: ", qq);
    ll N;
    scanf("%lld", &N);
    if (!N) {
      printf("INSOMNIA\n");
    } else {
      printf("%lld\n", solve(N));
    }
  }
  return 0;
}
