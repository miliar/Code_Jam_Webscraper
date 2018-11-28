#include<stdio.h>
int main()
{
    int t,num,a[4],temp,b;
    scanf("%d",&t);
    b=t;
    while(t--)
    {
              printf("case no.#%d\n",b-t);
             scanf("%d",&num);
              for(int i=0;i<4;i++)
              {
                      if(i==num-1)
                      {
                                  for(int j=0;j<4;j++)
                                          {
                                                      scanf("%d",&a[j]);                                         
                                          }
                                          
                      }
                      else
                      {
                      for(int j=0;j<4;j++)
                      {
                              scanf("%d",&temp);
                      }
                      }
              }
              scanf("%d",&num);
              int count=0,temp1; 
              for(int i=0;i<4;i++)
              {
                      if(i==num-1)
                      {
                                  for(int j=0;j<4;j++)
                                          {
                                                      scanf("%d",&temp);
                                                      for(int k=0;k<4;k++)
                                                      {
                                                              if(a[k]==temp)
                                                              {count++;temp1=temp; break;}
                                                      }                                         
                                          }
                                         
                      }
                      else
                      {
                      for(int j=0;j<4;j++)
                      {
                              scanf("%d",&temp);
                      }
                      }
              }
              switch(count)
              {
                           case 1:
                                printf("Case #%d: %d\n",b-t,temp1);
                                break;
                           case 0:
                                printf("Case #%d: Volunteer cheated!\n",b-t);
                                break;
                           default:
                                printf("Case #%d: Bad magician!\n",b-t);
                                break;                 
              }
    }
    return 0;
}
