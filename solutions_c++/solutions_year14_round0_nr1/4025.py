#include <stdio.h>

using namespace std;

 int main()
 {
     int i,j,t,m,n,a[4][4],b[4][4];

     scanf("%d",&t);
     int count=1;
     while(t--)
     {
         scanf("%d",&m);
         for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                     scanf("%d",&a[i][j]);
         scanf("%d",&n);
         for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                     scanf("%d",&b[i][j]);

         int match=0,num;

         for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            if(a[m-1][i]==b[n-1][j])
                {
                    match++;
                    num=a[m-1][i];
                }

         printf("Case #%d: ",count++);

         if(match==1)
            printf("%d",num);
         else
         if(match>1)
            printf("Bad Magician!");
         else
            printf("Volunteer cheated!");
            printf("\n");


     }
 }
