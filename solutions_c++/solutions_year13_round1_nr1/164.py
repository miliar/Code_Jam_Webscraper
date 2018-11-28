#include <iostream>
using namespace std;

int main() {
  int tc;
  long long r, t;
  scanf("%d", &tc);
  for (int cas = 1; cas <= tc; ++cas) {
    scanf("%lld%lld", &r, &t);
    unsigned int left = 0;
    unsigned int right = 2147483647;
    while (left < right) {
      unsigned int mid = (left + right) / 2 + 1;
      if ((t  + mid) / mid / 2 >= r + mid) {
        left = mid;
      } else {
        right = mid - 1;
      }
    }
    printf("Case #%d: %u\n", cas, left);
  }
  return 0;
}
