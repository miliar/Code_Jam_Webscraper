#include <bits/stdc++.h>

#define DEBUG

#ifdef DEBUG
#define DBG(...) printf(__VA_ARGS__)
#else
#define DBG(...)
#endif

using namespace std;

typedef long long ll;


int main() {
  ll T;
  scanf("%lld", &T);
  
  for (ll t=1; t<=T; t++)
  {
    ll N;
    scanf("%lld", &N);

    if (N == 0) { printf("Case #%lld: INSOMNIA\n", t); continue; }

    vector<bool> occs(10, false);
    ll C = 0;
    for (ll q=1; q<=100000; q++)
    {
      ll nn = N*q;
      ll num = nn;
      while (num != 0) 
      { 
        if (occs[num%10] == 0) 
        {
          occs[num%10] = 1;
          C++;
          if (C == 10) { printf("Case #%lld: %lld\n", t, nn); goto next_test_case; }
        }
        num /= 10;
      } 
    }
    next_test_case: ;
  }
  return 0;
}

