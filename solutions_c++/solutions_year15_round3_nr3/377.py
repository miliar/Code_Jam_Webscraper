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
int v,n;
int a[100];
bool used[100];
int best;
void f(int x,int c) {
  bool g[100];
  memset(g,0,sizeof(g));
  g[0]=true;
  for(int i=1;i<=v;i++) {
    if (used[i]) {
      for(int j=v;j>=0;j--)
        g[i+j]|=g[j];
    }
  }
  for(int i=1;i<x;i++)
    if(!g[i])
      return;
  bool t=true;
  for(int i=1;i<=v;i++)
    if(!g[i])
      t=false;
  if (t) {
    best=c;
    return;
  }
  if (c>=best)
    return;
  if (x==v+1)
    return;
  if (used[x])
    f(x+1,c);
  f(x+1,c);
  used[x]=true;
  f(x+1,c+1);
  used[x]=false;
}
int main() {
  int zzz;
  cin>>zzz;
  for(int zz=1;zz<=zzz;zz++) {
    int c;
    cin>>c>>n>>v;
    memset(used,0,sizeof(used));
    for(int i=0;i<n;i++) {
      cin>>a[i];
      used[a[i]]=true;
    }
    best=1000000;
    f(1,0);
    printf("Case #%d: %d\n",zz,best);
  }
  return 0;
}
