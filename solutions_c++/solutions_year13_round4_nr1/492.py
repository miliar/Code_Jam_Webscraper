#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;
#define MOD 1000002013
vector <pair <int, int> > en;

long long n;

int main () {
  int tc;
  scanf ("%d", &tc);
  for (int tn = 1; tn <= tc; tn++) {
    int m;
    scanf ("%lld %d", &n, &m);
    int cc = 0;
    en.resize (0);
    for (int j = 0; j < m; j++) {
      int o, e, p;
      scanf ("%d%d%d", &o, &e, &p);
      long long del = e - o;
      long long val = (n * (n + 1) / 2 - del * (del + 1) / 2) % MOD;
      cc += (val * p) % MOD;
      en.push_back (make_pair (o, -p));
      en.push_back (make_pair (e, p));
    }
    sort (en.begin (), en.end ());
    for (int i = 0; i < (int)en.size (); i++) {
      if (en[i].second >= 0) continue;
      long long delta = 0, mx = -(long long)1e18;
      int j;

      for (j = i; j < (int)en.size (); j++) {
	delta += en[j].second;
	if (!delta) break;
	if (delta > mx) mx = delta;
      }
      mx = -mx;
      assert (mx > 0);
      assert (-en[i].second >= mx && en[j].second >= mx);
      long long del = en[j].first - en[i].first;
      long long val = (n * (n + 1) / 2 - del * (del + 1) / 2) % MOD;
      cc -= (val * mx) % MOD;
      if (cc < 0) cc += MOD;
      en[i].second += mx;
      en[j].second -= mx;
      --i;
    }
    
    printf ("Case #%d: %d\n", tn, cc);
  }
  return 0;
}
