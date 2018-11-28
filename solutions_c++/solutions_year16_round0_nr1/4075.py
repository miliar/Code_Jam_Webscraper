#include <bits/stdc++.h>
using namespace std;
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

int T;

int main() {
#ifdef msci
  //freopen("input.txt", "r", stdin);
#endif
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    fflush(stdout);
    // begin solution
    unsigned long long n;
    cin >> n;   
    if (n == 0) {
      printf("INSOMNIA\n");
      continue;
    }
    bitset<10> bit;
    unsigned long long index = 1;
    while (bit.count() < 10) {
      unsigned long long temp = n * index;
      index++;
      while (temp != 0) {
        bit[temp % 10] = true;
        temp /= 10;
      }
    }
    cout << n * (index - 1) << "\n";
    fflush(stdout);
    //end solution
  }
  return 0;
}
