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
const int MAX = 1e3 + 11;
#else
const int MAX = 1e3 + 11;
#endif

using namespace std;

int C[MAX];

int main() {
#ifdef DK
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  int T = 0;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    memset(C, 0, sizeof(C));
    int N = 0;
    cin >> N;
    for (int i = 0; i < N; ++i) {
      cin >> C[i];
    }
    int res = (int) 1e9;
    for (int i = 1; i < MAX; ++i) {
      int tmp = 0;
      for (int j = 0; j < N; ++j) {
        if (i < C[j]) {
          int c = C[j] - i;
          tmp += c / i + (c % i > 0);
        }
      }
      res = min(res, i + tmp);
    }
    cout << "Case #" << t + 1 << ": " << res << "\n";
  }
  return 0;
}