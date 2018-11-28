#include <cstdio>
#include <set>
#define scanf(args...) (scanf(args) ? : 0)
typedef long long int LL;

LL solve(int n) {
  if (n == 0)
    return -1;
  std::set<int> digits;
  LL result = n;
  while (true) {
    LL t = result;
    while (t > 0) {
      digits.insert(t % 10);
      t /= 10;
    }

    if (digits.size() == 10)
      return result;
    result += n;
  }
}

int main() {
  int test_count;
  scanf("%d", &test_count);

  for (int t = 1; t <= test_count; t++) {
    int n;
    scanf("%d", &n);
    printf("Case #%d: ", t);
    LL r = solve(n);
    if (r == -1)
      printf("INSOMNIA\n");
    else
      printf("%Ld\n", solve(n));
  }
}
