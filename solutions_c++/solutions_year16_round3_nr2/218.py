#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
using namespace std;
int a[50][50];
long long h[50];
int main() {
  #ifdef Vlad_kv
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #else
    //freopen("bicone.in", "r", stdin);
    //freopen("bicone.out", "w", stdout);
  #endif // Vlad_kv
  int q, w, e, r, t, test, o, c, v;
  h[0] = h[1] = 1;
  for (w = 2; w < 50; w++) {
    h[w] = h[w - 1] * 2;
  }
  cin >> o;
  long long sum;
  for (test = 0; test < o; test++) {
    cout << "Case #" << test + 1 << ": ";
    cin >> q >> sum;
    for (e = 0; e < q; e++) {
      for (r = 0; r < q; r++) {
        a[e][r] = 0;
      }
    }
    for (e = 0; e < q - 1; e++) {
      for (r = e + 1; r < q - 1; r++) {
        a[e][r] = 1;
      }
    }
    for (e = q - 2; e >= 0; e--) {
      if (sum >= h[e]) {
        sum -= h[e];
        a[e][q - 1] = 1;
      }
    }
    if (sum > 0) {
      cout << "IMPOSSIBLE\n";
      continue;
    }
    cout << "POSSIBLE\n";
    for (e = 0; e < q; e++) {
      for (r = 0; r < q; r++) {
        cout << a[e][r];
      }
      cout << "\n";
    }
  }
  
  
  return 0;
}