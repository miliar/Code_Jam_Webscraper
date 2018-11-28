#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
#include<deque>
using namespace std;
#define pi 3.141592653589793238
int main(){
  int T,ccount=0;
  double r,t,used;
  bool ok=true;
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    printf("Case #%d: ",tc);
    cin>>r>>t;
    ccount=0;
    ok=true;
    while(ok){
      ok=false;
      used=(r+1)*(r+1);
      used-=r*r;
      //cout<<used<<"  "<<t<<endl;
      if(used<=t){
        ccount++;
        t-=used;
        r+=2;
        ok=true;
      }
    }
    cout<<ccount<<"\n";
  }
  return 0;
}
