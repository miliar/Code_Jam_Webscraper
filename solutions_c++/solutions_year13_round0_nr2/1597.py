/* 
 * Author: Hakobyan Tigran
 */

#pragma comment(linker, "/STACK:60777216") 
#define printTime(begin, end) printf("%.3lf\n", (double)(end - begin) / (double)CLOCKS_PER_SEC) 


#include <string.h>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <functional>
#include <complex>
#include <iostream>
#include <fstream>
#include <sstream>
#include <bitset>
#include <limits>
#include <ctime>
#include <cassert>
#include <valarray>

using namespace std;

#define IN(a) freopen(a, "r", stdin)
#define OUT(a) freopen(a, "w", stdout)

#define mp(a, b) make_pair(a, b)
#define det(a, b, c, d) (a * d - c * b)
#define sbstr(s, i, j) s.substr(i, j - i + 1)

#define clear(dp) memset(dp, -1, sizeof(dp))
#define reset(arr) memset(arr, 0, sizeof(arr))

#define EPS 1e-9
#define PI acos(-1.0)
#define MOD 1000000007
#define IINF 1000000000
#define LINF 6000000000000000000LL

const int MAXN = 100 + 7;

int n, m;
int orig = 100;
int test_id = 0;
int curr[MAXN][MAXN];
int desired[MAXN][MAXN];

class Comparator {
public:
  bool operator () (const pair < int, int > &ind1, const pair < int, int > &ind2) {
    return desired[ind1.first][ind1.second] < desired[ind2.first][ind2.second];
  }
};

void init () {
    scanf("%d%d", &n, &m);
    for(int i = 0; i < n; ++i) {
      for(int j = 0; j < m; ++j) {
        curr[i][j] = orig;
        scanf("%d", desired[i] + j);
      }
    }
}

void solve () {
  priority_queue < pair < int, int > , vector < pair < int, int > >, Comparator > Q;
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < m; ++j) {
      Q.push(mp(i, j));
    }
  }
  while(!Q.empty()) {
    pair < int, int > p = Q.top();
    Q.pop();
    int i = p.first;
    int j = p.second;
    bool can_cut = true;
    int height = desired[i][j];
    for(int k = 0; k < n; ++k) {
      if(desired[k][j] > height) {
        can_cut = false;
        break;
      }
    }
    if(can_cut) {
      for(int k = 0; k < n; ++k) {
        curr[k][j] = height;
      }
    }
    else {
      can_cut = true;
      for(int k = 0; k < m; ++k) {
        if(desired[i][k] > height) {
          can_cut = false;
          break;
        }
      }
      if(can_cut) {
        for(int k = 0; k < m; ++k) {
          curr[i][k] = height;
        }
      }
    }
  }
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < m; ++j) {
      if(curr[i][j] != desired[i][j]) {
        printf("Case #%d: NO\n", ++test_id);
        return ;
      }
    }
  }
  printf("Case #%d: YES\n", ++test_id);
}

int main () {
#ifndef ONLINE_JUDGE
  IN("/home/tigran/Desktop/Debug/input.txt");
  OUT("/home/tigran/Desktop/Debug/output.txt");
#endif
  int test_case;
  scanf("%d", &test_case);
  while(test_case--) {
    init();
    solve();
  }
  return 0;
}
