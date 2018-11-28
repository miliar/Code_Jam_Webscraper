#include <cstdio>
#include <cassert>
#include <algorithm>

using namespace std;

const int maxN = 1000;
const int mod = 1000002013;

int n, k;
pair <int, int> a[maxN];
int x[maxN];
pair <int, int> b[maxN];
int s[maxN], sx[maxN], sp;

int getSum (int i, int j) {
  int d = j - i;
  return (int)(((long long)(n + (n - d + 1)) * d / 2) % (long long)mod);
}

int main () {
  int nt;
  assert (scanf ("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; ++tt) {
    assert (scanf ("%d%d", &n, &k) == 2);
    for (int i = 0; i < k; ++i) {
      assert (scanf ("%d%d%d", &a[i].first, &a[i].second, &x[i]) == 3);
    }
    int was = 0;
    for (int i = 0; i < k; ++i) {
      was = (was + (long long)x[i] * getSum (a[i].first, a[i].second)) % mod;
    }
    for (int i = 0; i < k; ++i) {
      b[i].first = a[i].first;
      b[i].second = -x[i];
      b[i + k].first = a[i].second;
      b[i + k].second = x[i];
    }
    sort (b, b + (2 * k));
    sp = 0;
    int have = 0;
    for (int i = 0; i < 2 * k; ++i) {
      if (b[i].second < 0) {
        s[sp] = b[i].first;
        sx[sp] = -b[i].second;
        ++sp;
      } else {
        while (b[i].second > 0) {
          int cnt = min (b[i].second, sx[sp - 1]);
//          fprintf (stderr, "%d pass from %d to %d\n", cnt, s[sp - 1], b[i].first);
          have = (have + (long long)cnt * getSum (s[sp - 1], b[i].first)) % mod;
          b[i].second -= cnt;
          sx[sp - 1] -= cnt;
          if (sx[sp - 1] == 0) {
            --sp;
          }
        }
      }
    }
    printf ("Case #%d: %d\n", tt, (was - have));
  }
  return 0;
}
/*
1   5 = n + n-1 + n-2 + n-3
  3   7 = n + n-1 + n-2 + n-3
     6   9 = n + n-1 + n-2

1        9 = n + n-1 + n-2 + n-3 + n-4 + n-5 + n-6 + n-7
  3 5 = 
     67
*/
