#include <stdio.h>

char people[1002];

int main() {
  int t, n;
  scanf("%d", &t);
  for (int c = 1; c <= t; ++c) {
    scanf("%d%s", &n, people);
    int invites = 0, standup = 0;
    for (int i = 0; i <= n; ++i) {
      if (standup < i && '0' < people[i])
        invites += i - standup, standup += i - standup;
      standup += people[i] - '0';
    }
    printf("Case #%d: %d\n", c, invites);
  }
  return 0;
}