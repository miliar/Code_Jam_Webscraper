#include <stdio.h>

int main()
{
    int t[101],t1[4][4],t2[4][4];
    int nbr_test,i,j,k,l,test1,test2;
    scanf("%d",&nbr_test);
    for(i=0;i<nbr_test;i++)
    {
                           l=0;
      scanf("%d",&test1);                    
      for(j=0;j<4;j++) 
      {
                       for(k=0;k<4;k++)
                       {
                          scanf("%d",&t1[j][k]);             
                       }
      }                    
      scanf("%d",&test2);                    
      for(j=0;j<4;j++) 
      {
                       for(k=0;k<4;k++)
                       {
                          scanf("%d",&t2[j][k]);             
                       }
      }  
      for(j=0;j<4;j++) 
      {
                       for(k=0;k<4;k++)
                       {
                          if ( t1[test1-1][j] ==  t2[test2-1][k] ) l++;
                          if ( t1[test1-1][j] ==  t2[test2-1][k] ) t[nbr_test+i]=t1[test1-1][j];         
                       }
      }  
        t[i]=l;                  
    }
    for(i=0;i<nbr_test;i++)
    {
                           if (t[i]==0) printf("Case #%d: Volunteer cheated!\n",i+1);
                           if (t[i]==1) printf("Case #%d: %d\n",i+1,t[nbr_test+i]);
                           if (t[i]>1) printf("Case #%d: Bad magician!\n",i+1);
    }
    return 0 ;
}
