#include <stdio.h>
#include <vector>
#include <string.h>
#include <iostream>

using namespace std;

long long myPow(long long x, long long e) {
  long long result;

  if (e == 0) result = 1;
  else if (e == 1) result = x;
  else {
    result = myPow(x, e / 2);
    result = result * result;
    if (e % 2) result = result * x;
  }
  return result;
}

void solve() {
  long long k, c, s;
  cin >> k >> c >> s;
  cout << 1;
  long long inc = 0;
  for(long long i = c-1; i >= 0; i--) inc += myPow(k, i);
  long long counter = 1;
  for(int i = 1; i < k; i++) {
    counter += inc;
    cout << " " << counter;
  }
  cout << endl;
}

int main() {
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
