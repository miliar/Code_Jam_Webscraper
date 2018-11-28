#include <iostream>
#include <cstring>

using namespace std;

#define ALLSET ((1<<10)-1)
long checkSlow(long x) {
  int mask = 0;
  long y = 0;
  for (int i = 1; i <= 1000; i++) {
    y += x;
    long t = y;
    while (t != 0) {
      mask |= 1 << (t % 10);
      t /= 10;
    }
    if (mask == ALLSET) {
      break;
    }
  }
  if (mask != ALLSET) {
    return -1;
  }
  return y;
}

int main() {
  #ifdef TEST
  for (long i = 10000000; i < 10000000 + 200; i++) {
    cout << i << " " << checkSlow(i) << endl;
  }
  #else
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    long k;
    cin >> k;
    long ans = checkSlow(k);
    cout << "Case #" << i+1 << ": ";
    if (ans == -1) {
      cout << "INSOMNIA";
    } else {
      cout << ans;
    }
    cout << endl;
  }
  #endif
  return 0;
}
