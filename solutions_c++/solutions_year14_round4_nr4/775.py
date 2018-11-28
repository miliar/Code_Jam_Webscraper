#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <climits>
#include <algorithm>
#include <complex>
#include <cmath>
#include <cstdlib>
using namespace std;

#define pb push_back 
#define mp make_pair 
#define repn(i, n) for(int i = 0; i < (n); i++)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mii;
typedef vector<vi> vvi;
typedef map<int, mii> mimii;
typedef map<int, si> misi;
typedef map<int, pii> mipii;
typedef vector<pii> vpii;
typedef map<int, vi> mivi;
typedef vector<string> vs;
typedef set<string> ss;
typedef vector<ss> vss;

int n, m;
vs xs;
vss ys;
mii cs;

void foo(vi &ps) {
  vss zs;
  for (int i = 0; i < n; i++)
    zs.pb(ss());
  for (int i = 0; i < m; i++)
    zs[ps[i]].insert(ys[i].begin(), ys[i].end());
  /*
  for (int i = 0; i < m; i++)
    printf(" %d", ps[i]);
  printf(":");
  for (int i = 0; i < n; i++)
    printf(" %d", zs[i].size());
  printf("\n");
  */
  int c = 0;
  for (int i = 0; i < n; i++)
    c += zs[i].size();
  cs[-c] += 1;
  cs[-c] %= 1000000007;
}

void asdf(vi &ps, int j) {
  if (j == m) foo(ps);
  else
  for (int k = 0; k < n; k++) {
    ps[j] = k;
    asdf(ps, j + 1);
  }
}

int main(int argc, char **argv) {
  int tc;
  cin >> tc;
  repn(ti, tc) {
    xs.clear();
    ys.clear();
    cs.clear();
    cin >> m >> n;
    for (int i = 0; i < m; i++)
    {
      string t;
      cin >> t;
      xs.pb(t);
    }

    for (int i = 0; i < m; i++)
    {
      ys.pb(ss());
      for (int k = 0; k <= xs[i].size(); k++)
        ys[i].insert(xs[i].substr(0, k));
    }

    vi ps;
    for (int i = 0; i < m; i++)
      ps.pb(-1);
    asdf(ps, 0);
    auto it = cs.begin();

    printf("Case #%d: %d %d\n", ti + 1, -it->first, it->second);
  }
  return 0;
}
