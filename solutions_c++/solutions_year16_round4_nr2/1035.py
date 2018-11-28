#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf(stderr, args)

typedef long long ll;
typedef pair<int,int> pii;
const int oo = 0x3f3f3f3f;

double memo[18][1 << 18];
bool mark[18][1 << 18];
int N;
double p[18];

double go(int votes, int mask) {
  if (mask == 0) return votes == 0;
  if (votes < 0) return 0.0;
  
  if (mark[votes][mask]) return memo[votes][mask];
  mark[votes][mask] = 1;
  
  double ret = 0;
  for (int x = 0; x < N; ++x) {
    if (mask & (1 << x)) {
      int nmask = mask & (~(1 << x));
      ret += p[x] * go(votes - 1, nmask) + (1.0 - p[x]) * go(votes, nmask);
      break;
    }
  }
  
  return memo[votes][mask] = ret;
}

int main() {
  int TC; scanf("%d", &TC);
  
  for (int caso = 1; caso <= TC; ++caso) {
    memset(mark, 0, sizeof mark);
  
    int K; scanf("%d %d", &N, &K);
    
    for (int i = 0; i < N; ++i) scanf("%lf", &p[i]);
    
    
    double best = 0.0;
    for (int mask = 0; mask < (1 << N); ++mask) {
      if (__builtin_popcount(mask) == K) {
        double rsp = go(K / 2, mask);
        best = max(best, rsp);
        /*for (int submask = (mask - 1) & mask; submask; submask = (submask - 1) & mask) {
          if (__builtin_popcount(submask) == K / 2) {
            double rsp = 0;
            for (int votes = 0; votes <= K / 2; ++votes) {
              // cerr << votes << endl;
              rsp += go(votes, submask) * go(votes, mask & (~submask));
              // cerr << ">> " << rsp << endl;
            }
            best = max(best, rsp);
          }
        }*/
      }
    }
  
    cerr << caso << endl;
    printf("Case #%d: %.10lf\n", caso, best);
  }

  return 0;
}
