#include <iostream>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
using namespace std;
typedef long long int int64;
int main(){
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int64 i,j,k,n,t,cnt=1,ans,x,a[100001];
  cin>>t;
  while(t--){
    scanf("%lld %lld",&n,&x);ans=0;
    for(i=0;i<n;i++)scanf("%lld",&a[i]);
    sort(a,a+n);
    for(i=0,j=n-1;i<=j;){
      if(a[i]+a[j]<=x){ans++;i++;j--;}
      else {ans++;j--;}
    }
    printf("Case #%lld: %lld\n",cnt,ans);
    cnt++;
  }
  return 0;
}

