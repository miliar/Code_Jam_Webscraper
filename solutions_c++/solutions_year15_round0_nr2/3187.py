#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
using namespace std;

#define rep(i, s, t) for (int i = (s); i < (t); i ++)
#define repd(i, s, t) for (int i = (s); i > (t); i --)
#define ll long long

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t, d, p[1005];
  cin >> t;
  for (static int cas = 1; cas <= t; cas ++) {
    cin >> d;
    int tmp_max = 0;
    rep(i, 0, d) {
      cin >> p[i];
      tmp_max = max(tmp_max, p[i]);
    }
    int ans = 0x7fffffff;
    for (int partition = 1; partition <= tmp_max; partition ++) {
        int cnt = 0;
      rep(i, 0, d) {
        if (p[i] <= partition) continue;
        else {
          int num = p[i] / partition + (p[i] % partition ? 1 : 0);
          cnt += num - 1;
        }
      }
        ans = min(ans, partition + cnt);
    }
    cout << "Case #" << cas << ": " << ans << endl;
  }
}
