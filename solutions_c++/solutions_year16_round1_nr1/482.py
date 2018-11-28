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
static const int N = 1002;

int findMax(const char* s, int l) {
  int mi = N-1;
  for (--l; l >= 0; --l) {
    if (s[mi] < s[l]) {
      mi = l;
    }
  }
  return mi;
}

void solve() {
  char letters[N];
  char suffix[N];
  int sl = 0;
  char prefix[N];
  int pl = 0;

  scanf("%s", letters);
  letters[N-1] = 0;
  int len = strlen(letters);
  int l = len;
  while (sl + pl < len) {
    int i = findMax(letters, l);
    for (int j = l - 1; j > i; --j) {
      suffix[sl++] = letters[j];
    }
    prefix[pl++] = letters[i];
    l = i;
  }
  reverse(suffix, suffix + sl);
  suffix[sl++] = prefix[pl++] = 0;
  printf("%s%s\n", prefix, suffix);
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
