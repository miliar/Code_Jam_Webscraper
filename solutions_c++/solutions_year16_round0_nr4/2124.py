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

int main() {
	int T,cs;
  int K,C,S;
  int i;

	scanf("%d",&T);

	rab(cs,1,T) {
    scanf("%d %d %d",&K,&C,&S);

    printf("Case #%d:",cs);
    
    if (K == 1) {
      printf(" 1\n");
    } else {
      if (C == 1) {
        if (S < K) printf(" IMPOSSIBLE\n");
        else {
          rab(i,1,K) printf(" %d",i);
          printf("\n");
        }
      } else {
        if (2 * S < K) printf(" IMPOSSIBLE\n");

        long l = 2;
        long d = 1;

        for (i = 0; i < C - 1; i++) d *= K;

        for (i = 0; i < K; i += 2) {
          printf(" %ld",l);
          l +=  2* d;

          if (i + 2 == K - 1) l++;
          else l += 2;
        }
        printf("\n");
      }
    }
  }

  return 0;
} 
