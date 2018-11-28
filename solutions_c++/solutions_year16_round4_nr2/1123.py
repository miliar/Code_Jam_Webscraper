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

double prob[20];
int N, K;

int main() {
	int T,cs;
  int i,j;
  int p,q;

	scanf("%d",&T);

	rab(cs,1,T) {
    scanf("%d %d",&N, &K);

    Fi(N) scanf("%lf",&prob[i]);

    double mx = 0.0;

    Fi(1 << N) {
      vector <double> f;

      Fj(N) {
        if (i & (1 << j)) f.push_back(prob[j]);
      }

      if (sz(f) != K) continue;

      double memo[20][20];

      rep(q,K) memo[K][q] = 0.0;
      memo[K][0] = 1.0;

      for (p = K - 1; p >= 0; p--) {
        for (q = 0; q <= K; q++) memo[p][q] = 0.0;
        for (q = 0; q <= K; q++) {
          memo[p][q] += (1 - f[p]) * memo[p + 1][q];
          memo[p][q + 1] += f[p] * memo[p + 1][q];
        }
      }

      double tie = memo[0][K / 2];

      if (tie > mx) mx = tie;
    }

    printf("Case #%d: %.7lf\n", cs, mx);
	}

  return 0;
} 
