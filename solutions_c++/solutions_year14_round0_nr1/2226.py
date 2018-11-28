#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<limits.h>
#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,a,arr[10][10],b,i,j,pos;
    scanf("%d",&t);
    for(b=1;b<=t;b++)
    {
              int hash[20]={0};
              int k=1;
              while(k<=2)
              {
              scanf("%d",&a);
              for(i=1;i<=4;i++)
              {
                      for(j=1;j<=4;j++)
                      {
                                       scanf("%d",&arr[i][j]);
                                       if(i==a)
                                       hash[arr[i][j]]++;
                      }
              }
              k++;
              }
              int flag=0;
              for(i=1;i<=16;i++)
              {
                                if(hash[i]==2)
                                {
                                              if(!flag)
                                              {
                                                       flag=1;
                                                       pos=i;
                                              }
                                              else
                                              {
                                                  flag=-1;
                                                  break;
                                              }
                                              
                                }
              }
              if(!flag)
              printf("Case #%d: Volunteer cheated!\n",b);
              else if(flag==-1)
              printf("Case #%d: Bad magician!\n",b);
              else
              printf("Case #%d: %d\n",b,pos);
    }
    return 0;
}
              
              
