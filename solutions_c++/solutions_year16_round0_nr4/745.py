#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <fstream>
#include <ctime>
using namespace std;
int main() {
  srand(time(0));
  #ifdef Vlad_kv
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif
  int q, w, e, r, t, test, o;
  long long c, v;
  cin >> o;
  for (test = 0; test < o; test++) {
    cout << "Case #" << test + 1 << ": ";
    cin >> q >> w >> t;
    e = q / w;
    if (q % w != 0) {
      e++;
    }
    if (e > t) {
      cout << "IMPOSSIBLE\n";
      continue;
    }
    t = 0;
    for (r = 0; r < e; r++) {
      c = 0;
      for (v = 0; v < w; v++) {
        c = c * q + t;
        t = (t + 1) % q;
      }
      cout << c + 1 << " ";
    }
    cout << "\n";
  }
  return 0;
}