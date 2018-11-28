#include <iostream>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
typedef long long int int64;
int main(){
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int64 i,j,k,n,t,cnt=1,ans1,ans2,u1[1005],u2[1005];
  double w1[1005],w2[1005];
  cin>>t;
  while(t--){
    scanf("%lld",&n);
    for(i=0;i<n;i++)scanf("%lf",&w1[i]);
    for(i=0;i<n;i++)scanf("%lf",&w2[i]);
    sort(w1,w1+n);sort(w2,w2+n);
//    for(i=0;i<n;i++)cout<<w1[i]<<" ";cout<<endl;
//    for(i=0;i<n;i++)cout<<w2[i]<<" ";cout<<endl;

    memset(u1,0,sizeof(u1));memset(u2,0,sizeof(u2));
    ans1=0;
    for(i=0;i<n;i++){
      for(j=0;j<n;j++)
        if(w2[i]<w1[j]&&u1[j]==0){u1[j]=1;ans1++;break;}
    }
   

    memset(u1,0,sizeof(u1));memset(u2,0,sizeof(u2));
    ans2=0;
    for(i=0;i<n;i++){
      for(j=0;j<n;j++)
        if(w1[i]<w2[j]&&u2[j]==0){u2[j]=1;ans2++;break;}
    }
    ans2=n-ans2;


    printf("Case #%lld: %lld %lld\n",cnt,ans1,ans2);
    cnt++;
  }
  return 0;
}

