#include<stdio.h>
int main(){
    int t,i,ans,smax,np,x;
    char s[1003];
    scanf("%d",&t);
    for(x=1;x<=t;x++){
     scanf("%d %s",&smax,s);
     for(i=ans=np=0;s[i];i++){
      if(np<i){
       ans+=i-np;
       np=i;
      }
      np+=s[i]-'0';
     }
     printf("Case #%d: %d\n",x,ans);
    }
    return 0;
}
     
