#include<iostream>
#include<cstring>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("i.txt","r",stdin);
    freopen("output.jjj","w",stdout);
    int n,i,j,r,p,t,x;
    char a[4][4];
    cin>>n;
    char c=getchar();
    for(p=1;p<=n;p++)
    {
        r=0;
        x=0;
      for(i=0;i<4;i++)
      {
          for(j=0;j<4;j++)
          {
           cin>>a[i][j];
           if(a[i][j]!='.')
           x=x+1;
          }
       }
       //printf("%d",x);
      for(i=0;i<4;i++)
      {
          for(j=0;j<=0;j++)
          {
              if(a[i][j]!='.'&&a[i][j]==a[i][j+1]&&a[i][j+1]==a[i][j+2]&&a[i][j+2]==a[i][j+3]&&r==0)
              {
                  printf("Case #%d: %c won\n",p,a[i][j]);
                  r=1;
              }
              if(i==0)
              {
                  if(a[i][j]!='.'&&a[i][j]==a[i+1][j+1]&&a[i+1][j+1]==a[i+2][j+2]&&a[i+2][j+2]==a[i+3][j+3]&&r==0)
                  {
                    printf("Case #%d: %c won\n",p,a[i][j]);
                    r=1;
                  }
              }
          }
      }
      for(j=0;j<4;j++)
      {
          for(i=0;i<=0;i++)
          {
              if(a[i][j]!='.'&&a[i][j]==a[i+1][j]&&a[i+1][j]==a[i+2][j]&&a[i+2][j]==a[i+3][j]&&r==0)
              {
                   printf("Case #%d: %c won\n",p,a[i][j]);
                   r=1;
              }
              if(j==3)
              {
                  if(a[i][j]!='.'&&a[i][j]==a[i+1][j-1]&&a[i+1][j-1]==a[i+2][j-2]&&a[i+2][j-2]==a[i+3][j-3]&&r==0)
                  {
                    printf("Case #%d: %c won\n",p,a[i][j]);
                    r=1;
                  }
              }
          }
      }
      for(i=0;i<4;i++)
      {
          for(j=0;j<=0;j++)
          {
             if(a[i][j]!='.'&&((a[i][j]==a[i][j+1]&&a[i][j+1]==a[i][j+2]&&a[i][j+3]=='T'&&r==0)
                ||(a[i][j]=='T'&&a[i][j+1]==a[i][j+2]&&a[i][j+2]==a[i][j+3]&&r==0&&a[i][j+1]!='.')))
                {
                    if(a[i][j]=='T')
                    {
                        printf("Case #%d: %c won\n",p,a[i][j+1]);
                        r=1;
                    }
                    else
                    {
                        printf("Case #%d: %c won\n",p,a[i][j]);
                        r=1;
                    }
                    }
             if(i==0)
             {
                 if(a[i][j]!='.'&&((a[i][j]==a[i+1][j+1]&&a[i+1][j+1]==a[i+2][j+2]&&a[i+3][j+3]=='T'&&r==0)||
                    (a[i][j]=='T'&&a[i+1][j+1]==a[i+2][j+2]&&a[i+2][j+2]==a[i+3][j+3])&&r==0&&a[i+1][j+1]!='.'))
                 {
                    if(a[i][j]=='T')
                    {
                        printf("Case #%d: %c won\n",p,a[i+1][j+1]);
                        r=1;
                    }
                    else
                    {
                        printf("Case #%d: %c won\n",p,a[i][j]);
                        r=1;
                    }
                 }
             }
          }
      }
      for(j=0;j<4;j++)
      {
          for(i=0;i<=0;i++)
          {
              if(a[i][j]!='.'&&((a[i][j]==a[i+1][j]&&a[i+1][j]==a[i+2][j]&&a[i+3][j]=='T'&&r==0)||
                 (a[i][j]=='T'&&a[i+1][j]==a[i+2][j]&&a[i+2][j]==a[i+3][j]&&r==0&&a[i+1][j]!='.')))
              {
                 if(a[i][j]=='T')
                    {
                        printf("Case #%d: %c won\n",p,a[i+1][j]);
                        r=1;
                    }
                    else
                    {
                        printf("Case #%d: %c won\n",p,a[i][j]);
                        r=1;
                    }
              }
              if(j==3)
              {
                 if(a[i][j]!='.'&&((a[i][j]==a[i+1][j-1]&&a[i+1][j-1]==a[i+2][j-2]&&a[i+3][j-3]=='T'&&r==0)||
                    a[i][j]=='T'&&a[i+1][j-1]==a[i+2][j-2]&&a[i+2][j-2]==a[i+3][j-3]&&r==0&&a[i+1][j-1]!='.'))
                    {
                      if(a[i][j]=='T')
                    {
                        printf("Case #%d: %c won\n",p,a[i+1][j-1]);
                        r=1;
                    }
                    else
                    {
                        printf("Case #%d: %c won\n",p,a[i][j]);
                        r=1;
                    }
                    }
              }
          }
      }
      if(r==0&&x==16)
      printf("Case #%d: Draw\n",p);
      else if(r==0&&x<16)
      printf("Case #%d: Game has not completed\n",p);
    }
    return 0;
}


