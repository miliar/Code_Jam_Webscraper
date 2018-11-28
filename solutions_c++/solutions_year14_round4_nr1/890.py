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

const int maxn = 100000;

int n;
int x;
int s[maxn];
bool was[maxn];

int tests;

bool check(int k){ 
  int cnt = n;
  for (int i = 0; i < n; i++)
    was[i] = false;
  for (int i = 0; i < n; i++) {
    if (was[i])
      continue;
    int j = i + 1;
    while (j < n && (was[j] || s[i] + s[j] > x)) j++;
    if (j == n) {
      cnt--;   
      was[i] = true;
      k--;
      if (cnt == 0) {
        return 1;
      }
      if (k == 0)
        break;
    }
    else {
      for (int z = j; z < n; z++) {
        if (!was[z] && s[i] + s[z] <= x && s[z] > s[j])
          j = z;
      }
      cnt -= 2;
      was[i] = was[j] = true;
      k--;
      if (cnt == 0) {
        return 1;
      }
      if (k == 0)
        break;
    }            
  }
  return 0;
}

int main() {
  assert(freopen("input.txt", "rt", stdin));
  assert(freopen("output.txt", "wt", stdout));
  scanf("%d", &tests);
  for (int test = 0; test < tests; test++) {
    printf("Case #%d: ", test + 1);
    scanf("%d %d", &n, &x);
    for (int i = 0; i < n; i++)
      scanf("%d", &s[i]);
    int l = 0;
    int r = maxn;
    while (r - l > 1) {
      int m = (l + r) / 2;
      if (check(m))
        r = m;
      else 
        l = m;
    }
    printf("%d\n", r);
  }
  
  return 0;
}