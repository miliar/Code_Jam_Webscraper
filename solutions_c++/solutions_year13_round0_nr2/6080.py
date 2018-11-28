#include <stdio.h>
#include <iostream>
using namespace std;
int num[50][50];
int cas,n,m;
int judge(int a,int b){
   bool res1=false,res2=false;
   for(int i=0;i<m;i++) {
     if(num[a][i]>1){
       res1=true;
       break;
     }
   }

   for(int i=0;i<n;i++) {
     if(num[i][b]>1) {
        res2=true;
        break;
     }
   }
   if(res1&&res2)return 1;
   else return 0;
}
int main() {
   freopen("B-small-attempt0.in","r",stdin);
   freopen("data.out","w",stdout);
   scanf("%d",&cas);
   for(int t=1;t<=cas;t++) {
      scanf("%d%d",&n,&m);
      for(int i=0;i<n;i++){
        for(int j=0;j<m;j++)scanf("%d",&num[i][j]);
      }
      int flag=0;
      for(int i=0;i<n&&flag==0;i++) {
        for(int j=0;j<m&&flag==0;j++) {
          if(num[i][j]==1){
            flag=judge(i,j);
          }
        }
      }

      printf("Case #%d: ",t);
      if(flag==0)printf("YES\n");
      else printf("NO\n");
   }
   return 0;
}
