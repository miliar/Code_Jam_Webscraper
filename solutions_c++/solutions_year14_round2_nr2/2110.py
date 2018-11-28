#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    int A, B, K;
    cin >> A; cin >> B; cin >> K;
    int count = 0;
    for (int i = 0; i < A; i++) {
      for (int j = 0; j < B; j++) {
        int k = i & j;
        //        printf("(%d, %d) -> %d\n", i, j, k);
        if (k < K) {
          count++;
        }
      }
    }
    printf("Case #%d: %d\n", t, count);
  }
}
