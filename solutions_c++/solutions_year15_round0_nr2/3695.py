#include <iostream>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <algorithm>
#include <functional>
#include <limits.h>
#include <bitset>

#include <tuple>
#include <unordered_map>

#define mp make_pair
#define mt make_tuple
#define pb push_back
#define rep(i, n) for (int i = 0; i < (n); i++)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

const int INF = 1 << 29;
const double EPS = 1e-9;

const int dx[] = {1, 0, -1, 0}, dy[] = {0, -1, 0, 1};
int T;

int main() {
  cin >> T;
  int testcase = 1;
  while (T--) {
    int D;
    cin >> D;
    vector<int> P;
    P.resize(D);
    for (int i = 0; i < D; i++) {
      cin >> P[i];
    }
    sort(P.begin(), P.end());
    reverse(P.begin(), P.end());
    int maxP = P[0];
    int minT = INF;
    for (int i = 1; i <= maxP; i++) {
      int tmpP = 0;
      for (int j = 0; j < P.size(); j++) {
        if (P[j] <= i) {
          break;
        }
        tmpP += ceil((double)P[j] / i) - 1;
      }
      minT = min(minT, tmpP + i);
    }

    printf("Case #%d: %d\n",testcase++, minT);
  }
  return 0;
}