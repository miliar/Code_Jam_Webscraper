#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    int count=1;
    int first[4][4];
    int second[4][4];
    int extract[4];
    int i,j,r1,r2,re,ans;
    while(t--)
    {
         scanf("%d",&r1);
         for(i=0;i<4;i++)
         {
             for(j=0;j<4;j++)
                 scanf("%d",&first[i][j]);
         }
         r1--;
         scanf("%d",&r2);
         for(i=0;i<4;i++)
         {
              for(j=0;j<4;j++)
              {
                     scanf("%d",&second[i][j]);
              }
         }
         r2--;
         re=0;
         for(i=0;i<4;i++)
         {
             for(j=0;j<4;j++)
             {
                  if(first[r1][i]==second[r2][j])
                  {
                        re++;
                        ans=first[r1][i];
                  }      
             }
         }    
         printf("Case #%d: ",count);     
         if(re==1)
               printf("%d\n",ans);
         else
            if(re==0)
                printf("Volunteer Cheated!\n");
            else
                printf("Bad Magician!\n");
         count++;
    }
    return(0);
}
