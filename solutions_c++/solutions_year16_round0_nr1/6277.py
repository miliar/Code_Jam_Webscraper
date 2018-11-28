/*zhen hao*/
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

const int maxn = 20;
int cnt;
bool vis[maxn];

void divide(int n) {
  while (n) {
    if (!vis[n % 10]) cnt++;
    vis[n % 10] = true;
    n /= 10;
  }
}

int slove(int n) {
  memset(vis, false, sizeof vis);
  cnt = 0;
  int x = n;
  for (;;) {
    divide(x);
    if (cnt >= 10) break;
    x += n;
  }
  return x;
}

int main() {
//  freopen("A-large.in", "r", stdin);
//  freopen("case.in", "w", stdout);
  int T, tcase = 0;
  cin >> T;
  while (T--) {
    int n;
    scanf("%d", &n);
    printf("Case #%d: ", ++tcase);
    if (n == 0) puts("INSOMNIA");
    else printf("%d\n", slove(n));
  }
  return 0;
}
