#include <cstdio>
#include <string>
const int MAXN = 1000005;

char buffer[MAXN];

char flip(char c) {
  return c == '+' ? '-' : '+';
}

int solve(const std::string& str) {
  bool changed = false;
  int result = 0;
  for (int i = str.size() - 1; i >= 0; i--) {
    char sgn = changed ? flip(str[i]) : str[i];
    if (sgn == '-')
      changed ^= 1, result++;
  }
  return result;
}

int main() {
  int test_count;
  scanf("%d", &test_count);

  for (int t = 1; t <= test_count; t++) {
    scanf("%s", buffer);
    printf("Case #%d: %d\n", t, solve(buffer));
  }
}
