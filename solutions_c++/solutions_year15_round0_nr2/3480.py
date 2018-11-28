// Author: Kamil Nizinski
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
#include <math.h>
#define debug(fmt,...) fprintf(stderr,fmt, ## __VA_ARGS__)
#define mp make_pair
#define ft first
#define sd second
#define psb push_back
#define ppb pop_back
using namespace std;
typedef long long int ll;
typedef long long unsigned llu;
typedef double dd;
const int inf=1000000009;
int ans_with(const int up_b, int * P, int D) {
  int ans=up_b;
  for(int i=1;i<=D;i++) ans+=(P[i]-1)/up_b;
  return ans;
}
void solve() {
  int D,P[1003],up_b,max_P;
  scanf("%d",&D);
  for(int i=1;i<=D;i++) {
    scanf("%d",&P[i]);
    max_P=max(max_P,P[i]);
  }
  int ans=inf;
  for(up_b=max_P;up_b>0;up_b--) ans=min(ans,ans_with(up_b,P,D));
  printf("%d\n",ans);
}
int main()
{
  int z;
  scanf("%d",&z);
  for(int i=1;i<=z;i++) {
    printf("Case #%d: ",i);
    solve();
  }
  return 0;
}
