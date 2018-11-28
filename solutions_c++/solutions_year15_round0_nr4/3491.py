#include<stdio.h>
using namespace std;
int main(){
 int t,x,r,c,flag;
 scanf("%d",&t);
 for(int j=1;j<=t;++j){
  scanf("%d%d%d",&x,&r,&c);
  flag=1;
  if(x==1) flag=0;
  else if(x==2){
   if((r*c)%2==0) flag=0;
  }
  else if(x==3){
   if((r*c)%3==0 && r>1 && c>1) flag=0;
  }
  else if(x==4){
   if((r*c)%4==0 && r>1 && c>1){
    if(r>=3 && c>=3) flag=0;
   }
  }
  if(flag==0) printf("Case #%d: GABRIEL\n",j);
  else printf("Case #%d: RICHARD\n",j);
 }
 return 0;}
