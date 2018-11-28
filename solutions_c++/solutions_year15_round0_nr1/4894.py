#include <stdio.h>

int solve(int s_max, char audiences[]) {
  int standings = 0;
  int required_friends = 0;
  for (int i = 0; i < s_max + 1; i++) {
    if (standings < i) {
      int addition = i - standings;
      standings += addition;
      required_friends += addition;
    }
    standings += audiences[i];
  }
  return required_friends;
}

int main() {
  int t = 0;
  scanf("%d", &t);

  for (int i = 0; i < t; i++) {
    int s_max = 0;
    char audiences[1001];
    scanf("%d %s", &s_max, audiences);
    for(int j = 0; j < s_max + 1; j++)
      audiences[j] -= '0';
    int result = solve(s_max, audiences);
    printf("Case #%d: %d\n", i + 1, result);
  }
  return 0;
}
