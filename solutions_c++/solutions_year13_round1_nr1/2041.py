#include <stdio.h>
int main(){
  freopen("A-small-attempt0.in","rt",stdin);
  freopen("A-small-attempt0.out","wt",stdout);
  int test,nTest;
  long long r,t,sum,ans;
  scanf("%d",&nTest);
  for(test =1;test<=nTest;test++){
    scanf("%lld %lld",&r,&t);
    ans=0;
    for(long long j=2*r+1,sum=j;sum<=t;j+=4,sum+=j){
        ans++;
    }
    printf("Case #%d: %lld\n",test,ans);
  }
  return 0;
}
