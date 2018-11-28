#include <stdio.h>

int main(){
  long long t,smax,i,invites,standing,dig,j;
  char arr[1002];
  scanf("%lld",&t);
  for(j=1;j<=t;j++){
    scanf("%lld",&smax);
    scanf("%s",arr);
    standing=0;
    invites=0;
    for(i=0;i<=smax;i++){
      dig=arr[i]-'0';
      if(i>standing){
	invites+=i-standing;
	standing+=i-standing;
      }
      standing+=dig;
    }
    printf("Case #%lld: %lld\n",j,invites);
  }
  return 0;
}
