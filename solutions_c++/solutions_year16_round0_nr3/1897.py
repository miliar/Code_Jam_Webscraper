#include <cstdio>
#include <string>
#include <algorithm>
#define scanf(args...) (scanf(args) ? : 0)
typedef __int128 LL;

std::string to_binary(unsigned t) {
  std::string str;
  while (t > 0) {
    str += t % 2 + '0';
    t /= 2;
  }
  std::reverse(str.begin(), str.end());
  return str;
}

int is_prime(LL n) {
  int t = 2;
  while (t * t <= n) {
    if (n % t == 0)
      return t;
    t++;
    if (t >= 100)
      return -1;
  }
  return -1;
}

LL convert(unsigned mask, int base) {
  LL result = 0, pbase = 1;
  while (mask > 0) {
    result += (mask % 2) * pbase;
    mask /= 2;
    pbase *= base;
  }
  return result;
}

bool check(unsigned int t) {
  for (int i = 2; i <= 10; i++)
    if (is_prime(convert(t, i)) == -1)
      return false;
  return true;
}

void solve(int n, int j) {
  int cnt = 0;
  for (unsigned t = 0; t < (1u << (n - 2)); t++) {
    unsigned value = t * 2 + 1 + (1 << (n - 1));
    if (check(value)) {
      cnt++;
      printf("%s ", to_binary(value).c_str());
      for (int i = 2; i <= 10; i++)
        printf("%d ", is_prime(convert(value, i)));
      printf("\n");

      if (cnt == j)
        return;
    }
  }
}

int main() {
  int test_count;
  scanf("%d", &test_count);

  for (int t = 1; t <= test_count; t++) {
    int n, j;
    scanf("%d%d", &n, &j);
    printf("Case #%d: \n", t);
    solve(n, j);
  }
}
