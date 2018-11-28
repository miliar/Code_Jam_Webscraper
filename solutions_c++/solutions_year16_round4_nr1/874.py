#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <cstdio>
#include <unordered_set>
using namespace std;

///////////////// macros and typedefs ///////////////////
#define rep(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define repd(i, n) for (int i = (n)-1; i >= 0; --i)
#define DEB(k) cerr << "debug: " #k << "=" << k << endl;
#define CLEAR(a) memset((a), 0, sizeof(a));
#define all(c) (c).begin(), (c).end()
#define mp(a, b) make_pair(a, b)
#define l(c) (int)((c).size())
#define sqr(a) ((a) * (a))
#define inf 0x7f7f7f7f
#define pb push_back
#define ppb pop_back
#define x first
#define y second
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

using namespace std;

string A[12][3];

void solveCase() {
  int N, R, P, S;
  cin >> N >> R >> P >> S;
  N--;
  rep(i, 3) {
    int r = 0, p = 0, s = 0;
    rep(j, l(A[N][i])) {
      if (A[N][i][j] == 'R') r++;
      else if (A[N][i][j] == 'P') p++;
      else if (A[N][i][j] == 'S') s++;
    }
    if (R == r && P == p && S == s) {
      cout << A[N][i];
      return;
    }
  }
  cout << "IMPOSSIBLE";
}

#define NAME "A-large"
//#define NAME "A-small-attempt0"
//#define NAME "test"

int main() {
  freopen(NAME ".in", "rt", stdin);
  freopen(NAME ".out", "wt", stdout);
  A[0][0] = "PR";
  A[0][1] = "PS";
  A[0][2] = "RS";
  for (int i = 1; i < 12; i++) {
    A[i][0] = A[i-1][0] + A[i-1][1];
    A[i][1] = A[i-1][0] + A[i-1][2];
    A[i][2] = A[i-1][1] + A[i-1][2];
  }
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    //cerr << "Case #" << i << ": ";
    solveCase();
    cout << endl;
    //cerr << endl;
  }
  return 0;
}
