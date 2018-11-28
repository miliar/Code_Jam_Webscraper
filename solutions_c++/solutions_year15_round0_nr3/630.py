#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

const int M = 200000;
char ijk[M];

inline char mult(char a, char b) {
  static const char mlt[5][5] = {
    {0, 0,  0,  0,  0},
    {0, 1,  2,  3,  4},
    {0, 2, -1,  4, -3},
    {0, 3, -4, -1,  2},
    {0, 4,  3, -2, -1}
  };

  char sign = a * b > 0 ? 1 : -1;
  if (a < 0) a = -a;
  if (b < 0) b = -b;
  return sign * mlt[(int)a][(int)b];
}

inline char trn(char a) {
  switch (a) {
    case 'i':
    return 2;
    case 'j':
    return 3;
    case 'k':
    return 4;
    default:
    return -1;
  }
}

bool check(int l) {
  const char ij = mult(trn('i'), trn('j'));
  if (ijk[l - 1] != mult(ij, trn('k')))
    return false;
  
  for (int i = 0; i < l; ++i) {
    if (ijk[i] != trn('i')) continue;
    for (int j = i + 1; j < l; ++j) {
      if (ijk[j] == ij) return true;
    }
  }
  return false;
}

void solve() {
  int x, l;
  long long lx;
  scanf("%d%lld%s", &l, &lx, ijk);
  x = min(lx, 8 + lx % 4);
  for (int i = 0; i < l; ++i) {
    ijk[i] = trn(ijk[i]);
  }
  for (int i = l; i < l * x; ++i) {
    ijk[i] = ijk[i - l];
  }
  l *= x;
  for (int i = 1; i < l; ++i) {
    ijk[i] = mult(ijk[i - 1], ijk[i]);
  }
  printf("%s\n", check(l) ? "YES" : "NO");
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
