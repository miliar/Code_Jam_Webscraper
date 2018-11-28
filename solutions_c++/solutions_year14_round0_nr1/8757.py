#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
   int t,g1,g2,a[4][4],b[4][4],n;
   scanf("%d",&t);
   for(int cs=1;cs<=t;cs++){
       scanf("%d",&g1);
       for(int i=0;i<4;i++){
        scanf("%d %d %d %d",&a[i][0],&a[i][1],&a[i][2],&a[i][3]);
       }
       scanf("%d",&g2);
       for(int i=0;i<4;i++){
        scanf("%d %d %d %d",&b[i][0],&b[i][1],&b[i][2],&b[i][3]);
       }
       int found =0;
       if(a[g1-1][0]==b[g2-1][0] || a[g1-1][0] ==b[g2-1][1] || a[g1-1][0]==b[g2-1][2] || a[g1-1][0]==b[g2-1][3]){
           n = a[g1-1][0];
           found++;
       }
       if(a[g1-1][1]==b[g2-1][0] || a[g1-1][1] ==b[g2-1][1] || a[g1-1][1]==b[g2-1][2] || a[g1-1][1]==b[g2-1][3]){
            n = a[g1-1][1];
           found++;
       }
       if(a[g1-1][2]==b[g2-1][0] || a[g1-1][2] ==b[g2-1][1] || a[g1-1][2]==b[g2-1][2] || a[g1-1][2]==b[g2-1][3]){
            n = a[g1-1][2];
           found++;
       }
       if(a[g1-1][3]==b[g2-1][0] || a[g1-1][3] ==b[g2-1][1] || a[g1-1][3]==b[g2-1][2] || a[g1-1][3]==b[g2-1][3]){
            n = a[g1-1][3];
           found++;
       }
       if(found==0){
           printf("Case #%d: Volunteer cheated!\n",cs);
       }else if (found == 1){
             printf("Case #%d: %d\n",cs,n);
           
       }else{
        printf("Case #%d: Bad magician!\n",cs);
       }   
   }
   return 0;
}
