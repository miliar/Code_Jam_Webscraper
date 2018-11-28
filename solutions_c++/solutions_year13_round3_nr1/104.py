#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 1000005;

char s[MaxN];
int prev[MaxN];

bool check(char c) {
  return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int getC(int i, int j) {
  if (prev[j] == -1)
    return -1;
  if (prev[j] > i)
    return j - prev[j] + 1;
  return j - i + 1;
}

int main() {
  int T, n, cnt, m;

  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);

  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    scanf("%s%d", s, &m);
    n = strlen(s);
    for (int i = 0; i < n; ++i) {
      if (!check(s[i]))
        prev[i] = (i == 0 || prev[i - 1] == -1) ? i : prev[i - 1];
      else
        prev[i] = -1;
    }
    long long ret = 0;
    for (int i = 0, j = 0; i < n; ++i) {
      if (j < i) j = i;
      while (j < n) {
        cnt = getC(i, j);
        if (cnt < m)
          ++j;
        else
          break;
      }
      cnt = getC(i, j);
      if (cnt < m) break;
      ret += n - j;
    }
    printf("Case #%d: %lld\n", cas, ret);
  }

  return 0;
}

