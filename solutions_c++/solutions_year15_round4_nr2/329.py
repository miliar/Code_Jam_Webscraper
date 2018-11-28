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

const double EPS = 0.000001l;

int main()
{
  int T;
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    int N;
    double V, X;
//    double R[100], C[100];
    pair<double, double> taps[101]; // Temp first
    bool ov = false, bel = false;
    scanf("%d%lf%lf", &N, &V, &X);
    for(int i = 0; i < N; ++i) {
      scanf("%lf%lf", &(taps[i].second), &(taps[i].first));
      taps[i].first -= X;
      if(taps[i].first < EPS) bel = true;
      if(taps[i].first > -EPS) ov = true;
    }

    if(!bel || !ov) {
      printf("IMPOSSIBLE\n");
      continue;
    }

    sort(taps, taps+N);

    double over = 0, under = 0;
    double sumR = 0;

    for(int i = 0; i < N; ++i) {
      sumR += taps[i].second;
      if(taps[i].first > EPS) {
        over += taps[i].first*taps[i].second;
      } else if(taps[i].first < -EPS) {
        under += -taps[i].first*taps[i].second;
      }
    }
    double diff;

    if(over > under) {
      diff = over - under;
      for(int i = N-1; i >= 0 && taps[i].first > EPS; --i) {
        if(diff <= taps[i].first*taps[i].second) {
          sumR -= diff / (taps[i].first);
          break;
        }
        diff -= taps[i].first*taps[i].second;
        sumR -= taps[i].second;
      }
    } else {
      diff = under - over;
      for(int i = 0; i < N && taps[i].first < -EPS; ++i) {
        if(diff <= -taps[i].first*taps[i].second) {
          sumR -= diff / (-taps[i].first);
          break;
        }
        diff -= -taps[i].first*taps[i].second;
        sumR -= taps[i].second;
      }
    }

    printf("%.8lf\n", V / sumR);
  }

  return 0;
}
