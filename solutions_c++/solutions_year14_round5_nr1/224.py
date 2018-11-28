#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <cstdarg>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <ctime>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(c) (c).begin(), (c).end()
#define mp make_pair
#define pb push_back
#define sz(c) (int)(c).size()
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

const int maxn = 1 << 20;

int a[maxn];

void solve(int test) {
  int n;
  long long p, q, r, s;
  scanf("%d", &n);
  scanf("%lld%lld%lld%lld", &p, &q, &r, &s);
  for (int i = 0; i < n; i++) a[i] = ((long long)i * p + q) % r + s;
  //for (int i = 0; i < n; i++) {
 //   eprintf("%d%c", a[i], " \n"[i + 1 == n]);
  //}
  long long right = 0;
  long long left = 0;
  long long total = 0;
  for (int i = 0; i < n; i++) right += a[i];
  total = right;
  right += 1;
  while (left + 1 < right) {
    long long ave = (left + right) >> 1;
    int c = 1;
    long long sum = 0;
    for (int i = 0; i < n; i++) {
      if (a[i] > ave) c = 100;
      if (sum + a[i] <= ave) {
        sum += a[i];
      } else {
        sum = a[i];
        c++;
      }
    }
//    eprintf("%lld, %d\n", ave, c);
    if (c > 3) {
      left = ave;
    } else {
      right = ave;
    }
  }
  printf("Case #%d: %.20lf\n", test, 1 - (1. * right / total));
}

int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
