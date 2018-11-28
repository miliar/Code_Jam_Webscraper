#include <bits/stdc++.h>

using namespace std;

const int N = 1 << 14;

int n, r, p, S;
int c[5], nc[5];
int cnt;
char s[N];

void dfs(int j, int d) {
  if (d == n) {
    if (j == 0) s[cnt++] = 'R';
    else if (j == 1) s[cnt++] = 'P';
    else s[cnt++] = 'S';
    return;
  }
  if (j == 0) dfs(0, d + 1), dfs(2, d + 1);
  else if (j == 1) dfs(1, d + 1), dfs(0, d + 1);
  else dfs(2, d + 1), dfs(1, d + 1);
}

void go(int l, int r) {
  if (l + 1 == r) return;
  int mid = (l + r) >> 1;
  go(l, mid);
  go(mid, r);
  int ok = 1;
  for (int i = l; i < mid; ++i) {
    if (s[i] > s[i + mid - l]) {
      ok = 0;
      break;
    }
  }
  if (!ok) {
    for (int i = l; i < mid; ++i) {
      swap(s[i], s[i + mid - l]);
    }
  }
}

int main() {
  int t;
  scanf("%d", &t);
  for (int _ = 1; _ <= t; ++_) {
    scanf("%d%d%d%d", &n, &r, &p, &S);
    memset(s, 0, sizeof(s));
    cnt = 0;
    //r, p, s
    int who = -1;
    for (int j = 0; j < 3; ++j) {
      memset(c, 0, sizeof(c));
      c[j] = 1;
      for (int i = 0; i < n; ++i) {
        memset(nc, 0, sizeof(nc));
        nc[0] += c[0];
        nc[2] += c[0];
        nc[0] += c[1];
        nc[1] += c[1];
        nc[2] += c[2];
        nc[1] += c[2];
        swap(nc, c);
      }
      if (c[0] == r && c[1] == p && c[2] == S) {
        who = j;
        break;
      }
    }
    printf("Case #%d: ", _);
    if (who == -1) {
      puts("IMPOSSIBLE");
    }
    else {
      dfs(who, 0);
      go(0, 1 << n);
      puts(s);
    }
  }
  return 0;
}
