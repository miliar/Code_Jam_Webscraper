#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <cstring>
using namespace std;
char a[101], s[101];
int q;
long long mainAns;
char ans1[101], ans2[101];
char a2[101], s2[101];
void l(char *a, char *s) {
  char *a2 = new char[q + 1];
  char *s2 = new char[q + 1];
  int w, t;
  for (w = 0; w < q; w++) {
    a2[w] = a[w];
    s2[w] = s[w];
  }
  for (w = 0; w < q; w++) {
    if ((a2[w] == '?') && (s2[w] != '?')) {
      a2[w] = min(48 + 9, s2[w] + 1);
      l(a2, s2);
      a2[w] = max(48 + 0, s2[w] - 1);
      l(a2, s2);
      a2[w] = s2[w];
      continue;
    }
    if ((s2[w] == '?') && (a2[w] != '?')) {
      s2[w] = min(48 + 9, a2[w] + 1);
      l(a2, s2);
      s2[w] = max(48 + 0, a2[w] - 1);
      l(a2, s2);
      s2[w] = a2[w];
      continue;
    }
    if (a2[w] == '?') {
      a2[w] = '1';
      s2[w] = '0';
      l(a2, s2);
      a2[w] = '0';
      s2[w] = '1';
      l(a2, s2);
      a2[w] = s2[w] = '0';
    }
    if (a2[w] != s2[w]) {
      break;
    }
  }
  t = w;
  for (w = t + 1; w < q; w++) {
    if (a2[t] < s2[t]) {
      if (a2[w] == '?') {
        a2[w] = '9';
      }
      if (s2[w] == '?') {
        s2[w] = '0';
      }
    } else {
      if (a2[w] == '?') {
        a2[w] = '0';
      }
      if (s2[w] == '?') {
        s2[w] = '9';
      }
    }
  }
  long long e = 0, r = 0;
  for (w = 0; w < q; w++) {
    e = e * 10 + a2[w] - 48;
    r = r * 10 + s2[w] - 48;
  }
  e = abs(e - r);
  if (mainAns > e) {
    mainAns = e;
    for (w = 0; w < q; w++) {
      ans1[w] = a2[w];
      ans2[w] = s2[w];
    }
  } else {
    if (mainAns == e) {
      bool b = 0;
      for (w = 0; w < q; w++) {
        if (ans1[w] < a2[w]) {
          b = 1;
          return;
        }
        if (ans1[w] > a2[w]) {
          b = 1;
          break;
        }
      }
      if (!b) {
        for (w = 0; w < q; w++) {
          if (ans2[w] < s2[w]) {
            b = 1;
            return;
          }
          if (ans2[w] > s2[w]) {
            b = 1;
            break;
          }
        }
      }
      if (b) {
        for (w = 0; w < q; w++) {
          ans1[w] = a2[w];
          ans2[w] = s2[w];
        }
      }
    }
  }
}
int main(){
  #ifdef Vlad_kv
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
  #endif // Vlad_kv
  int w, e, r, t, o, test;
  scanf("%d", &o);
  for (test = 0; test < o; test++) {
    scanf("%s%s", a, s);
    q = strlen(a);
    mainAns = ((long long)1)<<62;
    l(a, s);
    ans1[q] = ans2[q] = 0;
    printf("Case #%d: %s %s\n", test + 1, ans1, ans2);
  }
  return 0;
}