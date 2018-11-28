#include <stdio.h>
#include <string>
int main(){
	freopen("A-small.txt","r",stdin);
	freopen("Aoutput.out","w",stdout);
  int t,maxsh;
  scanf("%d",&t);
  for(int j=1; j<t+1; ++j){
    scanf("%d",&maxsh);
    char str[1005];
    scanf("%s",str);
    int cnt=0,pl=0,sz=strlen(str);
    for(int i=0; i<sz; ++i){
      int num=str[i]-'0';
      if(i<=pl){
        if(num==0) continue;
        else pl+=num;
      }
      else if(i>pl){
        if(num==0) continue;
        cnt+=i-pl;
        pl+=num+i-pl;
      }
    }
    printf("Case #%d: %d\n",j,cnt);
  }
  return 0;
}
