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
  int X, R, C;
  cin >> X >> R >> C;
  cout << "Case #" << test_num << ": ";
  if (R * C % X != 0 || X > max(R, C))
    cout << "RICHARD\n";
  else if (X >= 3 && min(R, C) == 1)
    cout << "RICHARD\n";
  else if (X == 4 && R * C == 8)
    cout << "RICHARD\n";
  else
    cout << "GABRIEL\n";
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
