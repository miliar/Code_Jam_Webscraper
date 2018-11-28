#include<cstdio>
#include<iostream>
using namespace std;
int main() {
  int zzz;
  cin>>zzz;
  for(int zz=1;zz<=zzz;zz++) {
    int x,r,c;
    cin>>x>>r>>c;
    bool g=true;
    if(x==1) {
    }
    else if (x==2) {
      if((r*c)%2>0)
        g=false;
      if(r<2&&c<2)
        g=false;
    }
    else {
      if((r*c)%x>0)
        g=false;
      if(r<x&&c<x)
        g=false;
      if(r==1||c==1)
        g=false;
      if (x==3) {
      }
      if (x==4) {
        if(r==2&&c==2)
          g=false;
        if(r*c==8)
          g=false;
      }
    }
    printf("Case #%d: ",zz);
    cout<<(g?"GABRIEL":"RICHARD")<<endl;
  }
  return 0;
}
