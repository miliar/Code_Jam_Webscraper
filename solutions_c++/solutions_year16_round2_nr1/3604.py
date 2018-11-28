#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N = 100005;
const int M = 1000000007;

char s[N];
int len;
int cnt[26];
int ans[10];
int need[10][26];
string num[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
bool ok;

bool check(int x, int k) {
  for (int i = 0; i < 26; i++) { if (cnt[i] < need[x][i] * k) { return false; } }
  return true;
}

void dfs(int pos) {
  if (ok) { return; }
  if (pos == 10) {
    if (all_of(cnt, cnt + 26, [](int x) {return x == 0;})) { ok = true; }
    return;
  }
  for (int i = 0; !ok && i * (int)num[pos].size() <= len; i++) {
    if (check(pos, i)) {
      for (int j = 0; j < 26; j++) { cnt[j] -= need[pos][j] * i; }
      ans[pos] = i; dfs(pos + 1);
      for (int j = 0; j < 26; j++) { cnt[j] += need[pos][j] * i; }
    }
  }
}

int main() {
  freopen("A-small-attempt1.in", "r", stdin);
  freopen("A.out", "w", stdout);

  for (int i = 0; i < 10; i++) {
    for (char c : num[i]) { need[i][c - 'A']++; }
  }
  int C = 0, T;
  scanf("%d", &T);
  while (++C <= T) {
    scanf("%s", s);
    memset(cnt, 0, sizeof(cnt));
    len = strlen(s);
    for (int i = 0; i < len; i++) { cnt[s[i] - 'A']++; }
    ok = false;
    dfs(0);
    printf("Case #%d: ", C);
    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < ans[i]; j++) { putchar(i + '0'); }
    }
    puts("");
  }
}
