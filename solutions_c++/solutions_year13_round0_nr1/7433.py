#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
    int t,i,j,te;
    char board[5][5],in[5][5];
    scanf("%d",&t);
    for(te=1;te<=t;te++)
    {
       int empty=0,done=0;
       for(j=1;j<=4;j++)
       scanf("%s",in[j]);
       printf("Case #%d: ",te);
       for(i=1;i<=4;i++)
       {
         for(j=1;j<=4;j++)
         {
           board[i][j]=in[i][j-1];
         }
       }
       
       if(empty==1)
       {
          printf("Game has not completed\n");
       }
       else
       {
           int x=0,o=0;
           for(i=1;i<=4;i++)
           {x=0;o=0;
             for(j=1;j<=4;j++)
             {
               if(board[i][j]=='X'||board[i][j]=='T')
               {
                  x++;
               }
               if(board[i][j]=='O'||board[i][j]=='T')
               {
                  o++;
               }
             }
             if(x==4||o==4){done=1;break;}
           }
           if(!done)
           {
             for(i=1;i<=4;i++)
             {x=0;o=0;
             for(j=1;j<=4;j++)
             {
               if(board[j][i]=='X'||board[j][i]=='T')
               {
                  x++;
               }
               if(board[j][i]=='O'||board[j][i]=='T')
               {
                  o++;
               }
             }
             if(x==4||o==4){done=1;break;}
             }
           }
           if(!done)
           {x=0;o=0;
                for(i=1;i<=4;i++)
                {
                   if(board[i][i]=='X'||board[i][i]=='T')
                   x++; 
                   if(board[i][i]=='O'||board[i][i]=='T')
                   o++;
                }
                if(x==4||o==4)done=1;
                if(!done)
                {
                   x=0;o=0;
                for(i=4,j=1;i>=1,j<=4;i--,j++)
                {
                   if(board[j][i]=='X'||board[j][i]=='T')
                   x++; 
                   if(board[j][i]=='O'||board[j][i]=='T')
                   o++;
                }
                }     
           }
           if(x==4)
           printf("X won\n");
           else if(o==4)
           printf("O won\n");
           else
           {
               for(i=1;i<=4;i++)
               for(j=1;j<=4;j++)
               {       
                       if(board[i][j]=='.')
                       {
                        empty=1;
                       }
               }
               if(empty)printf("Game has not completed\n");
               else
               printf("Draw\n");
           }
       } 
    }
    //system("pause");
    return 0;
}
   
