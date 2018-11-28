#include <cassert>
#include <cstdio>

#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int main () {
  int tn;
  assert (scanf ("%d", &tn) == 1);
  for (int tt = 1; tt <= tn; tt++) {
    int n, d;
    assert (scanf ("%d%d", &n, &d) == 2);
    int s[n], m[n];
    int a_s, c_s, r_s;
    int a_m, c_m, r_m;
    assert (scanf ("%d%d%d%d", &s[0], &a_s, &c_s, &r_s) == 4);
    assert (scanf ("%d%d%d%d", &m[0], &a_m, &c_m, &r_m) == 4);
    for (int i = 1; i < n; i++) {
      s[i] = (s[i - 1] * a_s + c_s) % r_s;
      m[i] = (m[i - 1] * a_m + c_m) % r_m;
    }
    for (int i = 1; i < n; i++)
      m[i] %= i;
    // for (int i = 0; i < n; i++)
    //   fprintf (stderr, "[i=%d] s=%d m=%d\n", i, s[i], m[i]);
    int sm[n], sx[n];
    sm[0] = sx[0] = s[0];
    vector <pair <int, int> > ev;
    for (int i = 1; i < n; i++) {
      sm[i] = min (sm[m[i]], s[i]);
      sx[i] = max (sx[m[i]], s[i]);
      if (sx[i] - d <= sm[i]) {
        ev.push_back (make_pair (sx[i] - d, -1));
        ev.push_back (make_pair (sm[i], +1));
      }
      // fprintf (stderr, "# [i=%d]: (%d..%d)\n", i, sx[i] - d, sm[i]);
    }
    sort (ev.begin (), ev.end ());
    int r = 1, ans = 1;
    for (int i = 0; i < (int)ev.size (); i++) {
      r -= ev[i].second;
      if (ev[i].first <= s[0] && s[0] <= ev[i].first + d && r > ans)
        ans = r;
    }
    printf ("Case #%d: %d\n", tt, ans);
  }
  return 0;
}

