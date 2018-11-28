#include<stdio.h>
//#include<conio.h>

int main()
{
    int t,n,m,i,j,k;
    int a[5][5],b[5][5];
    int x[5],y[5];
    
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
              int c=0;
              int q =0;
              scanf("%d",&n);
              for(i=0;i<4;i++)
              {
                              for(j=0;j<4;j++)
                              {
                                              
                                              scanf("%d",&a[i][j]);
                                              if(i==n-1)
                                              x[j]=a[i][j];
                              }
              }  
              
              scanf("%d",&m);
              for(i=0;i<4;i++)
              {
                              for(j=0;j<4;j++)
                              {
                                              
                                              scanf("%d",&a[i][j]);
                                              if(i==m-1)
                                              y[j]=a[i][j];
                              }
              }
              /*for(i=0;i<4;i++)
              {
                                
                                printf("%d\n",x[i]);
                                printf("%d\n",y[i]);
              }*/
              
              for(i=0;i<4;i++)
              {
                              for(j=0;j<4;j++)
                              {
                                              
                                              if(x[i]==y[j])
                                              {
                                                            
                                                            c++;
                                                            q = x[i];
                                              }
                                              
                              }
              }
              
              if(c==0)
              printf("Case #%d: Volunteer cheated!\n",k);
              else if(c>1)
              printf("Case #%d: Bad magician!\n",k);
              else
              printf("Case #%d: %d\n",k,q);
              
    }
              //getch();
              return 0;
}
                              
