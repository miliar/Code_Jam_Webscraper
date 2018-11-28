#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<stack>
#define oo 105
using namespace std;
int a[5][5],b[5][5];
int main()
{
      int cases,T,x,y,i,j,ans;
      freopen("A-small-attempt0.in","r",stdin);
      freopen("output.txt","w",stdout);
      scanf("%d",&T);
      for (cases=1;cases<=T;cases++)
      {
              scanf("%d",&x);
              for (i=1;i<=4;i++)
                 for (j=1;j<=4;j++)
                    scanf("%d",&a[i][j]);
              scanf("%d",&y);
              for (i=1;i<=4;i++)
                 for (j=1;j<=4;j++)
                    scanf("%d",&b[i][j]);
              ans=-1;
              for (i=1;i<=4;i++)
                 for (j=1;j<=4;j++)
                    if (a[x][i]==b[y][j])
                    {
                          if (ans<0) ans=a[x][i]; else
                          if (ans>0) ans=0;
                    }
              printf("Case #%d: ",cases);
              if (!ans)  puts("Bad magician!"); else
              if (ans<0) puts("Volunteer cheated!"); else
                         printf("%d\n",ans);
      }
      return 0;
}
