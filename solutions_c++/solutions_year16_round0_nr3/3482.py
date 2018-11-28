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

int T, n, k;

LL calc(LL m, int b) {
  LL pw = 1, res = 0;
  for(int i = 0; i < n; ++i) {
    if(m & (1<<i))
      res += pw;
    pw *= b;
  }
  return res;
}

LL getDiv( LL x ) {
  for(LL i = 2; i * i <= x; ++i) {
    if(x % i == 0) {
      return max(i, x / i);
    }
  }
  return x;
}

vector<LL> v;

int main() {
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    scanf("%d%d", &n, &k);
    printf("Case #1:\n");
    for(LL m = 0; m < (1<<n) && k > 0; ++m) {
      if((m & 1) > 0 && (m & (1<<(n-1))) > 0) {
        bool ok = 1;
        v.clear();
        for(int i = 2; i <= 10; ++i) {
          LL num = calc(m, i);
          LL md = getDiv(num);
          if(md == num) {
            ok = 0;
            break;
          }
          v.pb(md);
        }
        if(ok) {
          k--;
          for(int i = n - 1; i >= 0; --i) {
            if(m & (1<<i))
              printf("1");
            else
              printf("0");
          }
          for(LL x : v) printf(" %lld", x);
          printf("\n");
        }
      }
    }
  return 0;
}
