#include <bits/stdc++.h>

using namespace std;

bool vis[10];

int sum() {
  int ret = 0;
  for (int i = 0; i < 10; i++)
    if (vis[i])
      ret++;
  return ret;
}

int main() {
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    printf("Case #%d: ", tc);
    long long n;
    cin >> n;
    if (n == 0) {
      printf("INSOMNIA\n");
      continue;
    }
    memset(vis, 0, sizeof(vis));
    long long cur = 0, pos = 1;
    while (sum() < 10) {
      cur = n * pos;
      while (cur > 0) {
        vis[cur % 10] = 1;
        cur /= 10;
      }
      cur = n * pos++;
    }
    cout << cur << endl;
  }
  return 0;
}