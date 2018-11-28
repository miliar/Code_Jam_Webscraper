#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
using namespace std;
int main(){
  #ifdef Vlad_kv
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
  #endif
  int q, w, e, r, t, o, test, a[10];
  scanf("%d", &o);
  for (test = 0; test < o; test++) {
    printf("Case #%d: ", test + 1);
    scanf("%d", &q);
    if (q == 0) {
      printf("INSOMNIA\n");
      continue;
    }
    for (w = 0; w < 10; w++) {
      a[w] = 1;
    }
    t = 0;
    for (w = 0; ; w += q) {
      for (e = w; e; e /= 10) {
        t += a[e % 10];
        a[e % 10] = 0;
      }
      if (t == 10) {
        break;
      }
    }
    printf("%d\n", w);
  }
  return 0;
}