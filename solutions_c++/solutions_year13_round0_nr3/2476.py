#include "stdio.h"
#include "string.h"
#include <vector>
#include <algorithm>
using namespace std;
#define ll long long
#define MAX 100000000
#define TEST
vector<ll> A;
ll reverse (ll n) {
  ll m=0;
  while(n>0) {
    ll d = n%10;
    m = m*10 + d;
    n = n/10;
  }
  return m;
}
bool isPalin(ll n) {
  return ((n - reverse(n)) == 0);
}
void init() {
  for(ll i=1; i< MAX; i++) {
    //printf("%lld --> %lld\n", i, i*i);
    if (isPalin(i) && isPalin(i*i)) {
#ifdef DATA
      A.push_back(i);
#endif
#ifdef TEST
      A.push_back(i*i);
#endif
    }
  }
}

int main() {
  init();
#ifdef DATA
  for (ll i =0 ; i<A.size(); i++)
    printf("%lld --> %lld\n", A[i], A[i]*A[i]);
#endif
#ifdef TEST
  ll t;
  scanf("%lld", &t);
  for(ll x=1; x<=t; x++) {
    ll a, b;
    scanf("%lld %lld", &a, &b);
    ll acount = lower_bound(A.begin(), A.end(), a) - A.begin();
    ll bcount = lower_bound(A.begin(), A.end(), b+1) - A.begin();
    ll ans = bcount - acount;
    printf("Case #%lld: %lld\n", x,ans);
  }
#endif
}