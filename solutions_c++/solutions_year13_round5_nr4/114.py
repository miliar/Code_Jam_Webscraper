#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<cassert>
#include<map>
#define INF (1000000000000000LL)
using namespace std;
typedef long long ll;
int zz;
double pc[1LL<<21LL];
ll optc(ll mask, ll len){
  ll opts=0;
  for(int i=0;i<len;i++){
    if(!(mask&(1LL<<i)))
      opts++;
  }
  return opts;
}
double prof(ll mask, ll len){
  if(pc[mask]>-0.5)
    return pc[mask];
  ll opt=optc(mask,len);
  if(opt==0)
    return 0;
  double ept=0;
  for(ll i=0;i<len;i++){
    if(!(mask&(1LL<<i))){
      ll j;
      ll k;
      for(k=0, j=(i+1)%len;mask&(1LL<<j);j=(j+1)%len,k++);
      ept+=(k+1)*(prof(mask+(1LL<<i),len)+k);
    }
  }
  pc[mask]=((double)ept)/((double)len);
  return pc[mask];
}
int main(){
  int ntest;
  cin>>ntest;
  char inp[30];
  ll inmask;
  ll n;
  bool debug=false;
  bool spam=true;
  for(zz=1;zz<=ntest;zz++){
    if(spam)
      printf("Case #%d: ",zz);
    scanf("%s",inp);
    for(n=0;inp[n]!='\0';n++);
    inmask=0;
    for(ll i=0;i<(1LL<<n);i++){
      pc[i]=-1;
    }
    for(ll i=0;i<n;i++){
      if(inp[i]=='X')
        inmask+=(1LL<<(n-i-1));
    }
    printf("%.10lf\n",((double)(optc(inmask,n)*n))-prof(inmask,n)*0.5);
  }
  return 0;
}
