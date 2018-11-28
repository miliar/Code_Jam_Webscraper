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

void solve() {
  char T[1007];
  int S;
  scanf("%d",&S);
  scanf("%s",T);
  int ans=0,appl=0;
  int i=0;
  while(appl<S) if(i<=appl) { appl+=T[i]-'0'; i++; }
  else { appl++; ans++; }
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
