#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define forab(i,a,b) for(int i = (a); i <= (int)(b); i++)
#define forn(i,n) for(int i = 0; i < (int)(n); i++)
// need declare it for vc, vc can not use <typeof> keyword
#define foreach(it,c) for(it = c.begin(); it != c.end(); ++it)

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define zero(a) memset(a, 0, sizeof(a))

#define pb push_back
#define mp make_pair

int t;

double PI = atan2(0.0, -1.0);

double area(int r) {
  return ((r+1)*(r+1) - (r)*(r));
}

int main() {
  //freopen("1.in", "r", stdin);
  //freopen("1.out", "w", stdout);

  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-small-attempt0.out", "w", stdout);

  //freopen("X-large.in", "r", stdin);
  //freopen("X-large.out", "w", stdout);


  cin >> t;
  for (int cc = 1; cc <= t; cc++) {
    LL r;
    LL m;
    cin >> r >> m;
    LL cnt = 0;
    while (m > 0) {
      double a = area(r);
      if (m - a >= 0) {
        cnt++;
      }
      m -= a;
      r += 2;
    }

    cout << "Case #" << cc << ": " << cnt << endl;
  }
  return 0;
}
