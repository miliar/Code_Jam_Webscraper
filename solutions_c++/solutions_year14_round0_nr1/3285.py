#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
    freopen("data.in","r",stdin);
   freopen("data.out","w",stdout);
  int T,t;
  int i,j;
  cin>>T;
  int maps[11][11];
  int x;
  int a,b;
  for(t=1;t<=T;t++)
  {
      scanf("%d",&a);
      for(i=1;i<=4;i++)
      {
          for(j=1;j<=4;j++)
          {
              cin>>maps[i][j];
          }
      }
      scanf("%d",&b);
      for(i=1;i<b;i++)
        for(j=1;j<=4;j++)cin>>x;
      int leap=0;
      int st=0;
      for(j=1;j<=4;j++)
      {
          cin>>x;
          for(i=1;i<=4;i++)
          {
              if(x==maps[a][i])
              {
                  leap++;
                  st=x;
              }
          }
      }
      for(i=b+1;i<=4;i++)
        for(j=1;j<=4;j++)cin>>x;
      printf("Case #%d: ",t);
      if(leap==0)cout<<"Volunteer cheated!"<<endl;
      if(leap==1)cout<<st<<endl;
      if(leap>1)cout<<"Bad magician!"<<endl;

  }
  return 0;
}
