#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  long long test_num, k, num;
  scanf("%lld", &test_num);

  for (unsigned i (0); i < test_num; ++i) {
    scanf("%lld", &k);

    long long counter1 = 0, counter2 = 0;
    int temp;
    unsigned res = 0;
    while (counter2 <= k) {
      scanf("%1d", &temp);
      if (counter2 > counter1) {
        res += counter2 - counter1;
        counter1 = counter2;
      }
      counter1 += temp;
      counter2++;
    }
    printf("Case #%d: %u\n", i + 1, res);
  }
}