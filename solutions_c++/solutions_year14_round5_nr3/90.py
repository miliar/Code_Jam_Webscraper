/* 
  2014.03.26 15:10
  http://codeforces.ru/gym/100289/
*/


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <cmath>
#include <string> 
#include <ctime>

using namespace std;

// #undef Fdg_Home

int st[2002];
char t[1002];
int id[1002];

bool dp[16][1<<16][16][16];

int what[2002];

void solveTest(int CS) {
  printf("Case #%d: ", CS);
  for (int i = 0; i <= 2000; ++i)
    st[i] = 2;
  int n;
  scanf("%d\n", &n);
  memset(what, -1, sizeof(what));
  int ind = 0;
  for (int i = 0; i < n; ++i) {
    scanf("%c %d\n", &t[i], &id[i]);
    if (id[i] != 0) {
      if (what[id[i]] == -1)
        what[id[i]] = ind++;
    }
  }
  memset(dp, 0, sizeof(dp));
  for (int mask = 0; mask < (1<<n); ++mask) {
    dp[0][mask][0][0] = true;
  }
  for (int i = 0; i < n; ++i)
    for (int mask = 0; mask < (1<<n); ++mask)
      for (int in = 0; in <= 0; ++in)
        for (int out = 0; in + out <= 0; ++out)
          if (dp[i][mask][in][out]) {
            int ind = what[id[i]];
            if (t[i] == 'E') {
              if (id[i] == 0) {
                // if (out)
                //   dp[i + 1][mask][in][out - 1] = true;
                // dp[i + 1][mask][in + 1][out] = true;
                for (int j = 0; j < n; ++j) {
                  if (mask & (1<<j));
                  else
                    dp[i + 1][mask | (1<<j)][in][out] = true;
                }
              } else {
                if (mask & (1<<ind)) {
                  if (out)
                    dp[i + 1][mask][in][out - 1] = true;
                } else {
                  dp[i + 1][mask | (1<<ind)][in][out] = true;
                }
              }
            }

            if (t[i] == 'L') {
              if (id[i] == 0) {
                // if (in)
                //   dp[i + 1][mask][in - 1][out] = true;
                // dp[i + 1][mask][in][out + 1] = true;
                for (int j = 0; j < n; ++j) {
                  if (mask & (1<<j))
                    dp[i + 1][mask - (1<<j)][in][out] = true;
                }
              } else {
                if (mask & (1<<ind)) {
                  dp[i + 1][mask - (1<<ind)][in][out] = true;
                } else {
                  if (in)
                    dp[i + 1][mask][in - 1][out] = true;
                }
              }
            }
          }

  int ans = 55;
  for (int mask = 0; mask < (1<<n); ++mask)
    for (int in = 0; in <= n; ++in)
      for (int out = 0; in + out <= n; ++out)
        if (dp[n][mask][in][out]) {
          int cur = in;
          for (int i = 0; i < n; ++i)
            if (mask & (1<<i)) ++cur;
          ans = min(ans, cur);
        }
  if (ans == 55) puts("CRIME TIME");
  else printf("%d\n", ans);
}

void solveTest2(int CS) {
  printf("Case #%d: ", CS);
  for (int i = 0; i <= 2000; ++i)
    st[i] = 2;
  int n;
  scanf("%d\n", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%c %d\n", &t[i], &id[i]);
  }
  int in0 = 0, out0 = 0, ok = 1;
  for (int i = 0; i < n; ++i) {
    if (t[i] == 'E') {
      if (id[i] == 0) ++in0;
      else {
        if (st[id[i]] == 1) {
          if (out0 == 0)
            ok = false;
          else out0--;
        }
        st[id[i]] = 1;
      }
    }
    if (t[i] == 'L') {
      if (id[i] == 0) ++out0;
      else {
        if (st[id[i]] == 0) {
          if (in0 == 0)
            ok = false;
          else in0--;
        }
        st[id[i]] = 0;
      }
    }
  }
  if (!ok) puts("CRIME TIME");
  else {
    for (int i = 1; i <= 2000; ++i)
      if (st[i] == 1) ++in0;
    int ans = in0;
    for (int mask = 0; mask < (1<<n); ++mask) {
      for (int i = 0; i <= 2000; ++i)
        st[i] = 2;
      ok = 1;
      in0 = 0; out0 = 0;
      for (int i = 0; i < n; ++i) {
        if (t[i] == 'E') {
          if (id[i] == 0) {
            if (mask & (1<<i)) ++in0;
            else {
              out0--;
              if (out0 < 0) ok = 0;
            }
          }
          else {
            if (st[id[i]] == 1) {
              if (out0 == 0)
                ok = false;
              else out0--;
            }
            if (st[id[i]] == 2) {
              if (mask & (1<<i));
              else {
                in0--; out0--;
                if (out0 < 0 || in0 < 0) ok = 0;
              }
            }
            if (st[id[i]] == 0) {
              if (mask & (1<<i));
              else {
                in0--; out0--;
                if (in0 < 0 || out0 < 0) ok = 0;
              }
            }
            st[id[i]] = 1;
          }
        }
        if (t[i] == 'L') {
          if (id[i] == 0) {
            if (mask & (1<<i)) ++out0;
            else {
              in0--;
              if (in0 < 0) ok = 0;
            }
          }
          else {
            if (st[id[i]] == 0) {
              if (in0 == 0)
                ok = false;
              else in0--;
            }
            if (st[id[i]] == 2) {
              if (mask & (1<<i));
              else {
                in0--;
                if (in0 < 0) ok = 0;
              }
            }
            if (st[id[i]] == 1) {
              if (mask & (1<<i));
              else {
                in0--; out0--;
                if (in0 < 0 || out0 < 0) ok = 0;
              }
            }
            st[id[i]] = 0;
          }
        }
      }
      if (ok) {
        // cout << in0 << endl;
        int cur = in0;
        for (int i = 1; i <= 2000; ++i) {
          if (st[i] == 1) cur++;
        }
        ans = min(ans, cur);
      }
    }
    printf("%d\n", ans);
  }
}

int main() {
// #ifndef Fdg_Home
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
// #endif
  int T;
  scanf("%d\n", &T);
  for (int test = 1; test <= T; ++test) {
    solveTest(test);
  }
  return 0;
}