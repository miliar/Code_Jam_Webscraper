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

const int maxn = (int)1e5;

int a[maxn];

void solve(int test) {
  int n, x;
  scanf("%d%d", &n, &x);
  for (int i = 0; i < n; i++) scanf("%d", &a[i]);
  int res = 0;
  sort(a, a + n);
  reverse(a, a + n);
  int i = 0;
  int j = n - 1;
  while (i <= j) {
    if (a[i] + a[j] <= x) {
      i++, j--;
      res++;
    } else {
      res++;
      i++;
    }
  }
  printf("Case #%d: %d\n", test, res);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
