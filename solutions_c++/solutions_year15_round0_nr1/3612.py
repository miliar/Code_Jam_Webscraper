#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <fstream>

#ifdef DK
const int MAX = 13;
#else
const int MAX = 1e2 + 11;
#endif

using namespace std;

int main() {
#ifdef DK
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  int T = 0;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    int N = 0;
    string A;
    cin >> N >> A;
    int res = 0, cur = 0;
    for (int i = 0; i < A.length(); ++i) {
      int x = A[i] - '0';
      int v = i - cur;
      if (i > cur) {
        res += v;
        cur += v;
      }
      cur += x;
    }
    cout << "Case #" << t + 1 << ": " << res << "\n";
  }
  return 0;
}