#include <bits/stdc++.h>

using namespace std;

long long power(long long a, long long b) {
  if (a == 1) return 1;
  if (b == 0) return 1;
  if (b == 1) return a;
  long long t = power(a, b >> 1);
  return t * t * (b & 1 ? a : 1);
}

int main()  {
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    cout << "Case #" << tc << ": ";
    int k, c, s;
    cin >> k >> c >> s;
    if (k == 1) {
      cout << 1 <<endl;
    }
    else if (c == 1 and s < k) {
      cout << "IMPOSSIBLE" << endl;
    }
    else if (c == 1 and s >= k) {
      for (int i = 1; i <= k; i++)
        cout << i << " ";
      cout << endl;
    }
    else if (k == 2) {
      cout << 2 << endl;
    }
    else if(k == 3) {
      cout << "2 3" << endl;
    } else {
      for (int i = 2; i <= k - 2; i++)
        cout << i << " ";
      cout << power(k, c) - k << endl;
    }
  }
  return 0;
}