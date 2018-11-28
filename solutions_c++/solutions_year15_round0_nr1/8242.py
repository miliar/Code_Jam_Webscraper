#include<stdio.h>
#include<string.h>

int main(){
  int t;
  long long i,j,s,l,ans,temp;
  scanf("%d",&t);
  for(i=1;i<=t;i++){
    ans=0;
    temp=0;
    scanf("%lld",&s);
    char a[s+1];
    scanf("%s",a);
    l=strlen(a);
    temp=(a[0]-'0');
    for(j=1;j<l;j++){
      //printf("%lld   a\n",temp);
      if(temp<j){
	//printf("%lld\n",j);
	ans+=(j-temp);
	temp+=(j-temp);
      }
      temp+=(a[j]-'0');
    }
    printf("Case #%lld: %lld\n",i,ans);
  }
  return 0;
}
