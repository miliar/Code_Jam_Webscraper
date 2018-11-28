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

int main(void) {
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    char buff[1234];
    int n; scanf("%d %s", &n, buff);

    int ans = 0;
    int stand = 0;
    for (int i = 0; i <= n; ++i) {
      int k = buff[i] - '0';
      if (k == 0) continue;
      if (stand < i) {
        ans += i-stand;
        stand = i;
      }
      stand += k;
    }      
    
    printf("Case #%d: %d\n", tc+1, ans);
    fflush(stdout);
  }
  return 0;
}   
