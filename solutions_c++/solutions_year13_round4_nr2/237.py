#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
long long t,p,n,x,y,mid,tot,x1,x2;

bool ok(long long lmt){
  long long tst = 1,zz = 0;
  while (lmt>=tst){
      lmt-=tst;
      tst*=2;
      zz+=tot/tst;  
  }
  return zz<p;
}

bool ok2(long long lmt){
  long long tst = 1,zz = 0;
  lmt = tot-1-lmt;
  while (lmt>=tst){
      lmt-=tst;
      tst*=2;
      zz+=tot/tst;  
  }
  return tot-zz<=p;
}


int main(){
    freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
    cin>>t;
    for (int i=1;i<=t;i++){
        cin>>n>>p;
        x = 0;
        y = 1;
        tot = (y<<n);
        y=tot-1;
        while (x<y){
              mid = (x+y)/2;
              if (ok(mid+1))
                 x = mid+1;
              else 
                 y = mid;
        }
        x1 = x;
       
        x = 0;
        y = tot-1;
        while (x<y){
           mid = (x+y)/2;
           if (ok2(mid+1))     
              x = mid+1;
           else
              y = mid;
        } 
        //cout<<ok(6)<<endl;
        x2 = x;
        cout<<"Case #"<<i<<": "<<x1<<" "<<x2<<endl;
    }
    return 0;
}
