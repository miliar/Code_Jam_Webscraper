#include <bits/stdc++.h>
using namespace std;

const int COMPLETE = (1 << 10) - 1;

int main() {
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; ++caso) {
    long N;
    cin >> N;
    int mask = 0;
    
    auto add = [&] (int value) {
      while (value) {
        mask |= (1 << (value % 10));
        value /= 10;
      }
    };
    
    printf("Case #%d: ", caso);
    
    if (N == 0) printf("INSOMNIA\n");
    else {
      add(N);
      long x = N;
      while (mask != COMPLETE) {
        x += N;
        add(x); 
      }
      printf("%ld\n", x);
    }
  }  
  return 0;
}