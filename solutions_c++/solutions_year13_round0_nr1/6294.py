#include<iostream>
#include<cstdio>
#define N 4
using namespace std;
int map[N][N];

int solve()
{ int sum;
    for(int i=0;i<4;i++)
     {
         sum=0;
         for(int j=0;j<4;j++)
          sum+=map[i][j];
          if(sum==4||sum==8)return 1;
          else if(sum==40||sum==35)return 3;
     }
     for(int i=0;i<4;i++)
     {
         sum=0;
         for(int j=0;j<4;j++)
          sum+=map[j][i];
         if(sum==4||sum==8)return 1;
          else if(sum==40||sum==35)return 3;
     }
     sum=0;
     sum=map[0][0]+map[1][1]+map[2][2]+map[3][3];
    if(sum==4||sum==8)return 1;
          else if(sum==40||sum==35)return 3;
          sum=0;
     sum=map[0][3]+map[1][2]+map[2][1]+map[3][0];
     if(sum==4||sum==8)return 1;
          else if(sum==40||sum==35)return 3;
   for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
     if(map[i][j]==0)return 2;//Ã´ÓÐ½áÊø
     return 0;
}
int main()
{
   // freopen("in.txt","r",stdin);
     //freopen("out.txt","w",stdout);
    int T,test=1;
    char c;

    cin>>T;
    while(T--)
    {
       for(int i=0;i<4;i++)
      {
       for(int j=0;j<4;j++)
        {

            cin>>c;

            if(c=='.')
            map[i][j]=0;
            else if(c=='X')
            map[i][j]=1;
            else if(c=='O')
            map[i][j]=10;
             else if(c=='T')
             map[i][j]=5;

        }

      }

      int flag=solve();
      if(flag==1)
      printf("Case #%d: X won\n",test++);
      else if(flag==3)
       printf("Case #%d: O won\n",test++);
       else if(flag==2)
       printf("Case #%d: Game has not completed\n",test++);
        else if(flag==0)
         printf("Case #%d: Draw\n",test++);

    }
    return 0;
}
