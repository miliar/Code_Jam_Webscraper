#include <cassert>
#include <cstring>

#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAXVAL = 1234;

int main(void) {
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    int n; scanf("%d", &n);
    static int orig_frek[MAXVAL]; REP(i, MAXVAL) orig_frek[i] = 0;
    REP(i, n) {
      int x; scanf("%d", &x);
      ++orig_frek[x];
    }

    int ans = MAXVAL;
    REP(mic, MAXVAL) {
      int lo = 1, hi = 1000;

      while (lo < hi) {
        int mid = (lo + hi) / 2;
        int left = mic;

        static int frek[MAXVAL]; REP(i, MAXVAL) frek[i] = orig_frek[i];
        for (int i = 1000; i > mid; --i) {
          left -= frek[i];
          frek[i-mid] += frek[i];
        }

        if (left < 0)
          lo = mid + 1;
        else
          hi = mid;
      }

      ans = min(ans, mic + lo);
    }

    printf("Case #%d: %d\n", tc+1, ans); fflush(stdout);
  }
  return 0;
}   
