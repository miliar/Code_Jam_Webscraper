#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <climits>
#include <limits.h>
#include <string>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <assert.h>
#include <cstring>
using namespace std;
#define rep(i, n) for (int (i) = 0, j123 = n; (i) < j123; (i) ++)
#define rep1(i, n) for (int (i) = 1, j123 = n; (i) <= j123; (i) ++)
#define db(x) {cout << #x << " = " << (x) << endl;}
#define dba(a, x, y) {cout << #a << " :";for(int i123=(x);i123<=(y);i123++) cout<<setw(4)<<(a)[i123];cout<<endl;}
#define clr(x) memset(x,0,sizeof(x));
#define mp make_pair
#define pb push_back
#define sz(x) int(x.size())
#define endl '\n'
typedef long long ll;
typedef long double ld;
const int INF = INT_MAX;
const ll INFL = LLONG_MAX;
const ld pi = acos(-1);
// const int MOD = ;
map<char, int> g;
vector<int> a;
int ff[5][5] = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};

int part;
int pp[10015];
int range[10015];
int range2[10015];
int L, x;

int findright(int a, int b) {
  for (int i = 1; i <= 4; i++) {
    if (ff[b][i] == a) return i;
  }
  return 0;
}

int getright(int a, int b) {
  int c = findright(a, b);
  if (c != 0) return c;
  return -findright(-a, b);
}

int getff(int a, int b) {
  int f = 1;
  if (a < 0) {
    a = -a;
    f = -f;
  }
  if (b < 0) {
    b = -b;
    f = -f;
  }
  return f * ff[a][b];
}

int init(int n) {
  range[0] = range2[n + 1] = 1;
  range[1] = a[1];
  rep1(i, n) {
    range[i] = getff(range[i - 1], a[i]);
  }
  for (int i = n; i >= 1; i--) {
    range2[i] = getff(a[i], range2[i + 1]);
  }
  part = range[n];
  pp[0] = 1;
  rep1(i, x) {
    pp[i] = getff(pp[i - 1], part);
  }
}

int calRange(int k1, int s, int k2, int t) {
  if (k1 == k2) {
    return getright(range[t], range[s - 1]);
    //int ans = 1;
    //for (int i = s; i <= t; i++) {
    //  ans = getff(ans, a[i]); 
    //}
    //return ans;
  }
  int r = getff(range2[s], pp[k2 - k1 - 1]);
  return getff(r, range[t]);
}

int main()
{
  ios_base::sync_with_stdio(0); cout.precision(15); cout << fixed; cout.tie(0);
  int T;
  string s;
  g['i'] = 2;
  g['j'] = 3;
  g['k'] = 4;
  cin >> T;
  rep1(cc, T) {
    cin >> L >> x;
    cin >> s;
    a.clear();
    a.pb(0);
    rep(i, s.length()) {
      a.pb(g[s[i]]);
    }
    init(L);
    //dba(range, 1, L);
    //rep1(i, L){
    //  cout << range[i] << " " << range[i - 1] << endl;
    //  cout << getright(range[i], range[i - 1]) << endl; 
    //}
    //cout << endl;
    int find = 0;
    for (int i = 1; i <= x; i++) { 
      for (int j = 1; j <= L; j++) {
        if (i == 1 && j == 1) continue;
        if (i == x && j == L) continue;
        for (int i2 = i; i2 <= x; i2++) {
          for (int j2 = 1; j2 <= L; j2++) {
            if (i2 == i && j2 <= j) continue;
            int a, b, c;
            if (j == 1) {
              a = calRange(1, 1, i - 1, L);
            } else {
              a = calRange(1, 1, i, j - 1);
            }
            if (a != 2) continue;
            if (j2 == 1) {
              b = calRange(i, j, i2 - 1, L);
            } else {
              b = calRange(i, j, i2, j2 - 1);
            }
            if (b != 3) continue;
            c = calRange(i2, j2, x, L);
            if (c == 4) {
              find = 1;
              break;
            }
          }
          if (find) break;
        }
        if (find) break;
      }
      if (find) break;
    }
    cout << "Case #" << cc << ": " << (find ? "YES": "NO") << endl;
  }
}
