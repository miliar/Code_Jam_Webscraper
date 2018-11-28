/*
 *
 * File: stuff.cpp
 * Author: Andy Y.F. Huang (azneye)
 * Created on Aug 23, 2014, 11:50:25 PM
 */

#include <bits/stdc++.h>

using namespace std;

namespace stuff {
typedef long long ll;

void solve(int test_num) {
  int M;
  string str;
  cin >> M >> str;
  int cnt = 0, res = 0;
  for (int i = 0; i <= M; i++) {
    if (cnt < i) {
      res += i - cnt;
      cnt = i;
    }
    cnt += str[i] - '0';
  }
  cout << "Case #" << test_num << ": " << res << endl;
}

void solve() {
#ifdef AZN
  double start_t = clock();
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
//freopen("azn.txt", "w", stderr);
#endif
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int T = 1;
//scanf("%d", &T);
  cin >> T;
  for (int t = 1; t <= T; t++)
    solve(t);
#ifdef AZN
  cerr << "Took: " << ((clock() - start_t) / CLOCKS_PER_SEC);
#endif
}
}

int main() {
  stuff::solve();
  return 0;
}
