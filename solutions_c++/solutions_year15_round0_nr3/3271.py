#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>

using namespace std;

#define out(x) cerr << #x"=" << x << endl
#define INF 0xfffffff
#define N 10010

string str = "";
int dp[N][N];
int mul[256][256];
int len;

int multi(int a, int b) {
  int tt;
  if (a >= 0 && b >= 0) {
    tt = mul[a][b];
  }
  else if (a < 0 && b < 0) {
    tt = mul[-a][-b];
  }
  else if (a > 0) {
    tt = -mul[a][-b];
  }
  else {
    tt = -mul[-a][b];
  }
  return tt;
}

bool check() {
  for (int i = 1; i < len; ++i) {
    if (dp[0][i] == 'i') {
      for (int j = i+1; j < len; ++j) {
        if (dp[i][j] == 'j' && dp[j][len] == 'k') {
          return true;
        }
      }
    }
  }
  return false;
}

int main() {
  freopen("e.in", "r", stdin);
  freopen("e.out", "w", stdout);
  int t;
  scanf("%d", &t);
  mul['1']['1'] = '1';
  mul['i']['1'] = 'i';
  mul['j']['1'] = 'j';
  mul['k']['1'] = 'k';
  mul['1']['i'] = 'i';
  mul['i']['i'] = -'1';
  mul['j']['i'] = -'k';
  mul['k']['i'] = 'j';
  mul['1']['j'] = 'j';
  mul['i']['j'] = 'k';
  mul['j']['j'] = -'1';
  mul['k']['j'] = -'i';
  mul['1']['k'] = 'k';
  mul['i']['k'] = -'j';
  mul['j']['k'] = 'i';
  mul['k']['k'] = -'1';
  for (int id = 1; id <= t; ++id) {
    int l, x;
    scanf("%d%d", &l, &x);
    string tmp;
    cin >> tmp;
    str = "";
    for (int i = 0; i < x; ++i) {
      str += tmp;
    }
    len = l*x;
//    cout << str << endl;
    for (int i = 0; i < len; ++i) {
      dp[i][i+1] = str[i];
//      printf("%d ", dp[i][i+1]);
    }
//    printf("\n");
    for (int i = 0; i < len; ++i) {
      for (int j = i+2; j <= len; ++j) {
        dp[i][j] = multi(dp[i][j-1], str[j-1]);
//        printf("%d,%d,%d\n", i, j, dp[i][j-1]);
//        printf("%d,%d,%d\n", i, j, dp[i][j]);
      }
    }
//    printf("%d ", dp[0][3]);
//    printf("%d ", dp[3][6]);
//    printf("%d\n", dp[6][len]);
    int flag = false;
    if (check()) {
      printf("Case #%d: YES\n", id);
    }
    else {
      printf("Case #%d: NO\n", id);
    }

  }
  return 0;
}
