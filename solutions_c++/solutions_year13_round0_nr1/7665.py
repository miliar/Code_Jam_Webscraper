#include<iostream>
using namespace std;
char a[5][5];
int main()
{    freopen("hehe.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int cas;

    for(cas=0;cas<t;cas++)
    {
       for(int i=0;i<4;i++)
       {
          scanf("%s",a[i]);
          }
       int flag=0;
       printf("Case #%d: ",cas+1);
       for(int i=0;i<4;i++)
       {int j;          
       for(j=0;j<4;j++)
         if(a[i][j]=='.')
               flag=1;
          for(j=0;j<4;j++)
          {//printf("%c\n",a[i][j]);             

             if(a[i][j]!='X'&&a[i][j]!='T')
               break;

          }
          if(j==4)
          {
             printf("X won");        
             goto chasingdream;
          }
          for( j=0;j<4;j++)
          {
             if(a[j][i]!='X'&&a[j][i]!='T')
               break;
          }
          if(j==4)
          {
             printf("X won");        
             goto chasingdream;
          }
          for( j=0;j<4;j++)
          {
             if(a[i][j]!='O'&&a[i][j]!='T')
               break;
          }
          if(j==4)
          {
             printf("O won");        
             goto chasingdream;
          }
          for(j=0;j<4;j++)
          {
             if(a[j][i]!='O'&&a[j][i]!='T')
               break;
          }
          if(j==4)
          {
             printf("O won");        
             goto chasingdream;
          }
          if((a[0][0]=='X'||a[0][0]=='T')&&(a[1][1]=='X'||a[1][1]=='T')
          &&(a[2][2]=='X'||a[2][2]=='T')&&(a[3][3]=='X'||a[3][3]=='T')
          ||(a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')
          &&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T'))
          {
             printf("X won");
             goto chasingdream;
             }
          if((a[0][0]=='O'||a[0][0]=='T')&&(a[1][1]=='O'||a[1][1]=='T')
          &&(a[2][2]=='O'||a[2][2]=='T')&&(a[3][3]=='O'||a[3][3]=='T')
          ||(a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')
          &&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T'))
            {
               printf("O won");
               goto chasingdream;
            }
       }
       if(flag==1)
          printf("Game has not completed");
       else
          printf("Draw");
chasingdream :
             cout<<endl;
        }
        return 0;
}
          
