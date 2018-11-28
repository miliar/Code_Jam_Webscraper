#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
using namespace std;
char a[101];
int main() {
  #ifdef Vlad_kv
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif
  int q, w, e, r, t, test, o;
  cin >> o;
  for (test = 0; test < o; test++) {
    printf("Case #%d: ", test + 1);
    scanf("%s", a);
    t = 1;
    for (w = 1; a[w]; w++) {
      if (a[w] != a[w -1]) {
        t++;
      }
    }
    if (a[w - 1] == '+') {
      t--;
    }
    printf("%d\n", t);
  }
  
  
  
  return 0;
}