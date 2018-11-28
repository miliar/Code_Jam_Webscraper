#include <iostream>
using namespace std;

using int64 = long long;

int64 safe_pow(int base, int power) {
  int64 res = 1;
  for (int i = 0; i < power; ++i) {
    res *= base;
  }
  return res;
}

int main() {
  int tc;
  cin >> tc;
  
  for (int tcase = 1; tcase <= tc; ++tcase) {
    cout << "Case #" << tcase << ":";
    
    int k, c, s;
    cin >> k >> c >> s;
    
    if (k > c * s) {
      cout << " IMPOSSIBLE\n";
      continue;
    }
    
    //if (c > k) c = k;
    //const int64 iter_growth = c * safe_pow(k, c - 1);
    
    int next = 1;
    
    while (next <= k) {
      const int n_we_will_take = min(k - next + 1, c);
      
      int64 x = next;
      for (int i = 1; i < n_we_will_take; ++i) {
          x = (x - 1) * k + (next + i);
      }
      cout << " " << x;
      
      next += n_we_will_take;
    }
    
    cout << "\n";
  }
  
  return 0;
}
