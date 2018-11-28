#include <iostream>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
typedef long long int int64;
double fr[5000003];
int main(){
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int64 i,j,k,n,t,cnt=1;
  double c,f,x,ans,vl;
  cin>>t;
  while(t--){
    scanf("%lf %lf %lf",&c,&f,&x);
    ans = 100000.0;
    fr[0]=0.5;for(i=1;i<=5000000;i++){fr[i]=fr[i-1]+(1.0/(2+i*f));}
    for(i=0;i<=5000000;i++){
      vl=0;j=0;
      if(i>0)vl+=c*fr[i-1];
      vl+=x/(2.0+(i*f));
      if(vl<ans)ans=vl;
      else break;
    }
    printf("Case #%lld: %0.7lf\n",cnt,ans);
    cnt++;
  }
  return 0;
}

