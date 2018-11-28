#include <cstdio>
#include <cstring>

int solve() {
  int ans = 0, sl;
  char s[101];
  scanf("%s", s);
  sl = strlen(s);
  while (1) {
    int i = sl - 1;
    while (i >= 0 && s[i] == '+')
      i--;
    if (i == -1)
      return ans;
    int j = 0;
    while (s[j] == '+')
      j++;
    if (j) {
      ans++;
      while (j--)
	s[j] = '-';
    }
    ans++;
    for (j = 0; j <= i - j; j++) {
      if (s[j] == '+' && s[i - j] == '+')
	s[j] = '-', s[i - j] = '-';
      else if (s[j] == '+' && s[i - j] == '-')
	s[j] = '+', s[i - j] = '-';
      else if (s[j] == '-' && s[i - j] == '+')
	s[j] = '-', s[i - j] = '+';
      else if (s[j] == '-' && s[i - j] == '-')
	s[j] = '+', s[i - j] = '+';
    }
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++)
    printf("Case #%d: %d\n", i, solve());
}
