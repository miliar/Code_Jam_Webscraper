#include <bits/stdc++.h>

using namespace std;

#ifdef ACMTUYO
struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#else
struct RTC{};
#define DBG(X)
#endif

#define fast_io() ios_base::sync_with_stdio(false)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long int number;
bool vis[10];
number maxcnt = 0;
number solve(number n) {
  memset(vis, false, sizeof(vis));
  int to_visit = 10;
  number cur = 0;
  number cnt = 0;
  while (to_visit > 0) {
    cnt++;
    cur += n;
    int c = cur;
    while (c > 0) {
      int digit = c % 10LL;
      c /= 10LL;
      if (!vis[digit]) {
        vis[digit]++;
        to_visit--;
      }
    }
  }
  maxcnt = max(maxcnt, cnt);
  return cur;
}
int main() {
  int casos;
  scanf("%d", &casos);
  for (int caso = 1; caso <= casos; caso++) {
    DBG(caso);
    int n;
    scanf("%d", &n);
    printf("Case #%d: ", caso);
    if (n == 0)
      printf("INSOMNIA\n");
    else
      printf("%lld\n", solve(n));
  }
  DBG(maxcnt);
  return 0;
}

