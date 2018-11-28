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
  for (int i = 0; i < T; i++) {
    int smax;
    string slist;
    cin >> smax >> slist;
    int acnt = 0;
    int fcnt = 0;
    for (int k = 0; k <= smax; k++) {
      int d = slist[k] - '0';
      if (d != 0) {
        if (acnt < k) {
          fcnt += k - acnt;
          acnt = k;
        }
        acnt += d;
      }
    }
    printf("Case #%d: %d\n", i + 1, fcnt);
  }
  return 0;
}