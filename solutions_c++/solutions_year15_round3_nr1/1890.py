#include<bits/stdc++.h>
using namespace std;
int main(){
  int T,R,C,W;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    scanf("%d %d %d",&R,&C,&W);
    int count=0;
    for(int i=0;i<C;i+=W)
      count++;
    count*=R;
    count+=(W-1);
    printf("Case #%d: %d\n",t,count);
  }
  return 0;
}
      
