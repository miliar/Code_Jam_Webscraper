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

char out[10000000];
char tmp[10000000];

char win(char a, char b) {
  if (a == b) return 'x';
  if (a > b) swap(a, b);
  if (a == 'P') {
    if (b == 'R') return 'P';
    else return 'S';
  } else {
    return 'R';
  }
}

bool check(int n) {
  for (; n > 1; n /= 2) {
    for (int i = 0; i < n / 2; ++i) {
      tmp[i] = win(tmp[2*i], tmp[2*i + 1]);
      if (tmp[i] == 'x') return false;
    }
  }
  return true;
}

void solve() {
  int n, r, p, s;
  scanf("%d%d%d%d", &n, &r, &p, &s);
  n = 1 << n;
  for (int i = 0; i < p; ++i) out[i] = 'P';
  for (int i = 0; i < r; ++i) out[p + i] = 'R';
  for (int i = 0; i < s; ++i) out[p + r + i] = 'S';
  out[n] = 0;
  do {
    copy_n(out, n, tmp);
    if (check(n)) {
      printf("%s\n", out);
      return;
    }
  } while (next_permutation(out, out + n));
  printf("IMPOSSIBLE\n");
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
