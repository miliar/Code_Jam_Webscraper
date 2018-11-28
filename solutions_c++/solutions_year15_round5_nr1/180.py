#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>

using namespace std;

#define ABS(x) (((x) < 0) ? (-(x)) : (x))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MAX(a,b) (((a) > (b)) ? (a) : (b))

#define MAXN 1000000

long minm[MAXN];
long maxm[MAXN];
long sal[MAXN];
long par[MAXN];

int main (void) {
  int T;
  scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    std::priority_queue<int> mypq;
    int N;
    long D;
    scanf("%d %ld", &N, &D);
    long as, cs, rs;
    long am, cm, rm;
    scanf("%ld %ld %ld %ld", &(sal[0]), &as, &cs, &rs);
    scanf("%ld %ld %ld %ld", &(par[0]), &am, &cm, &rm);
    std::priority_queue< std::pair<int,int> > q;
    for (int i = 0; i < N; i++) {
      if (i == 0) {
        minm[i] = sal[i] - D;
        maxm[i] = sal[i];
      } else {
        sal[i] = (sal[i-1]*as + cs) % rs;
        par[i] = (par[i-1]*am + cm) % rm;
        minm[i] = MAX(sal[i]-D, minm[par[i]%i]);
        maxm[i] = MIN(sal[i], maxm[par[i]%i]);
      }
      //printf("%d %d %d %d %d\n", i, sal[i], par[i], minm[i], maxm[i]);
      if (minm[i] <= maxm[i]) {
        q.push(make_pair(-minm[i], 1));
        q.push(make_pair(-maxm[i], -1));
      }
    }
    int count = 0;
    int best = 0;
    while (!q.empty()) {
      std::pair<long,int> cur = q.top();
      //printf("%d %d\n", cur.first, cur.second);
      q.pop();
      count += cur.second;
      best = MAX(best, count);
    }
    printf("Case #%d: %d\n", currentcase, best);
  }
  return 0;
}
