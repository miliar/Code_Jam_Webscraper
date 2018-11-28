
/*

  //auther - DUDEJUIT ........ 
  // DATE -14/04/2013
  
  Problem A. Tic-Tac-Toe-Tomek
Confused? Read the quick-start guide.
Small input
10 points	Solve A-small
You may try multiple times, with penalties for wrong submissions.


Large input
20 points	You must solve the small input first.
You will have 8 minutes to solve 1 input file. (Judged after contest.)


Problem
Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.
After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.
Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are: 
•	"X won" (the game is over, and X won) 
•	"O won" (the game is over, and O won) 
•	"Draw" (the game is over, and it ended in a draw) 
•	"Game has not completed" (the game is not over yet) 
If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable.
Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.
Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.
Limits
The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.
Small dataset
1 = T = 10.
Large dataset
1 = T = 1000.
Sample

Input	
Output
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O	

****** YOUR OUTPUT SHOULD BE LIKE THIS ****************

Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won
Note
Although your browser might not render an empty line after the last test case in the sample input, in a real input file there would be one.


*/

#include<iostream>
using namespace std;

#include<stdio.h>
#include<string.h>
#include<math.h>
//#include<conio.h>
int cheack_empty(char board[4][4])
{
    int flag=0;
    for(int i=0;i<4;i++)
    {
            for(int j=0;j<4;j++)
            {
                    if(board[i][j]=='.')
                    {
                     flag=1;
                     break;
                    }
            }
            if(flag)
            break;
    }
    if(flag==1)
    return 5;
    return 6;
}
int cheack(char board[4][4],int r,int c)
{
    int ocount=0;
    int xcount=0;
    int tcount=0;
    if(r==0&&c==0)
    {
    for(int i=0;i<4;i++)
    {
            
            if(board[i][i]=='X')
                               xcount++;
            else
            {
                if(board[i][i]=='O')
                                   ocount++;
                else
                {
                                   if(board[i][i]=='T')
                                   tcount++;
                }
            }
    }
    }
    else
    {
        if(r==0&&c!=0)
        {
           
                      for(int i=0;i<4;i++)
                      {
                       if(board[i][c-1]=='X')
                               xcount++;
                       else
                       {
                           if(board[i][c-1]=='O')
                                   ocount++;
                           else
                           {
                                   if(board[i][c-1]=='T')
                                   tcount++;
                           }
                       }
                      }
        }
        else
        {
            if(r!=0 && c==0)
            {
                    
                      for(int J=0;J<4;J++)
                      {
                       if(board[r-1][J]=='X')
                       { 
      
                         xcount++;
                       }
                       else
                       {
                           if(board[r-1][J]!='.'&&board[r-1][J]=='O')
                           {
                                   ocount++;
                           }
                           else
                           {
                                   if(board[r-1][J]=='T')
                                   tcount++;
                           }
                       }
                      }
                     
            }
            else
            {
                if(r==1&&c==1)
                {
                              for(int i=0;i<4;i++)
                              {
            
                                      if(board[i][3-i]=='X')
                                                          xcount++;
                                      else
                                      {
                                          if(board[i][3-i]=='O')
                                          ocount++;
                                          else
                                          {
                                              if(board[i][3-i]=='T')
                                              tcount++;
                                          }
                                      }
                               }
                              
                }
            }
        }  
    }
    if(xcount==4||(xcount==3 && tcount==1))
    {
         
         return 1;
    }
    else
    {
        if(ocount==4||(ocount==3&&tcount==1))
        {
                                            return 2;
        }
        else
        {
            return -1;
        }
    }
        
    
}
int Solve_Problem(char board[4][4])
{
    
    int fd=cheack(board,0,0);
    if(fd==1||fd==2)
    return fd;
    fd=cheack(board,1,1);
    if(fd==1||fd==2)
    return fd;
    for(int i=1;i<5;i++)
    {
            if(board[i-1][0]=='.')
            continue ;
            fd=cheack(board,i,0);
            if(fd==1||fd==2)
            {
                          
            return fd;
            }
    }
    for(int i=1;i<5;i++)
    {
            if(board[0][i-1]=='.')
            continue ;
            fd=cheack(board,0,i);
            if(fd==1||fd==2)
            {
                        
            return fd;
            }
            
    }
    
    int c=cheack_empty(board);
    
    if(c==6)
    {
             return 4;
    }
    else
    {
        if(c==5)
        return 3;
    }
           
}
int main()
{
    int T;
    cin>>T;
    // x won 1 ,o won 2, not complete 3, drow 4
    int *gtable=new int[T];
    char board[4][4];
    char *rword=new char[4];
    for(int i=0;i<T;i++)
    {
            for(int m=0;m<4;m++)
            {
                    cin>>rword;
                    for(int n=0;n<4;n++)
                    {
                            
                            board[m][n]=rword[n];
                    }
            }
           
            gtable[i]=Solve_Problem(board);
    }
    for(int i=0;i<T;i++)
    {
            switch(gtable[i])
            {
                             case 1:
                                  cout<<"Case #"<<i+1<<": X won"<<endl;
                                  break;
                             case 2 : 
                                  cout<<"Case #"<<i+1<<": O won"<<endl;
                                  break;
                             case 3 :
                                  cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
                                  break;
                             case 4 :
                                  cout<<"Case #"<<i+1<<": Draw"<<endl;
                                  break;
                             default :
                                     cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
                                  break;
            }                     
    }
  //  getch();
    return 0;
}
