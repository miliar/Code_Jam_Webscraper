
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <string>
#include <sstream>
#include <iomanip>
#include <iostream>

using namespace std;

#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)

#ifdef WIN32  
#define LLD "%I64d"
#else 
#define LLD "%Ld"
#endif

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...)
#endif

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int inf = (int) 1e9;
const int maxn = (int) 1e5 + 1;
const double eps = (double) 1e-8;

int main() {

  int t;  
  scanf("%d", &t);
  for (int test = 1; test <= t; test++) {
    int n;
    scanf("%d", &n);
    vector<pair<char, int> > a[n];
    for (int i = 0; i < n; i++) { 
      string s;
      cin >> s;
      for (int j = 0; j < s.size();) {
        int jj = j;
        while (j + 1 < s.size() && s[jj] == s[j + 1])
          j++;
        a[i].pb(mp(s[jj], j - jj + 1));
        j++;
      }
    }
    int nn = a[0].size();
    int ans[nn];
    memset(ans, 0, sizeof ans);
    bool f = true;
    for (int i = 0; i < n; i++) {
      if (a[i].size() != nn) {
        f = false;
        break;
      }
      for (int j = 0; j < nn; j++) {
        if (a[i][j].X != a[0][j].X) {
          f = false;
          break;
        }
        ans[j] += a[i][j].Y;
      }
    }
    if (!f) {
      printf("Case #%d: Fegla Won\n", test);
      continue;
    }
    int anss = 0;
    for (int i = 0; i < nn; i++) { 
      int s = ans[i] / n;
      //eprintf("%d\n", s);
      for (int j = 0; j < n; j++) {
        //eprintf("%c %d\n", a[j][i].X, a[j][i].Y);
        anss += abs(a[j][i].Y - s);
      }
    }
    printf("Case #%d: %d\n", test, anss);   
  }
  return 0;
}
