#include <cstdio>

#include <algorithm>
#include <set>

using namespace std;

long long solve(long long n) {
  set<int> nums = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 };

  for (int i = 1;; i++) {
    long long num = n * i;
    while (num) {
      nums.erase(num % 10);
      num /= 10;
    }
    if (nums.empty()) return n * i;
    if (n * i < 0) break;
  }

  return -1;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int kase = 1; kase <= T; kase++) {
    long long n;
    scanf("%lld", &n);

    if (n == 0) printf("Case #%d: INSOMNIA\n", kase);
    else printf("Case #%d: %d\n", kase, solve(n));
  }

  return 0;
}
