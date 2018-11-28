#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<=(b);i++)

void win(int w) {
  w? puts("RICHARD"):puts("GABRIEL");
}

int main(void) {
  //int d[21][21][21]; memset(d,0,sizeof d);
  //FOR(i,1,20)
  //  FOR(j,1,20)
  //  d[1][i][j]=1;
  //FOR(x,2,20) {
  //  d[x][x][1]=1;
  //  d[x][1][x]=1;
  //  FOR(r,1,20)
  //    FOR(c,1,20) {
  //  }
  //}
  int t,x,r,c;
  scanf("%d",&t);
  for (int cs=1;cs<=t;cs++) {
    scanf("%d%d%d",&x,&r,&c);
    if (r>c)
      swap(r,c);
    printf("Case #%d: ",cs);
    if (x==1)
      win(0);
    else if (x==2)
      win((r*c)%2);
    else if (x==3)
      r<2? win(1):win((r*c)%3);
    else if (x==4)
      r<4&&c<4? win(1):win(r<=2);
  }
}
