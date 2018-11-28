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
int64 i,j,k,n,t,cn,a1,a2,m1[4][4],m2[4][4],ar[20],fl,ans,cnt=1;
cin>>t;
while(t--){
  for(i=0;i<20;i++)ar[i]=0;fl=0;ans=-1;
  scanf("%lld",&a1);
  for(i=0;i<4;i++)for(j=0;j<4;j++)scanf("%lld",&m1[i][j]);
  scanf("%lld",&a2);
  for(i=0;i<4;i++)for(j=0;j<4;j++)scanf("%lld",&m2[i][j]);

  for(i=a1-1,j=0;j<4;j++)ar[m1[i][j]]++;
  for(i=a2-1,j=0;j<4;j++)ar[m2[i][j]]++;  
  for(i=a1-1,j=0;j<4;j++){if(ar[m1[i][j]]==2){fl++;ans=m1[i][j];}}

  //for(i=0;i<=16;i++)cout<<ar[i]<<" ";cout<<endl;
  if(fl==1)printf("Case #%lld: %lld\n",cnt,ans);
  else if(fl>=2)printf("Case #%lld: Bad magician!\n",cnt);
  else printf("Case #%lld: Volunteer cheated!\n",cnt);
  cnt++;
}
  return 0;
}

