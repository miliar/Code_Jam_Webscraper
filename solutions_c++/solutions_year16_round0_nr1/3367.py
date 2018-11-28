#include <stdio.h>
#include <bitset>

using namespace std;

long long int t, n, new_n, i, new_n_copy, first_t;

int main() {
  scanf("%lld", &t);
  first_t = t;
  bitset<10> seen;

  while (t--) {
    scanf("%lld", &n);
    seen.reset();

    if (n == 0) {
      printf("Case #%lld: INSOMNIA\n", first_t - t);
      continue;
    }
    
    i = 1;
    while (true) {
      new_n = n * i++;
      new_n_copy = new_n;

      do {
        int digit = new_n_copy % 10;
        seen[digit] = 1;
        new_n_copy /= 10;
      } while (new_n_copy > 0 && seen != (1 << new_n) - 1);

      if (seen.all()) {
        printf("Case #%lld: %lld\n", first_t - t, new_n);
        break;
      }
    }
  }
}
