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

const int N = 200;
const long long M = 1000000007LL;
char cars[N][N];

enum LE {
  NO = 0,
  X = 1,
  I = 2,
  R = 3,
  L = 4,
  W = 5,
  LW = 6,
  RW = 7,
  IW = 8,
};

LE le['z' + 1];
int cnt['z' + 1];

LE checkLetter(int c, char l) {
  LE ret = NO;
  if (cars[c][0] == l) {
    ret = W;
  }
  for (int i = 1; cars[c][i]; ++i) {
    if (cars[c][i] == l) {
      switch (ret) {
        case W:
        case R:
        case X:
          break;
        case NO:
          ret = R;
          break;
        case L:
        case I:
          ret = X;
          break;
        default:
        break;
      }
    } else {
      switch (ret) {
        case NO:
        case L:
        case I:
        case X:
          break;
        case R:
          ret = I;
          break;
        case W:
          ret = L;
          break;
        default:
        break;
      }
    }
  }
  return ret;
}

LE update(LE a, LE b) {
  if (a < b) {
    return update(b, a);
  }
  switch (b) {
    case NO:
      return a;
    case X:
    case I:
      return X;
    case R:
      if (a == R || a == RW || a == IW) 
        return X;
      if (a == W)
        return RW;
      if (a == L || a == LW)
        return IW;
    case L:
      if (a == L || a == LW || a == IW)
        return X;
      if (a == W) 
        return LW;
      if (a == RW)
        return IW;
    case W:
      return a;
    case LW:
      if (a == LW || IW) return X;
      if (a == RW) return IW;
    case RW:
    case IW:
      return X;
  }
  return X;
}

void updateLetter(char i, LE l) {
  if (l != NO) {
    ++cnt[(int)i];
  }
  le[(int)i] = update(le[(int)i], l);
}

long long fact(int n) {
  long long r = 1;
  for (int i = 2; i <= n; ++i) {
    r *= i;
    r %= M;
  }
  return r;
}

long long mult(int i, int &left) {
  LE l = le[i];
  switch (l) {
    case NO:
    case I:
    case R:
      return 1;
    case X:
      return 0;
    case L:
      ++left;
      return 1;
    case W:
      ++left;
      return fact(cnt[i]);
    case LW:
      ++left;
      return fact(cnt[i] - 1);
    case RW:
      return fact(cnt[i] - 1);
    case IW:
      return fact(cnt[i] - 2);
  }
  return 0;
}

void solve() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%s", cars[i]);
  }

  long long ret = 1;
  int left = 0;
  for (int i = 'a'; i <= 'z'; ++i) {
    le[i] = NO;
    cnt[i] = 0;
    for (int j = 0; j < n; ++j) {
      LE l = checkLetter(j, i);
      updateLetter(i, l);
    }
    ret *= mult(i, left);
    ret %= M;
  }
  if (!left) {
    ret = 0;
  } else {
    ret *= fact(left);
  }
  ret %= M;
  printf("%lld\n", ret);
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
