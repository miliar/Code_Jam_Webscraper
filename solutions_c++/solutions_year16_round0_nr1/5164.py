#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int T, n, r, i;
bool b[10];

inline void f(int k) {
  while (k) {
    if (!b[k%10]) {
      b[k%10] = true;
      ++r;
    }
    k /= 10;
  }
}

int main() {
  cin >> T;
  for (int ti = 1; ti <= T; ++ti) {
    memset(b, 0, sizeof b);
    r = 0;
    cin >> n;
    if (n == 0) {
      cout << "Case #" << ti << ": " << "INSOMNIA" << endl;
      continue;
    }
    for (i = 1; r != 10; ++i)
      f(n*i);

    cout << "Case #" << ti << ": " << n*(i-1) << endl;
  }
  return 0;
}
