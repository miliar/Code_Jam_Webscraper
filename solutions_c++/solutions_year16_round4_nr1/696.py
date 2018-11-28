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

static void output(int i, int n){
  int a[3][2] = {{0, 1}, {0, 2}, {1, 2}};
  if(n > 0){
    output(a[i][0], n - 1);
    output(a[i][1], n - 1);
  }else{
    putchar("PRS"[i]);
  }
}

int main(){
  int T;
  cin >> T;
  REP(i, T){
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    int a[3][3] = {{1, 1, 0}, {1, 0, 1}, {0, 1, 1}};
    int b[3][3];
    REP(j, N - 1){
      REP(k, 3){
        b[0][k] = a[0][k] + a[1][k];
        b[1][k] = a[0][k] + a[2][k];
        b[2][k] = a[1][k] + a[2][k];
      }
      memcpy(a, b, sizeof(b));
    }
    printf("Case #%d: ", i+1);
    bool ok = false;
    REP(j, 3){
      if(P == a[j][0] && R == a[j][1] && S == a[j][2]){
        output(j, N);
        ok = true;
        break;
      }
    }
    if(!ok){
      printf("IMPOSSIBLE\n", i+1);
    }else{
      puts("");
    }
  }

  return 0;
}

