#include<iostream>
using namespace std;
#include<cstdio>

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,x;
    scanf("%d",&t);
    for(x=0;x<t;x++)
    {
            int n,m,i,j;
            scanf("%d %d",&n,&m);
            int arr[n][m],flag=0;
            for(i=0;i<n;i++)
              for(j=0;j<m;j++)
              {  scanf("%d",&arr[i][j]);
                 if(arr[i][j]==1)
                   flag=1;
              }
            if(!flag)
            {   printf("Case #%d: YES\n",x+1);
                continue;
            }
            flag=0;
            for(i=0;i<n;i++)
            {
              for(j=0;j<m;j++)
              {
                       int flag1=0,flag2=0;      
                       if(arr[i][j]==1)
                       {
                             int row,col;
                             for(col=0;col<m;col++)
                               if(arr[i][col]>1)
                               {  flag1=1; 
                                  break;
                               }
                             for(row=0;row<n;row++)
                               if(arr[row][j]>1)
                               {  flag2=1; 
                                  break;
                               } 
                             if(flag1&&flag2)
                             {
                                        flag=1;
                                          break;
                             }
                                      
                       }     
              }   
              if(flag==1)
                break;
            }   
            if(flag==0)
            {
                    printf("Case #%d: YES\n",x+1);
            }
            else
              printf("Case #%d: NO\n",x+1);
    }
}            
    
