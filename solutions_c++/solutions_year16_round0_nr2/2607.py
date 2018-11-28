#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
using namespace std;
 
#define  rep(i,n)  for((i) = 0; (i) < (n); (i)++)
#define  rab(i,a,b)  for((i) = (a); (i) <= (b); (i)++)
#define all(v)    (v).begin(),(v).end()
#define  Fi(n)    rep(i,n)
#define  Fj(n)    rep(j,n)
#define  Fk(n)    rep(k,n)
#define  sz(v)    (v).size()

string pancackes;

int memo[1 << 12];

int reverse(int x,int i) {
  int r = 0;

  while (i > 0) {
    r = (r << 1) | (x & 1);
    x >>= 1;
    i--;
  }
  return r;
}

int state1 = 560;
int state2 = 572;

int min_flip(int state) {
  queue <int> q;

  memo[state] = 0;
  q.push(state);

  while (sz(q) > 0) {
    int s = q.front();
    //printf("s = %d\n", s);
    q.pop();

    int i, mask;

    for (i = 0, mask = 1; i < sz(pancackes); i++,(mask = (mask << 1) | 1)) {
      int n = reverse(~s & mask, i + 1) | (s & ~mask);
      if (memo[n] == -1) {
        memo[n] = memo[s] + 1;
        q.push(n);
      }
      //if (state == state1) printf("%d -> %d i = %d %x %x %x %x ==> %d\n", state, n, i, state, ~state, mask, ~mask, c);
    }

  }

  return memo[(1 << sz(pancackes)) - 1];
}

int main() {
	int T,cs;
  char s[1000];

	scanf("%d",&T);

	rab(cs,1,T) {
    scanf("%s",s);
    pancackes = s;
    memset(memo,-1,sizeof(memo));

    int st = 0;

    for (int i = sz(pancackes) - 1; i >= 0; i--) {
      st <<= 1;
      if (s[i] == '+') st |= 1;
    }

    printf("Case #%d: %d\n", cs, min_flip(st));
	}

} 
