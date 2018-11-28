#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
using std::string;
using std::vector;

struct Num {
  int number, lcost, rcost;
}a[1111];
int n;

bool CmpNum(const Num &x, const Num &y) {
  return x.number < y.number;
}

int Work() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &a[i].number);
  }
  int ans = 0;
  for (int i = 0; i < n; ++i) {
    int lcost = 0, rcost = 0;
    for (int j = 0; j < i; ++j) {
      if (a[j].number > a[i].number)
        lcost++;
    }
    for (int j = i + 1; j < n; ++j) {
      if (a[j].number > a[i].number)
        rcost++;
    }
    ans += std::min(lcost, rcost);
  }
  return ans;
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; ++i) {
    printf("Case #%d: %d\n", i, Work());
  }
  return 0;
}
