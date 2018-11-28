#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
using namespace std;
int ans, ans1[1000], ans2[1000], ans3[1000];
int q1, q2, q3, t;
int a[10][10][10];
int s1[10][10], s2[10][10], s3[10][10];
void l(int w, int e, int r) {
  //cout << w << " " << e << " " << r << "\n";
  if (r == q3) {
    //cout << "%%%%%%%\n";
    int subAns = 0;
    for (w = 0; w < q1; w++) {
      for (e = 0; e < q2; e++) {
        for (r = 0; r < q3; r++) {
          subAns += a[w][e][r];
        }
      }
    }
    if (ans < subAns) {
      ans = subAns;
      int t = 0;
      for (w = 0; w < q1; w++) {
        for (e = 0; e < q2; e++) {
          for (r = 0; r < q3; r++) {
            if (a[w][e][r]) {
              ans1[t] = w;
              ans2[t] = e;
              ans3[t] = r;
              t++;
            }
          }
        }
      }
    }
    return;
  }
  
  int c = w + 1, v = e, b = r;
  if (c == q1) {
    c = 0;
    v++;
    if (v == q2) {
      v = 0;
      b++;
    }
  }
  //cout << c << " " << v << " " << b << "  * " << q1 << " " << q2 << " " << q3 << "\n";
  if ((s1[w][e] > 0) && ((s2[w][r] > 0) && (s3[e][r] > 0))) {
    s1[w][e]--;
    s2[w][r]--;
    s3[e][r]--;
    a[w][e][r] = 1;
    l(c, v, b);
    s1[w][e]++;
    s2[w][r]++;
    s3[e][r]++;
  }
  a[w][e][r] = 0;
  l(c, v, b);
}
void sch() {
  int w, e, r;
  ans = 0;
  for (w = 0; w < q1; w++) {
    for (e = 0; e < q2; e++) {
      for (r = 0; r < q3; r++) {
        a[w][e][r] = 0;
      }
    }
  }
  for (e = 0; e < 10; e++) {
    for (r = 0; r < 10; r++) {
      s1[e][r] = s2[e][r] = s3[e][r] = t;
    }
  }
  l(0, 0, 0);
  
  
}
int main() {
  #ifdef Vlad_kv
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #else
    //freopen("bicone.in", "r", stdin);
    //freopen("bicone.out", "w", stdout);
  #endif // Vlad_kv
  int q, w, e, r, test, o, c, v;
  cin >> o;
  for (test = 0; test < o; test++) {
    cout << "Case #" << test + 1 << ": ";
    cin >> q1 >> q2 >> q3 >> t;
    sch();
    cout << ans << "\n";
    for (w = 0; w < ans; w++) {
      cout << ans1[w] + 1 << " " << ans2[w]  + 1 
           << " " << ans3[w] + 1 << "\n";
    }
  }
  return 0;
}