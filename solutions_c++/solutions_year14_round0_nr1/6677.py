#include<stdio.h>
int main()
{
    int t,a[100][100],b[100][100],index,q1,q2,c;
    scanf("%d",&t);
   for(int k=1;k<=t;k++)
    {
              
               scanf("%d",&q1);
              for(int i=1;i<=4;i++)
              {
               for(int j=1;j<=4;j++)
                       {
                   scanf("%d",&a[i][j]);
                                    
                       }        
                      
              }          
              
               scanf("%d",&q2);
              
                for(int i=1;i<=4;i++)
              {
               for(int j=1;j<=4;j++)
                       {
                       scanf("%d",&b[i][j]);
                                    
                       }        
                      
              }       
              c=0,index=1;
              for(int i=1;i<=4;i++)
              {
                      for(int j=1;j<=4;j++)
                      {
              if(a[q1][i]==b[q2][j])
                                    {
                                    c++;
                                    index=i;
                                    }        
                        }
              }   
              
              if(c==0)
              {
                                     printf("Case #%d: Volunteer cheated!\n",k);     

                
                      
              }
              else if(c==1)
              {
                   
              
                                    printf("Case #%d: %d\n",k,a[q1][index]);      
                   
              }
              else if(c>1)
              {

                      printf("Case #%d: Bad magician!\n",k);         
              }
              
              
    }
    
return 0;    
}
