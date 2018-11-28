#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
using namespace std;
char a[2001];
char h[][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int main(){
  #ifdef Vlad_kv
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
  #endif // Vlad_kv
  int q, w, e, r, t, test, o;
  scanf("%d", &o);
  int s[256], d[10];
  for (test = 0; test < o; test++) {
    scanf("%s", a);
    for (w = 0; w < 256; w++) {
      s[w] = 0;
    }
    for (w = 0; w < 10; w++) {
      d[w] = 0;
    }
    for (w = 0; a[w]; w++) {
      s[a[w]]++;
    }
    while (1) {
      t = -1; 
      if (s['Z']) {
        t = 0;
        goto st;
      }
      if (s['W']) {
        t = 2;
        goto st;
      }
      if (s['G']) {
        t = 8;
        goto st;
      }
      if (s['X']) {
        t = 6;
        goto st;
      }
      if (s['H']) {
        t = 3;
        goto st;
      }
      if (s['R']) {
        t = 4;
        goto st;
      }
      if (s['O']) {
        t = 1;
        goto st;
      }
      if (s['F']) {
        t = 5;
        goto st;
      }
      if (s['S']) {
        t = 7;
        goto st;
      }
      if (s['N']) {
        t = 9;
        goto st;
      }
      break;
      st:
      d[t]++;
      for (w = 0; h[t][w]; w++) {
        s[h[t][w]]--;
      }
    }
    printf("Case #%d: ", test + 1); 
    for (w = 0; w < 10; w++) {
      for (e = 0; e < d[w]; e++) {
        printf("%d", w);
      }
    }
    printf("\n");
  }
  return 0;
}