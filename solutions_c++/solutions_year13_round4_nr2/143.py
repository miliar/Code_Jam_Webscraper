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

int main (void) {
  int tn, nt;
  scanf ("%d", &nt);
  for (tn = 1; tn <= nt; tn++) {
    printf ("Case #%d: ", tn);
    fprintf (stderr, "Case #%d: \n", tn);

    long long p, N;
    cin >> N >> p;
    if (p == (1ll << N)) {
      cout << p - 1 << " " << p - 1 << endl;
    } else {
      long long cur = 0;
      long long ans = 0;
      for (long long i = 0; i < N; i++) {
        cur += 1ll << (N - 1 - i);
        ans += (1ll << i);
        if (p <= cur) {
          cout << ans - 1 << " ";
          break;
        }
      }

      cur = 0;
      ans = 0;
      for (long long i = 0; i < N; i++) {
        cur += 1ll << i;
        if (p <= cur) {
          cout << ans << endl;
          break;
        }
        ans += (1ll << (N - i - 1));
      }
    }

  }

  return 0;
}
