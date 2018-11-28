#include <cstdio>

const int MAXN = 1010;

int main() {
  int T;
  scanf("%d", &T);

  int times = 1;
  while (T--) {
    int smax;
    scanf("%d", &smax);

    char people[MAXN];
    scanf("%s", people);

    int cnt = 0;
    int ans = 0;
    for (int i = 0; i != smax + 1; i++) {
      if (cnt < i) {
        ans += i - cnt;
        cnt = i;
      }

      cnt += static_cast<int>(people[i] - '0');
    }

    printf("Case #%d: %d\n", times++, ans);
  }

  return 0;
}