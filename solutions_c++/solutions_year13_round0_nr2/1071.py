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
#define N 102
int lawn[N][N];

bool valid(int n, int m, int a, int b) {
  bool ret = true;
  forn (i, m) {
    if (lawn[a][i] > lawn[a][b]) {
      ret = false;
      break;
    }
  }
  bool ret2 = true;
  forn (i, n) {
    if (lawn[i][b] > lawn[a][b]) {
      ret2 = false;
      break;
    }
  }
  //cout << a << " " << b << " " << ret << " " << ret2 << endl;
  if (!ret && !ret2)
    return false;
  return true;
}

int main() {
  //freopen("1.in", "r", stdin);
  //freopen("1.out", "w", stdout);

  //freopen("B-small-attempt1.in", "r", stdin);
  //freopen("B-small-attempt1.out", "w", stdout);

  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);

  cin >> t;
  for (int cc = 1; cc <= t; cc++) {
    int n, m, x;
    cin >> n >> m;
    forn(i, n) {
      forn(j, m) {
        cin >> x;
        lawn[i][j] = x;
      }
    }
    bool is_valid = true;
    forn(i, n) {
      forn(j, m) {
        if (!valid(n, m, i, j))
          is_valid = false;
      }
    }
    cout << "Case #" << cc << ": ";
    if (is_valid)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}
