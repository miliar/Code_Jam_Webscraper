#include<stdio.h>

int main(int argc,char*agrv[]){
  int T;scanf("%d",&T);
  for(int tc=1;tc<=T;tc++){
    int res=0;
    int S;scanf(" %d",&S);
    char cur;
    int sum;scanf(" %c",&cur); sum=cur-48;
    for(int i=1;i<=S;i++){
      if(i-sum>res) res=i-sum;
      scanf("%c",&cur); sum+=cur-48;
    }
    printf("Case #%d: %d\n",tc,res);
  }
  return 0;
}
