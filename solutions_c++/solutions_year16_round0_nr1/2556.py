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

long last[1000001];

int main() {
  int i;

  last[0] = -1;

  rab(i,1,1000000) {
    long l = 0;
    set<int> s;

    while (s.size() < 10) {
      l += i;
      long k = l;

      while (k > 0) {
        s.insert(k % 10);
        k /= 10;
      }
    }

    //if (i % 1000 == 0) printf("--- %d", i);
    last[i] = l;
  }

  int T,cs;
  int N;

  scanf("%d",&T);

  rab(cs,1,T) {
    scanf("%d",&N);

    if (N == 0) printf("Case #%d: INSOMNIA\n", cs);
    else printf("Case #%d: %ld\n", cs, last[N]);
  }

  return 0;
} 

