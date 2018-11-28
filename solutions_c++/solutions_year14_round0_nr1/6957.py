
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
   int T,i1,i2,r1[5][5],r2[5][5],count,ans[5],i,j,k,l,m;


   scanf("%d",&T);
   for(i=1;i<=T;i++)
   {
   count=0;

     scanf("%d",&i1);

     for(j=1;j<=4;j++)
     {
     
     for(k=1;k<=4;k++)
     {
       scanf("%d",&r1[j][k]);
     }

     }

     scanf("%d",&i2);

     for(j=1;j<=4;j++)
     {
    
     for(k=1;k<=4;k++)
     {
       scanf("%d",&r2[j][k]);
     }

     }
     for(l=1;l<=4;l++)
     {
      for(m=1;m<=4;m++)
{
           if(r1[i1][l]==r2[i2][m])
       {
	ans[count]=r1[i1][l];
	count++;
       }
}
     }
     if(count==1)
     {
     printf("\nCase #%d: %d",i,ans[0]);

     }
     if(count==0)
     {
	printf("\nCase #%d: Volunteer cheated!",i);
     }
     if(count>1)
     {
      printf("\nCase #%d: Bad magician!",i);
     }


   }

   /* clean up */
   

   return 0;
}
