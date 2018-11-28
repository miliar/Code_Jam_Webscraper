#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
   int t,i,r1,r2,c,d1[4][4],d2[4][4],cp1[4],cp2[4],r,q,b,z,m,j;
   scanf("%d",&t);
   
   for(q=1;q<=t;q++)
   {z=0;
       scanf("%d",&r1);
       
       for(i=0;i<=3;i++)
       {
           for(j=0;j<=3;j++)
           {
               scanf("%d",&d1[i][j]);
               
           }
        }
       
       scanf("%d",&r2);
       for(r=0;r<=3;r++)
       {
           for(c=0;c<=3;c++)
           {
               scanf("%d",&d2[r][c]);
               
           }
           
       }
       
       for(i=0;i<=3;i++)
       {
           cp1[i]=d1[r1-1][i];
           cp2[i]=d2[r2-1][i];
       }
       
       
       for(i=0;i<=3;i++)
        {
            for(j=0;j<=3;j++)
            {
                if(cp1[i]==cp2[j])
                {
                   z++;
                   m=cp1[i];
                }
            }
        
        }
    
    
    
        switch(z)
        {
            case 0:printf("Case #%d: Volunteer cheated!\n",q);
            break;
            case 1:printf("Case #%d: %d\n",q,m);
            break;
            default:printf("Case #%d: Bad magician!\n",q);
        }
   }
   
    return 0;
}        