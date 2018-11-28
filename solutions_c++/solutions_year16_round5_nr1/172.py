#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 20020;

char a[MAX];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    scanf("%s", a);
    int n = strlen(a);
    REP(i, n) a[i] = a[i] == 'C';
    
    int ans = 0, cnt = 0, last = 0;
    REP(i, n) {
      if (cnt > 0 && (last == a[i] || cnt+1 > n-i-1)) {
        cnt--;
        ans += (last == a[i] ? 10 : 5);
        last ^= 1;
      } else {
        cnt++;
        last = a[i];
      }
    }
    
    printf("Case #%d: ", tp);
    printf("%d\n", ans);
  }
  return 0;
}
