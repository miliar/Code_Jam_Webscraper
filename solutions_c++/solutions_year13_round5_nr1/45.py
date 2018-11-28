#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <utility>

using namespace std;


long long a[37];
long long c[37];


int main (void) {
  int tn, nt;
  scanf ("%d", &nt);
  for (tn = 1; tn <= nt; tn++) {
    printf ("Case #%d: ", tn);
    fprintf (stderr, "Case #%d: \n", tn);

    long long b;
    cin >> b;
    int n;
    scanf ("%d", &n);
    memset (a, 0, sizeof (a));
    memset (c, 0, sizeof (c));
    vector <long long> aa;
    for (int i = 0; i < n; i++) {
      cin >> a[i];
      aa.push_back (a[i]);
      aa.push_back (a[i] + 1);
      aa.push_back (a[i] + 2);
      aa.push_back (a[i] - 1);
      if (a[i] >= 2)
        aa.push_back (a[i] - 2);
    }
    aa.push_back (0);
    aa.push_back (2000000000000ll);

    long long l = 0, r = 2000000000000ll;
    while (l + 1 < r) {
      long long m = (l + r) / 2;
      long long cnt = (37 - n) * m;
      for (int i = 0; i < n; i++) {
        if (a[i] < m) {
          cnt += m - a[i];
        }
      }
      if (cnt > b) {
        r = m;
      } else {
        l = m;
      }
    }
    if (l > 1)
      aa.push_back (l - 2);
    if (l > 0)
      aa.push_back (l - 1);
    aa.push_back (l);
    aa.push_back (l + 1);
    aa.push_back (l + 2);

    sort (a, a + 37);
    sort (aa.begin(), aa.end());
    aa.resize (unique (aa.begin(), aa.end()) - aa.begin());

    double ans = 0.0;
    long long real_b = b;

    for (int jj = 0; jj < (int)aa.size() && b > 0; jj++) {
      long long j = aa[jj]; 
      for (int ii = 36; ii >= 0 && b > 0; ii--) {
        if (a[ii] + c[ii] < j - 1) {
          b -= j - 1 - a[ii] - c[ii];
          c[ii] = j - 1 - a[ii];
        }
      }

      for (int ii = 36; ii >= 0 && b > 0; ii--) {
        if (a[ii] + c[ii] < j) {
          c[ii]++;
          b--;

          int mi = 0;
          for (int i = 0; i < 37; i++) {
//            cerr << a[i] + c[i] << " ";
            if (a[i] + c[i] < a[mi] + c[mi]) {
              mi = i;
            }
          }
          long long res = 0, cnt = 0;
          for (int i = 0; i < 37; i++) {
            if (a[i] + c[i] == a[mi] + c[mi]) {
              res += c[i];
              cnt++;
            }
          }
          double win = res * 36.0 / cnt - real_b + b;
//          cerr << win << endl;
          if (win > ans) {
            ans = win;
          }
        }
      }
    }
    assert (b <= 0);
    printf ("%.10lf\n", ans);
  }

  return 0;
}
