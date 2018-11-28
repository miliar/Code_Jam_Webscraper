#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <complex>
#include <string>
#include <stdint.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define rep(i,m,n) for(int i = m; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
typedef complex<decimal> P;

const decimal EPS = 1e-8;

const int MOD = 1000000007;

int main(){
  int T;
  cin >> T;
  REP(i, T){
    int N;
    cin >> N;
    int a[N];
    memset(a, 0, sizeof(int) * N);
    REP(j, N) REP(k, N){
      char c;
      cin >> c;
      a[j] |= (c - '0') << k;
    }
    int v[1 << N][1 << N];
    REP(j, 1 << N){
      int l = __builtin_popcount(j);
      REP(k, 1 << N){
        if(__builtin_popcount(k) == l){
          v[j][k] = 0;
          REP(m, N) if(j & (1 << m)){
            if(a[m] & ~k){
              v[j][k] = 10000;
              break;
            }
            v[j][k] += __builtin_popcount(k & ~a[m]);
          }
        }else{
          v[j][k] = 10000;
        }
      }
    }
    int c[1 << N][1 << N];
    memcpy(c, v, sizeof c);
    REP(j, 1 << N){
      int l = __builtin_popcount(j);
      REP(k, 1 << N) if(__builtin_popcount(k) == l){
        REP(m, j) if(m > 0 && (~j & m) == 0){
          REP(n, k) if(c[m][n] < 10000 && n > 0 && (~k & n) == 0){
            if(c[m][n] + c[j & ~m][k & ~n] < c[j][k]){
              c[j][k] = c[m][n] + c[j & ~m][k & ~n];
            }
          }
        }
      }
    }
    printf("Case #%d: %d\n", i+1, c[(1 << N) - 1][(1 << N) - 1]);
  }

  return 0;
}

