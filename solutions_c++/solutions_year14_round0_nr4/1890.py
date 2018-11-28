#include <cstdio>
#include <algorithm>
using namespace std;

double naomi[1005], ken[1005];

void work(int ind) {
  printf("Case #%d: ", ind);
  int N;
  scanf("%d", &N);
  int i;
  for(i = 0; i < N; i++) {
    scanf("%lf", &naomi[i]);
  }
  for(i = 0; i < N; i++) {
    scanf("%lf", &ken[i]);
  }
  sort(naomi, naomi + N);
  sort(ken, ken + N);
  int cnt, nind, kind;

  cnt = 0;
  kind = nind = 0;
  while(nind < N) {
    if(naomi[nind] > ken[kind]) {
      cnt++;
      nind++;
      kind++;
    }
    else {
      nind++;
    }
  }
  int ans1 = cnt;

  cnt = 0;
  kind = nind = 0;
  while(kind < N) {
    if(naomi[nind] < ken[kind]) {
      cnt++;
      nind++;
      kind++;
    }
    else {
      kind++;
    }
  }
  int ans2 = N - cnt;

  printf("%d %d\n", ans1, ans2);
}

int main() {
  int T;
  scanf("%d", &T);
  int i;
  for(i = 0; i < T; i++) {
    work(i + 1);
  }
  return 0;
}
