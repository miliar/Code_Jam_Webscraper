#include <bits/stdc++.h>

using namespace std;

int n;
int ans;
int bits[1 << 6];
int mask[1 << 6];
int nmask[1 << 6];
int p[6];
bool used[6];

bool dfs2(int i) {
  if (i == n) {
    return true;
  }
  bool ok = false;
  for (int j = 0; j < n; ++j) {
    if (used[j]) {
      continue;
    }
    if ((mask[p[i]] & (1 << j)) || (nmask[p[i]] & (1 << j))) {
      ok = true;
      used[j] = true;
      if (!dfs2(i + 1)) {
        return false;
      }
      used[j] = false;
    }
  }
  return ok;
}

bool check() {
  for (int i = 0; i < n; ++i) {
    p[i] = i;
  }
  do {
    memset(used, false, sizeof used);
    if (!dfs2(0)) {
      return false;
    }
  } while (next_permutation(p, p + n));
  return true;
}

void dfs(int i) {
  if (i == n) {
    if (check()) {
      int cur = 0;
      for (int j = 0; j < n; ++j) {
        cur += bits[nmask[j]];
      }
      /*
      if (cur == 2) {
        for (int j = 0; j < n; ++j) {
          for (int kk = 0; kk < n; ++kk) {
            cout << ((nmask[j] >> kk) & 1);
          }
          cout << endl;
        }
      }
      printf("\n");
      */
      ans = min(ans, cur);
    }
    return;
  }
  for (int j = 0; j < (1 << n); ++j) {
    if ((j & mask[i]) != 0) {
      continue;
    }
    nmask[i] = j;
    dfs(i + 1);
  }
}

char s[10];

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  freopen("log", "w", stderr);
  bits[0] = 0;
  for (int i = 1; i < (1 << 5); ++i) {
    bits[i] = bits[i & (i - 1)] + 1;
  }
  int tt;
  scanf("%d", &tt);
  for (int cc = 1; cc <= tt; ++cc) {
    printf("Case #%d: ", cc);
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%s", s);
      mask[i] = 0;
      for (int j = 0; j < n; ++j) {
        if (s[j] == '1') {
          mask[i] |= (1 << j);
        }
      }
    }
    ans = 1e9;
    dfs(0);
    printf("%d\n", ans);
  }
  return 0;
}