#include <stdio.h>
#include <assert.h>
#include <stack>
#include <queue>
#include <utility>
#include <algorithm>

#define MOD 1000002013
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define price(a,b) (N*(N+1)/2 - (N-(b-a))*(N-(b-a)+1)/2)

using namespace std;

long long int N, M;

typedef struct cards cards;
struct cards {
  long long int a;
  long long int b;
  long long int n;
};

long long int emp (stack<cards> &s, priority_queue< pair<long long int,long long int> > &t, long long int where) {
  long long int win = 0;
  while (!t.empty()) {
    pair<long long int,long long int> x = t.top();
    long long int stop = -x.first;
    if (stop > where) {
      break;
    }
    t.pop();
    long long int out = x.second;
    while (out > 0) {
      cards y = s.top();
      long long int pass = MIN(out, y.n);
      out -= pass;
      y.n -= pass;
      s.pop();
      if (y.n > 0) {
        s.push(y);
      }
      long long int lw = ((-price(y.a, stop) + price(y.a, y.b)) * pass) % MOD;
      //printf("(%lld, %lld: %lld) -> %lld: %lld\n", y.a, y.b, pass, stop, lw);
      win = (win + lw) % MOD;
    }
  }
  return win;
}

int main (void) {
  int T;
  int scanned = scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    stack<cards> s;
    long long int win = 0;
    priority_queue< pair<long long int,long long int> > t;
    priority_queue< pair<long long int,pair<long long int,long long int> > > v;
    scanf("%lld%lld", &N, &M);
    for (long long int i = 0; i < M; i++) {
      long long int a, b, n;
      scanf("%lld%lld%lld", &a, &b, &n);
      v.push(make_pair(-a,make_pair(b,n)));
    }
    long long int prev = -1;
    for (long long int i = 0; i < M; i++) {
      pair<long long int,pair<long long int,long long int> > x = v.top();
      v.pop();
      cards c;
      c.a = -x.first;
      c.b = x.second.first;
      c.n = x.second.second;
      //printf("%lld %lld %lld\n", c.a, c.b, c.n);
      if (prev != c.a) {
        win = (win + emp(s,t,c.a-1)) % MOD;
      }
      if (c.a < c.b) {
        s.push(c);
        t.push(make_pair(-c.b,c.n));
      }
      prev = c.a;
      //win = (win + emp(s,t,c.a)) % MOD;
    }
    win = (win + emp(s,t,N)) % MOD;
    printf("Case #%d: %lld\n", currentcase, win);
  }
  return 0;
}
