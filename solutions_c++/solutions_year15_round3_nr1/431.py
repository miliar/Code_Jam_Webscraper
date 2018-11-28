#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <queue>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int w;
bool v[30][5];
int dp[30][5];
int f(int x,int y) {
  if (v[x][y])
    return dp[x][y];
  v[x][y]=true;
  dp[x][y]=1000000;
  if (x==w)
    dp[x][y]=(y==1?w:1);
  else if (x<2*w && y==1)
    dp[x][y]=w+1;
  else if (x<w)
    dp[x][y]=(y==1?1000000:0);
  else {
    for(int i=0;i<x-1;i++) {
      dp[x][y]=min(dp[x][y],1+min(f(i,y)+f(x-1-i,0),f(x-1-i,y)+f(i,0)));
    }
  }
  //printf("%d %d %d\n",x,y,dp[x][y]);
  return dp[x][y];
}
int main() {
  int zz;
  cin>>zz;
  for(int zzz=1;zzz<=zz;zzz++) {
    int r,c,o;
    o=0;
    cin>>r>>c>>w;
    memset(v,0,sizeof(v));
    for (int i=0;i<r;i++) {
      o+=f(c,(i==0));
    }
    printf("Case #%d: %d\n",zzz,o);
  }
  return 0;
}
