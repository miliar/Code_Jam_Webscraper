#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long lglg;

const int MAXN = 1000000;

int main()
{
  int T;
  scanf("%d", &T);

//  int tt = 58;
//  printf("cica");


//  for(lglg i = 0; i < 1000000000ll; ++i) {
//    tt = tt * T % 100;
//  }

//  printf("mica %d\n", tt);

  int S[MAXN+1];
  int B[MAXN+1];
  int minin[MAXN+1], maxin[MAXN+1];


  for(int t = 0; t < T; ++t) {
    int best = 0;
    printf("Case #%d: ", t+1);

    int n, d, s0, as, cs, rs, m0, am, cm, rm;
    scanf("%d%d%d%d%d%d%d%d%d%d", &n, &d, &s0, &as, &cs, &rs, &m0, &am, &cm, &rm);

    S[0] = s0;
    B[0] = -1;
    for(int i = 1; i < n; ++i) {
      s0 = (lglg(s0) * as + cs) % rs;
      S[i] = s0;
      m0 = (lglg(m0) * am + cm) % rm;
      B[i] = m0 % i;
//      printf("%d %d\n", s0, B[i]);
    }

    minin[0] = max(S[0] - d, 0);
    maxin[0] = S[0];

    for(int i = 1; i < n; ++i) {
      minin[i] = max(minin[B[i]], S[i] - d);
      maxin[i] = min(maxin[B[i]], S[i]);
      if(maxin[i] < minin[i]) {
        maxin[i] = minin[i] - 1;
      }

    }

    sort(minin, minin+n);
    sort(maxin, maxin+n);

    int num = 0;
    int mini=0, maxi=0;
    while(mini < n || maxi < n) {
      if(maxi >= n || (mini < n && minin[mini] <= maxin[maxi])) {
        ++num;
        best = max(best, num);
        ++mini;
      } else {
        --num;
        ++maxi;
      }
    }

    printf("%d\n", best);
  }

  return 0;
}
