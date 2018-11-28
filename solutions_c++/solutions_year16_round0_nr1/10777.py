#include <bits/stdc++.h>
using namespace std;

int t, n;
bool seen[20];

bool check() {
  for (int i=0; i<=9; i++)
    if (!seen[i])
      return false;
  return true;
}

int main() {
  cin >> t;
  for (int c=1; c<=t; c++) {
    cin >> n;
    memset(seen, false, sizeof seen);

    int i;
    for (i=1; i<100 && !check(); i++) {
      int x = n*i;
      while (x > 0) {
        seen[x%10] = true;
        x /= 10;
      }
    }
    
    if (i >= 100)
      printf("Case #%d: INSOMNIA\n", c);
    else
      printf("Case #%d: %d\n", c, n*(i-1));
  }

  return 0;
}