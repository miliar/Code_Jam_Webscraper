#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<string>
#include<string.h>
#include<math.h>
#define in_t(t) scanf("%d",&t)
int a[5][5],b[5][5];
using namespace std;
int main()
{
    int t,n1,i,j,c,n2,x,k;
    in_t(t);
    for(k=1;k<=t;k++)
    {
              in_t(n1);
              for(i=1;i<=4;i++)
              for(j=1;j<=4;j++)
              in_t(a[i][j]);
              in_t(n2);
              for(i=1;i<=4;i++)
              for(j=1;j<=4;j++)
              in_t(b[i][j]);
              c=0;
              for(i=1;i<=4;i++)
              {
                 for(j=1;j<=4;j++)
                 {
                                  
                        if(a[n1][i]==b[n2][j])
                        {
                        c++;
                        x=a[n1][i];
                        }
                       
                 }
                  if(c>1)
                        break;
              }
              if(c==0)
              printf("Case #%d: Volunteer cheated!\n",k);
              else
              if(c==1)
              printf("Case #%d: %d\n",k,x);
              else
              printf("Case #%d: Bad magician!\n",k);
    }
    return 0;
}
              
                               
                              
              
