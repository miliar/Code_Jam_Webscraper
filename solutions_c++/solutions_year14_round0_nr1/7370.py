#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main(void)
{

int t=0,count=0,ans=0;
 scanf("%d",&t);
 int a[4][4],b[4][4];
 for(int i=0;i<t;i++)
 {

     ans=0;
     count=0;
     int row1=0,row2=0;
     scanf("%d",&row1);
     for(int j=0;j<4;j++)
       for(int k=0;k<4;k++)
        scanf("%d",&a[j][k]);

      scanf("%d",&row2);

       for(int j=0;j<4;j++)
       for(int k=0;k<4;k++)
        scanf("%d",&b[j][k]);

     for(int j=0;j<4;j++)
     for(int k=0;k<4;k++)
     {
         if(a[row1-1][j]==b[row2-1][k])
         {
            count++;
            ans=a[row1-1][j];
            break;
         }
     }

     if(count==1)
     printf("Case #%d: %d\n",i+1,ans);

     else if(count>1)
     printf("Case #%d: Bad magician!\n",i+1);

     else if(count==0)
     printf("Case #%d: Volunteer cheated!\n",i+1);


 }

return 0;
}
