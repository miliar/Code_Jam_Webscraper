//GCJ
/*
ID: Geek7
LANG: C++
TASK:
STATE:
MEMO:
*/
#include<iostream>
#include<cmath>
#include<map>
#include<cstring>
#include<cstdio>
#include<cstdarg>
#include<cstdio>
#include<cassert>
#include<vector>
#include<string>
#include<algorithm>
#include<list>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
#include<numeric>
#include<functional>
#include<utility>
#include<bitset>
#define LL long long
#define maxab(a,b) (a)>(b)?(a):(b)
#define LL long long
using namespace std;
LL gs(LL a){
  LL cnt=0,i,len,tt=9;
  for(i=1;;i++){
    if(cnt+tt>=a) {len=i;break;}
    cnt+=tt;
    if(i%2==0) tt*=10;
  }
  a-=cnt;
  LL half=1;
  for(i=2;i<=(len+1)/2;i++) half*=10;
  half+=a-1;
  LL res=half;
  if(len&1) half/=10;
  while(half){
    res=res*10+half%10;
    half/=10;
  }
  return res;
}
bool judge(LL n){
  char a[30],i=0,j;
  LL k=n;
  while(n){
    a[i++]=n%10;
    n/=10;
  }
  for(j=0;j<i/2;++j){
    if(a[j]!=a[i-1-j]) break;
  }
  if(j==i/2)return 1;
  return 0;
}
LL erfen(LL l,LL r,LL k){
  LL mid;
  while(l<r){
    mid=(l+r+1)>>1;
    if(gs(mid)<=k) l=mid;
    else r=mid-1;
  }
  return l;
}
int main(){
  int T,cases=1;
  LL s,e,ans;
 // freopen("input.txt","r",stdin);
 // freopen("output.out","w",stdout);
  scanf("%d",&T);
  while(T--){
    scanf("%I64d%I64d",&s,&e);
    int x=sqrt(s),y=sqrt(e);
    if((LL)(x*x)!=s) ++x;
    ans=0;
    for(int i=x;i<=y;++i){
      if(judge(i) && judge(i*i)) ++ans;
    }
    printf("Case #%d: %lld\n",cases++,ans);
  }
  return 0;
}
