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

int n;
int k;
double p[222];
//double dp[222][222][222];
double dp[17][17];
double P[17];

double get(int from, int yes) {
  if (from == k) return yes == k/2 ? 1 : 0;
  if (dp[from][yes] >= 0) return dp[from][yes];
  double A = 0;
  A += (1 - P[from]) * get(from + 1, yes);
  A += P[from] * get(from + 1, yes + 1);
  return dp[from][yes] = A;
}

void solveCase() {
  cin >> n >> k;
  rep(i, n) cin >> p[i];
  double answer = 0;
  rep(mask, 1<<n) {
    int bc = 0;
    rep(i, n) if ((mask >> i)&1) {
      P[bc] = p[i];
      bc++;
    }
    if (bc != k) continue;
    rep(i, 17) rep(j, 17) dp[i][j] = -1;
    double cur = get(0, 0);
    answer = max(answer, cur);
  }
  //rep(i, 222) rep(j, 222) rep(k, 222) dp[i][j][k] = -1;
  //double answer = get(0, k, 0);
  printf("%.10lf", answer);
}

//#define NAME "A-large"
#define NAME "B-small-attempt0"
//#define NAME "test"

int main() {
  freopen(NAME ".in", "rt", stdin);
  freopen(NAME ".out", "wt", stdout);
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
