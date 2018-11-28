#include <cstdio>

int T, tt;
int P[4000];
int best;
int max;
const int base = 2000;
      
void search(int i, int cost) {
  
  if(cost > best)
    return;
  if(i == 0) {
    if(cost < best)
      best = cost;
    return;
  }
  
  // special
  int tmp = P[base +i];
  for(int div = 2; div <= i/2; ++div) {
    P[base + i/div] += tmp*(div-1);
    P[base + i/div + i%div] += tmp;
    P[base + i] = 0;
    int j;
    for(j = i-1; j >= 1 && P[base + j] == 0; --j)
      ;
    search(j, cost+tmp*(div-1));
    P[base + i/div] -= tmp*(div-1);
    P[base + i/div + i%div] -= tmp;
    P[base + i] = tmp;
  }

  // regular
  for(int k = 0; k <= base + max; ++k)
    P[k] = P[k+1];
  search(i-1, cost+1);
  for(int k = base + max; k >= 1; --k)
    P[k] = P[k-1];

}

int solve() {
  int i, j;
  int res;
  for(i = 0; i < 4000; ++i)
    P[i] = 0;

  int D;
  max = -1;
  scanf("%d", &D);
  for(i = 0; i < D; ++i) {
    int val;
    scanf("%d", &val);
    P[base + val] += 1;
    if(val > max)
      max = val;
  }
  best = 999999;

  search(max, 0);

  return best;
}

int main() {

  scanf("%d", &T);
  for(tt = 1; tt <= T; ++tt) {

    int res = solve();
    printf("Case #%d: %d\n", tt, res);
  }
  return 0;
}
