#include <cstdio>
#include <iostream>
#include <ctime>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <bitset>

using namespace std;

typedef long long int int64;
typedef long double ext;

int tests;

const int inf = 1000000000;

const int maxn = 2000;
int n;
int a[maxn], b[maxn];

bool check() {
  int i = 1;
  while (i < n && a[b[i]] > a[b[i - 1]])
    i++;
  for (int j = i + 1; j < n; j++)
    if (a[b[j]] >= a[b[j - 1]])
      return 0;
  return 1;
}

int count() {
  int res = 0;
  int c[maxn];
  for (int i = 0; i < n; i++)
    c[i] = i;
  for (int i = 0; i < n; i++) {
    int j = i;
    while (j < n && c[j] != b[i])
      j++;
    assert(j < n);
    for (int z = j - 1; z >= i; z--) {
      swap(c[z], c[z + 1]);
      res++;
    }
  }
  return res;
}

int main() {
  assert(freopen("input.txt", "rt", stdin));
  assert(freopen("output.txt", "wt", stdout));
  scanf("%d", &tests);
  for (int test = 0; test < tests; test++) {
    printf("Case #%d: ", test + 1);
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%d", &a[i]);
      b[i] = i;
    }
    int mn = inf;
    do {
      if (!check())
        continue;
      mn = min(mn, count());
    } while (next_permutation(b, b + n));
    printf("%d\n", mn);         
  }
  return 0;
}