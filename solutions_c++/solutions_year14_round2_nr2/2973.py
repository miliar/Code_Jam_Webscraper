#include <iostream>
#include <cstdio>
#include <unordered_set>
#include <vector>

using namespace std;

unsigned long long A, B, K;

void work() {
  unsigned long long res = 0, val;
  for (unsigned long long a = 0; a < A; ++a) {
    for (unsigned long long b = 0; b < B; ++b) {
      val = a & b;
      if (val < K) {
        ++res;
      }
    }
  }

  printf("%llu\n", res);
}

int main() {
  int T;
  cin >> T;

  for (int i = 1; i <= T; ++i) {
    cin >> A >> B >> K;
    printf("Case #%d: ", i);
    work();
  }

  return 0;
}
