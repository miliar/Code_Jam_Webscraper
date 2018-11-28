#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

int T;
long long B, N;
long long M[1000];

int main() {
  std::cin >> T;
  long long low, high, mid;

  for (int n_case = 1; n_case <= T; n_case++) {
    std::cin >> B >> N;
    low = 0;
    high = 0;
    for (int i = 0; i < B; i++) {
      std::cin >> M[i];
      if (M[i] > high) high = M[i];
    }
    high *= N;

    long long v, idx, n_cus, zeros;
    while (low < high) {
      mid = (low+high)/2;
      n_cus = zeros = 0;
      for (int i = 0; i < B; i++) {
        n_cus += (mid+M[i]-1)/M[i];
        if (mid % M[i] == 0) zeros++;
      }
      if (n_cus >= N) high = mid;
      else if (n_cus+zeros < N) low = mid+1;
      else {
        for (int i = 0; i < B; i++) {
          if (mid % M[i] == 0) n_cus++;
          if (n_cus == N) {
            std::printf ("Case #%d: %d\n", n_case, i+1);
            break;
          }
        }
        break;
      }
    }
  }

  return 0;
}
