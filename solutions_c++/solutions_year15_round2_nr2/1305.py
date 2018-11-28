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
int r,c,n;
int a[20][20];
int best;
void f(int x,int y,int q) {
  //cout<<x<<" "<<y<<" "<<c<<endl;
  if (y==c+1) {
    if (x==r) {
      if(q!=n)
        return;
      int t=0;
      int dx[]={0,-1};
      int dy[]={-1,0};
      for(int i=1;i<=r;i++) {
        for(int j=1;j<=c;j++) {
          //cout<<a[i][j]<<" ";
          for(int k=0;k<2;k++) {
           if (a[i][j]==1&&1==a[i+dx[k]][j+dy[k]])
            t++; 
          }
        }
        //cout<<endl;
      }
      //cout<<t<<endl;
      best=min(best,t);
    }
    else
      f(x+1,1,q);
  }
  else {
    a[x][y]=1;
    f(x,y+1,q+1);
    a[x][y]=0;
    f(x,y+1,q);
  }
}
int main() {
  int zzz=0;
  cin>>zzz;
  for(int zz=1;zz<=zzz;zz++) {
    cin>>r>>c>>n;
    best=(r-1)*c+(c-1)*r;
    memset(a,0,sizeof(a));
    f(1,1,0);
    printf("Case #%d: %d\n",zz,best);
  }
  return 0;
}
