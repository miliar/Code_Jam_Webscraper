#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <iomanip>
using namespace std;

#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>

typedef int cnt[10];

int add(cnt buf, lint x) {
  int ans = 0;
  while (x > 0) {
    if (buf[x%10] == 0) ans++;
    buf[x%10]++;
    x /= 10;
  }
  return ans;
}


int main() {
  ios_base::sync_with_stdio(false);
  cout << setprecision(10) << fixed;
  int t;
  cin >> t;
  for (int ii = 0; ii < t; ii++) {
    cnt buf;
    memset(buf, 0, sizeof buf);
    lint n;
    cin >> n;
    if (n == 0)
      cout << "Case #" << ii+1 << ": INSOMNIA\n";
    else {
      int cur = 0;
      int ans = 0;
      lint cval = 0;
      while (cur < 10) {
        ans++;
        cval += n;
        cur += add(buf, cval);
      }
      cout << "Case #" << ii+1 << ": " << cval << "\n";
    }
  }
}
