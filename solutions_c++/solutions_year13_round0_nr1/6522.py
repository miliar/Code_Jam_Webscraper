// Problem 1
#include<stdio.h>
void solve();
int main(void)
{
    int T,t;
    freopen("l_input.in","r",stdin);
    freopen("l_output.txt","w",stdout);

    scanf("%d",&T);
    for(t=1;t<=T;t++)
     {
       printf("Case #%d: ",t);
       solve();
       printf("\n");
     }
    return 0;
}
void solve()
{
     char board[5][5];
     int i,j,no_X,no_O,no_T,no_dot,dots=0;
     for(i=0;i<4;i++)
       scanf("%s",board[i]);
     for(i=0;i<4;i++)
     {
        no_X=0,no_O=0,no_T=0,no_dot=0;
        for(j=0;j<4;j++)
        {
          switch(board[i][j])
          {
           case 'T':
                no_T++;
           break;
           case 'O':
                no_O++;
           break;
           case 'X':
                no_X++;
           break;
           case '.':
                no_dot++;
           break;
          } 
         }  
         if(no_O+no_T==4)
         {
          printf("O won");
          return;
         }
         if(no_X+no_T==4)
         {
          printf("X won");
          return;
         }
         dots+=no_dot;
        }
        
     for(j=0;j<4;j++)
     {
        no_X=0,no_O=0,no_T=0,no_dot=0;
        for(i=0;i<4;i++)
        {
          switch(board[i][j])
          {
           case 'T':
                no_T++;
           break;
           case 'O':
                no_O++;
           break;
           case 'X':
                no_X++;
           break;
           case '.':
                no_dot++;
           break;
          } 
         }  
         if(no_O+no_T==4)
         {
          printf("O won");
          return;
         }
         if(no_X+no_T==4)
         {
          printf("X won");
          return;
         }
        }
     no_X=0,no_O=0,no_T=0;
     for(i=0;i<4;i++)
     {
      switch(board[i][i])
          {
           case 'T':
                no_T++;
           break;
           case 'O':
                no_O++;
           break;
           case 'X':
                no_X++;
           break;
           case '.':
                no_dot++;
           break;
          }
     }
     if(no_O+no_T==4)
         {
          printf("O won");
          return;
         }
         if(no_X+no_T==4)
         {
          printf("X won");
          return;
         }
     no_X=0,no_O=0,no_T=0;
     for(i=3;i>=0;i--)
     {
      switch(board[i][3-i])
          {
           case 'T':
                no_T++;
           break;
           case 'O':
                no_O++;
           break;
           case 'X':
                no_X++;
           break;
           case '.':
                no_dot++;
           break;
          }
     }
     if(no_O+no_T==4)
         {
          printf("O won");
          return;
         }
         if(no_X+no_T==4)
         {
          printf("X won");
          return;
         }
     if(!dots)
          printf("Draw");
     else
          printf("Game has not completed");     
}
