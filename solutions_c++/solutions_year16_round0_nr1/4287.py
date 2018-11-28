#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long LL;

int T;
LL n, ans;

void work()
{
  bool isCounted[10];
  memset(isCounted, 0, sizeof(isCounted));
  int counts = 0;
  LL x = n;
  while (true) {
    LL tx = x;
    while (tx != 0) {
      LL t = tx % 10;
      if (!isCounted[t]) {
        isCounted[t] = true;
        counts++;
      }
      tx /= 10;
    }
    if (counts == 10) {
      ans = x;
      break;
    }
    x += n;
  }
}

int main()
{
  freopen("A-large.in.txt", "r", stdin);
  freopen("data.out", "w", stdout);
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    int x;
    scanf("%d", &x);
    n = x;
    printf("Case #%d: ", i + 1);
    if (n == 0)
      printf("INSOMNIA\n");
    else {
      work();
      cout << ans << endl;
    }
  }
}
