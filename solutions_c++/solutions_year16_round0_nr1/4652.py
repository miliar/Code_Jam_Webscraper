#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main() {
  //freopen("A-small-attempt2.in", "r", stdin);
  freopen("A-small-attempt0.out", "w", stdout);
  int T;
  cin >> T;
  int cas = 0;
  while(T--) {
    long long x;
    cin >> x;
    if (x == 0) {
      cout << "Case #" << ++cas << ": INSOMNIA" << endl;
      continue;
    }
    int vis[10];
    memset(vis, 0, sizeof vis);
    int ans = 10;
    long long out = 0;
    for(int i = 1; ; i++) {
      long long c = x * i;
      while(c) {
        //cout << "c = " << c << endl;
        int mod = c % 10;
        if (!vis[mod]) vis[mod] = 1, ans --;
        if (ans == 0) {
          out = x * i;
          break;
        }
        c /= 10;
      }
      if (out != 0) break;
    }
    cout << "Case #" << ++cas << ": " << out << endl;
  }
  return 0;
}