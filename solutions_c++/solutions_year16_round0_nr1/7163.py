#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int inf = 2e9;
const int mod = 1e9 + 7;
const int MAXN = 3e5;
const int N = 5e5 + 11;

int main(){
  #if __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #else
    // freopen("typing.in", "r", stdin);
    // freopen("typing.out", "w", stdout);
  #endif
  int t;
  scanf("%d", &t);
  int r = 0;
  while (t--){
    ++r;
    ll n;
    scanf("%lld", &n);
    bool f = false;
    int mask = 0;
    for (int i = 1; i <= 1e7 + 11 && !f; i++){
      ll q = n * (ll) i;
      if (!q) mask |= 1;
      while (q){
        mask |= (1 << (q % 10));
        q /= 10ll;
      }
      if (mask == 1023){
        f = true;
        printf("Case #");
        printf("%d", r);
        printf(": ");
        printf("%lld\n", n * (ll) i);
      }
    }
    if (!f) {
      printf("Case #");
      printf("%d", r);
      printf(": ");
      puts("INSOMNIA");
    }
  }
  return 0;
}







