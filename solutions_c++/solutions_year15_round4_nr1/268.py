#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string.h>
#include <utility>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctype.h>
#include <sstream>
#include <map>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <sys/time.h>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long LL;

#define FOR(i,n) for(int i = 0;i < n;i++)
#define MP make_pair
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define PII pair<int, int>
#define PLL pair<long long, long long>
#define CLEAR(a) memset(a, 0, sizeof(a))
#define prev eruyvuy
#define INF 2000000007
#define next abc
#define y1 uu1
#define y2 uu2
const double EPS = 1E-12;
const double PI = acos(-1.0);

using namespace std;

int n,m,tc;
char a[105][105];

int lx, ly;
vector<PII> unsafe;
PII dr;

map<char, PII> gd;

void go(int x, int y, bool k) {
  if (x < 0 || y < 0 || x >= n || y >= m) {
    unsafe.push_back(MP(lx,ly));
    return;
  }
  if (a[x][y] != '.') {
    if (k)
      return;

    lx = x;
    ly = y;
    dr = gd[a[x][y]];
    k = 1;
  }
  go(x+dr.first, y+dr.second, k);
}

void solve() {
  FOR(i,105) FOR(j,105) a[i][j] = '.';
  unsafe.clear();
  cin >> n >> m;
  FOR(i,n)
  FOR(j,m)
  cin >> a[i][j];

  FOR(i, n)
  FOR(j, m) {
    if (a[i][j] != '.') {
      go(i, j, false);
    }
  }

  int bad = 0;
  FOR(i, unsafe.size()) {
    int cnt = 0;
    assert(a[unsafe[i].first][unsafe[i].second] != '.');
    FOR(j, m)
      if (a[unsafe[i].first][j] != '.') cnt++;
    FOR(j, n)
      if (a[j][unsafe[i].second] != '.') cnt++;
    assert(cnt >= 2);
    if (cnt == 2) {
      bad = 1;
    }
  }

  if (bad) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << unsafe.size() << endl;
  }
}

int main() {
  int t;
  cin >> t;

  gd['>'] = MP(0,1);
  gd['<'] = MP(0,-1);
  gd['^'] = MP(-1,0);
  gd['v'] = MP(1,0);

  FOR(tt,t) {
    tc = tt+1;
    cout << "Case #" << tt+1 << ": ";
    solve();
  }
  return 0;
}
