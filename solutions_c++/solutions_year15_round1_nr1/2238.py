#include <iostream>

#include <cstdio>

using namespace std;

int m[100000];

void main2() {
  int n; cin >> n;
  for (int i = 0; i < n; ++i) cin >> m[i];
  int a1 = 0;
  int a2 = 0;
  int maxRate = 0;
  for (int i = 1; i < n; ++i) {
    if (m[i] < m[i - 1]) {
      a1 += m[i - 1] - m[i];
      maxRate = max(maxRate, m[i - 1] - m[i]);
    }
  }
  //cout << maxRate << '\n';

  int cur = m[0];
  for (int i = 1; i < n; i++) {
    int z = min(maxRate, cur);
    cur -= z;
    a2 += z;
    //cout << z << ' ' << a2 << '\n';
    cur = m[i];
  }
  cout << a1 << ' ' << a2;
}

int main() {
  //freopen("A-small-0.in", "r", stdin);
  //freopen("A-small-0.out", "w", stdout);

  ios::sync_with_stdio(0);
  cin.tie(0);

  int T; cin >> T;
  for (int i = 1; i <= T; ++i) {
    cout << "Case #" << i << ": ";
    main2();
    cout << '\n';
  }

}
