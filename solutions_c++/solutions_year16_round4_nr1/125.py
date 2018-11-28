#include <bits/stdc++.h>

const int N = 3;
const char s[] = "RPS";

int n;
int cnt[N];

std::string ans, cur;

std::string dfs(int a, int dep) {
  if (!dep) return std::string(1, s[a]);
  std::string u = dfs(a, dep - 1), v = dfs((a + 1) % 3, dep - 1);
  return u < v ? u + v : (v + u);
}

bool check(const std::string &s) {
  static int temp[N];
  memcpy(temp, cnt, sizeof cnt);
  for (int i = 0; i < s.length(); ++i) {
    int c = (s[i] == 'R' ? 0 : (s[i] == 'P' ? 1 : 2));
    if (--temp[c] < 0) return false;
  }
  return true;
}

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    scanf("%d%d%d%d", &n, &cnt[0], &cnt[1], &cnt[2]);
    std::string cur = dfs(0, n);
    ans = "";
    if (check(cur) && (ans.empty() || cur < ans)) ans = cur;
    cur = dfs(1, n);
    if (check(cur) && (ans.empty() || cur < ans)) ans = cur;
    cur = dfs(2, n);
    if (check(cur) && (ans.empty() || cur < ans)) ans = cur;
    if (ans.empty()) ans = "IMPOSSIBLE";
    printf("Case #%d: %s\n", tid, ans.c_str());
  }
  return 0;
}
