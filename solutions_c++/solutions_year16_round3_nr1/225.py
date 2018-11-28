#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
using namespace std;
int a[26];
int main() {
  #ifdef Vlad_kv
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #else
    //freopen("bicone.in", "r", stdin);
    //freopen("bicone.out", "w", stdout);
  #endif // Vlad_kv
  int q, w, e, r, t, test, o, sum, c, v;
  scanf("%d", &o);
  for (test = 0; test < o; test++) {
    cout << "Case #" << test + 1 << ": ";
    cin >> q;
    sum = 0;
    for (w = 0; w < q; w++) {
      cin >> a[w];
      sum += a[w];
    }
    while (sum > 3) {
      r = 0;
      for (e = 0; e < q; e++) {
        if (a[e] > a[r]) {
          r = e;
        }
      }
      c = r;
      a[r]--;
      r = 0;
      for (e = 0; e < q; e++) {
        if (a[e] > a[r]) {
          r = e;
        }
      }
      v = r;
      a[r]--;
      cout << ((char)(65 + c)) << ((char)(65 + v)) << " ";
      sum -= 2;
    }
    if (sum == 3) {
      r = 0;
      for (e = 0; e < q; e++) {
        if (a[e] > a[r]) {
          r = e;
        }
      }
      cout << ((char)(65 + r)) << " ";
      a[r]--;
    }
    
    
    
    r = 0;
    for (e = 0; e < q; e++) {
      if (a[e] > a[r]) {
        r = e;
      }
    }
    c = r;
    a[r]--;
    r = 0;
    for (e = 0; e < q; e++) {
      if (a[e] > a[r]) {
        r = e;
      }
    }
    v = r;
    a[r]--;
    cout << ((char)(65 + c)) << ((char)(65 + v)) << " ";
    sum -= 2;
    cout << "\n";
  }
  
  
  
  return 0;
}