#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <cctype>
#include <numeric>
using namespace std;

#define rep(i,n) for(int (i)=0; (i)<(int)(n); ++(i))
#define foreach(c,i) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define all(a) (a).begin(),(a).end()

double C, F, X;

double solve2() {
  double ans = 1 << 28;
  double per = 2.f, past = 0.f;

  while (true) {
    // prev
    const double prv = X / per;
    
    // next
    past += C / per;
    per += F;
    const double nxt = past + X / per;
    
    if (prv < nxt)
      break;

    ans = nxt;
  }

  return ans;
}

double solve() {
  double ans = 1 << 28, per = 2.f, past = 0.f;

  ans = min(ans, X / per);
  
  while (1) {
    // 現在のperでゴールまで
    ans = min(ans, past + X / per);

    bool ok = false;
    
    // 1個買ってから
    past += C / per; per += F;
    double v = past + X / per;
    // ans = min(ans, (past + X / per));
    if (ans > v) {
      ans = v;
      // printf("v:%f, past:%f, per:%f\n", v, past, per);
      ok = true;
    }
    
    // 終了条件
    if (!ok)
      break;
    
    // if ((past + (per/2)) > X) {
    //   break;
    // }
  }
  return ans;
}

int main() {
  int T;
  scanf("%d", &T);
  rep(z,T) {
    scanf("%lf%lf%lf", &C, &F, &X);
    printf("Case #%d: %.7f\n", z+1, solve());
    // printf("Case #%d: %.7f\n", z+1, solve2());
  }
  return 0;
}
