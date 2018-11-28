#include <bits/stdc++.h>

using namespace std;

const int N = 2222;
char s[N], res[N];
int cnt[26];

const string dig[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR",
    "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int cntdig[10][26];

void init() {
  for (int d = 0; d < 10; ++d) {
    int n = dig[d].size();
    for (int i = 0; i < n; ++i)
      ++cntdig[d][dig[d][i] - 'A'];
  }
}

bool exists(int d) {
  bool good = true;
  for (int i = 0; i < 26; ++i)
    good &= cnt[i] >= cntdig[d][i];
  if (!good)
    return false;
  for (int i = 0; i < 26; ++i)
    cnt[i] -= cntdig[d][i];
  return true;
}

void solve() {
  int d[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  do {
    int sz = 0;
    memset(res, 0, sizeof res);
    for (int i = 0; i < 10; ++i) {
      while (exists(d[i]))
        res[sz++] = d[i] + '0';
    }
    bool check = true;
    for (int i = 0; i < 26; ++i)
      check &= cnt[i] == 0;
    if (check) {
      sort(res, res + sz);
      return;
    }
    for (int i = 0; i < sz; ++i) {
      for (int j = 0; j < 26; ++j)
        cnt[j] += cntdig[res[i] - '0'][j];
    }
  } while (next_permutation(d, d + 10));
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  init();
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    memset(cnt, 0, sizeof cnt);
    scanf("%s", s);
    int n = strlen(s);
    for (int i = 0; i < n; ++i)
      ++cnt[s[i] - 'A'];
    solve();
    printf("Case #%d: %s\n", tst, res);
    ++tst;
  }
}
