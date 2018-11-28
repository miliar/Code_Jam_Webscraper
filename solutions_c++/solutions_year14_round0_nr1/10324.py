#include<bits/stdc++.h>
using namespace std;
int main(){
   freopen("A-small-attempt4.in","r",stdin);
   freopen("output.txt","w",stdout);
   int t,i,j;
   cin>>t;
   for(int x=0;x<t;x++){
       int b[8],c;
       int a,e;
       cin>>a;
       for(i=0;i<4;i++){
          for(j=0;j<4;j++){
             if(i==a-1)cin>>b[j];
             else cin>>c;
          }
       }
       cin>>e;
       for(i=0;i<4;i++){
          for(j=0;j<4;j++){
               if(i==e-1)
				cin>>b[j+4];
               else
				cin>>c;
          }
       }
       sort(b,b+8);
       int flag=0,ans=0;
       for(i=1;i<8;i++){
           if(b[i-1]==b[i]){
              flag++;
              ans=b[i];
           }
       }
       if(flag==0)
           printf("Case #%d: Volunteer cheated!",x+1);
       if(flag>1)
           printf("Case #%d: Bad magician!",x+1);
       if(flag==1)
          printf("Case #%d: %d",x+1,ans);
       printf("\n");
      }
   return 0;
}
