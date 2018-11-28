#define TASKNAME "text"

#include <bits/stdc++.h>

int main()
{
  freopen(TASKNAME".in", "r", stdin);
  freopen(TASKNAME".out", "w", stdout);
  int n;
  std::cin >> n;
  for (int t = 0; t < n; t++) {
      printf("Case #%d: ", t + 1);
      int x;                   
      std::cin >> x;
      std::string s;
      std::cin >> s;
      std::vector<int> cnt(x + 1, 0);
      for (int j = 0; j < x + 1; j++) {
          cnt[j] += s[j] - '0';
      }
      int nowStanding = 0;
      int ans = 0;
      for (int i = 0; i < x + 1; i++) {
          if (nowStanding < i && cnt[i] > 0) {
              ans += (i - nowStanding);
              nowStanding = i + cnt[i];
          } else {
              nowStanding += cnt[i];
          }
      }
      printf("%d\n", ans);
  }                     
  return 0;
}
