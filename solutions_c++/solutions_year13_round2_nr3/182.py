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

char dict[600000][12];
int len[600000];
int dn;

int DP[5][5000];
char text[5000];
int n;

void readDict() {
  FILE *fp = fopen("garbled_email_dictionary.txt", "r");
  for (dn = 0; fscanf(fp, "%s", dict[dn]) == 1; ++dn) {
    len[dn] = strlen(dict[dn]);
  }
}

inline int match(int i, int j, int &l) {
  int r = 0;
  for (int k = 0; dict[j][k]; ++k) {
    if (dict[j][k] == text[i + k]) continue;
    if (k - l < 5) return -1;
    if (!text[i + k]) return -1;
    ++r;
    l = k;
  }
  return r;
}

int dp(int i, int k) {
  int &ret = DP[k][i];
  if (ret >= 0) return ret;
  ret = 50000;
  for (int j = 0; j < dn; ++j) {
    int l = k - 5;
    int r = match(i, j, l);
    if (r < 0) continue;
    ret = min(ret, r + dp(i + len[j], max(0, 5 + l - len[j])));
  }
  return ret;
}

void solve() {
  scanf("%s", text);
  n = strlen(text);
  for (int k = 0; k < 5; ++k) {
    for (int i = 0; i < n; ++i) DP[k][i] = -1;
    DP[k][n] = 0;
  }
  printf("%d\n", dp(0, 0));
}

int main() {
  readDict();
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
