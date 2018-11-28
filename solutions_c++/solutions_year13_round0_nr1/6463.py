#include<iostream>
#include<string>
using namespace std;
char arr[4][4];
bool row_check(int x,char c)
{
    bool flag=0;
    int count=0;
    for(int i=0;i<4;i++)
    {
            if(arr[x][i]=='T')
            {
                              count++;
            }
            else if(arr[x][i]==c && count<=1)
            {
                 continue;
            }
            else
            return 0;
    }
    return 1;
}
bool col_check(int x,char c)
{
    bool flag=0;
    int count=0;
    for(int i=0;i<4;i++)
    {
            if(arr[i][x]=='T')
            {
                              count++;
            }
            else if(arr[i][x]==c && count<=1)
            {
                 continue;
            }
            else
            return 0;
    }
    return 1;
}
bool diag_check1(char c)
{
     int count=0;
     for(int i=0;i<4;i++)
     {
             for(int j=0;j<4;j++)
             {
                     if(i==j && arr[i][j]=='T')
                     count++;
                     else if(i==j && arr[i][j]==c && count<=1)
                     continue;
                     else if(i==j)
                     return 0;
             }
     }
     return 1;
}
bool diag_check2(char c)
{
     int count=0;
     for(int i=0;i<4;i++)
     {
             for(int j=3;j>=0;j--)
             {
                     if(i+j==3 && arr[i][j]=='T')
                     count++;
                     else if(i+j==3 && arr[i][j]==c && count<=1)
                     continue;
                     else if(i+j==3)
                     return 0;
             }
     }
return 1;
}                 
main()
{
      int t;
      cin>>t;
      int caseno=0;
      while(t--)
      {
                caseno++;
      for(int i=0;i<4;i++)
      {
              for(int j=0;j<4;j++)
              {
                      cin>>arr[i][j];
                      //cout<<arr[i][j];
              }
      }
      bool draw=0,owin=0,xwin=0,comp=1;
      for(int i=0;i<4;i++)
      {
              for(int j=0;j<4;j++)
              {
                      if(row_check(i,'X') || col_check(j,'X'))
                      xwin=1;
                      if(row_check(i,'O') || col_check(j,'O'))
                      owin=1;
                      if(arr[i][j]=='.')
                      comp=0;
              }
      }
      if(diag_check1('X') || diag_check2('X'))
      xwin=1;
      if(diag_check1('O') || diag_check2('O'))
      owin=1;
      if(xwin)
      cout<<"Case #"<<caseno<<": X won"<<endl;
      else if(owin)
      cout<<"Case #"<<caseno<<": O won"<<endl;
      else if(comp==0)
      cout<<"Case #"<<caseno<<": Game has not completed"<<endl;
      else
      cout<<"Case #"<<caseno<<": Draw"<<endl;
      }
//system("pause");
}
