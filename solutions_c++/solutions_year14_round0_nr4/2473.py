#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;
int const MAXN = 1000;
int T, N, i, j;
double naomi[MAXN], ken[MAXN];
bool flag[MAXN];
int getDecWar() {
  int point = 0;
  for(int i=0, j=0; i<N && j<N; i++)
    if(naomi[i]>ken[j]) point++, j++;
  return point;
}
int getWar() {
  int point = 0;
  for(int i=0, j=0; i<N && j<N; i++)
    if(naomi[j]<ken[i]) point++, j++;
  return point;
}
int main() {
  scanf("%d", &T);
  for(int cas=1; cas<=T; cas++) {
    memset(flag, false, sizeof(flag));
    scanf("%d", &N);
    for(i=0; i<N; i++)
      scanf("%lf", &naomi[i]);
    for(i=0; i<N; i++)
      scanf("%lf", &ken[i]);
    sort(naomi, naomi+N);
    sort(ken, ken+N);
    int decWar = getDecWar();
    int war = getWar();
    printf("Case #%d: %d %d\n", cas, decWar, N-war);
  }
  return 0;
}
