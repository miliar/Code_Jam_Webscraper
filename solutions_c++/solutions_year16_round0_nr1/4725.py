#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <queue>

using namespace std;

#define TRACE(x) cerr << #x << " " << x << endl
#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define _ << " " <<

#define fst first
#define snd second

typedef long long llint;
typedef pair<int, int> pii;

const int B = 27397, MOD = 1e9 + 7;
const int B1 = 33941, MOD1 = 1e9 + 9;

int T; 

void update_mask(llint x, int *mask) {
  while (x > 0) {
    *mask |= (1 << (x % 10));
    x /= 10;
  }
}

void solve(int t) {

  printf("Case #%d: ", t);

  int mask = 0;
  llint n = 0, _n;

  scanf("%lld", &_n); 

  if (_n == 0) {
    printf("INSOMNIA\n");
    return;
  }

  int cnt = 0;
  do {
    n += _n;
    update_mask(n, &mask); 
  } while (mask != 1023 && cnt < 100000);

  if (cnt == 100000) 
    printf("INSOMNIA\n");
  else
    printf("%lld\n", n);

}

int main(void) {

  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
    solve(t + 1);

  return 0;

}

