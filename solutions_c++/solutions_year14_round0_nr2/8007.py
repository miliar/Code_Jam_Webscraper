#include<cstdio>
#include<iostream>

using namespace std;
#define f(i, a, n) for(int i = a; i < n; i++)
typedef long double ld;

ld solve(){
  ld C, F, X;
  cin >> C >> F >> X;

  ld t = 0;
  ld best = 1e30;
  f(cookies, 0, 1000000) {
    ld partial = t + X / (2.0 + F * cookies);
    best = min(best, partial);
    t += C / (2.0 + F * (cookies));
  }
  return best;
}

int main(){
  int t; cin >> t;
  for(int tt = 1; tt <= t; tt++) {
    printf("Case #%d: %.07f\n", tt, (double)solve());
  }
}
