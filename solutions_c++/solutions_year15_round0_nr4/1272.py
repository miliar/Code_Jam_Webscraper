#include <cstdio>
#include <cassert>
#include <string>
#include <algorithm>
using std::string;

string ri = "RICHARD", ga = "GABRIEL";

string Work() {
  int x, l, s;
  assert(scanf("%d%d%d", &x, &l, &s) == 3);
  if (s > l) std::swap(l, s);
  if (x > l) return ri;
  if ((x + 1) / 2 > s) return ri;
  if ((x + 1) / 2 == s) {
    if (x >= 4) return ri;
  }
  if (x >= 7) return ri;
  if (l * s % x) return ri;
  return ga;
}

int main() {
  int cases;
  assert(scanf("%d", &cases) == 1);
  for (int i = 1; i <= cases; ++i)
    printf("Case #%d: %s\n", i, Work().c_str());
  return 0;
}
