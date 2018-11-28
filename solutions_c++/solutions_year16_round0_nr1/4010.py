#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define all(x) x.begin(),x.end()
#define sz(x) (int)(x.size())
#define LL long long
#define mp make_pair
#define pb push_back
#define f first
#define s second

using namespace std;

const int N = 1e5 + 7;
const int mod = 1e9 + 7;

int n, T, ans;

int main() {
//  #ifndef ONLINE_JUDGE
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
//  #endif
    scanf("%d", &T);
    for(int it = 1; it <= T; ++it) {
      scanf("%d", &n);
      ans = -1;
      vector<int> was(10, 0);
      int cnt = 0;
      for(int i = 1; i <= 1000000; ++i) {
        LL p = i * 1ll * n;
        while(p > 0) {
          if(!was[p % 10])
            cnt++;
          was[p % 10]++;
          p /= 10;
        }
        if(cnt == 10) {
          ans = i;
          break;
        }
      }
      printf("Case #%d: ", it);
      if(ans == -1)
        printf("INSOMNIA\n");
      else
        printf("%lld\n", ans * 1ll * n);
    }
  return 0;
}
