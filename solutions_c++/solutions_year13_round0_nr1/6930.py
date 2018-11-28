#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
 
using namespace std;
 
char board[4][4];
bool full;
 
bool judge (char c, int x, int y)
{
        int check = 0;
        for(int col = 0 ; col < 4 ; col++)
        {
                if(board[x][col] == 'T' || board[x][col] == c) check++;
        }
 
        if(check == 4) return true;
 
        check = 0;
        for(int row = 0 ; row < 4 ; row++)
        {
                if(board[row][y] == 'T' || board[row][y] == c) check++;
        }
 
        if(check == 4) return true;
 
        check = 0;
 
        if(x+y == 3)
        {
                for(int i = 0 ; i < 4 ; i++)
                {
                        for(int j = 0 ; j < 4 ; j++)
                        {
                                if(i+j == 3)
                                {
                                        if(board[i][j] == 'T' || board[i][j] == c) check++;
                                }
                        }
                }
                if(check == 4) return true;
                check = 0;
        }
 
        if(x == y)
        {
                for(int i = 0 ; i < 4 ; i++)
                {
                        for(int j = 0 ; j < 4 ; j++)
                        {
                                if(!(i-j))
                                {
                                        if(board[i][j] == 'T' || board[i][j] == c) check++;
                                }
                        }
                }
                if(check == 4) return true;
                check = 0;
        }
        return false;
}
 
int main()
{
        int test, count = 1;
        scanf("%d", &test);
        while(test--)
        {
                //memset(board, 0, sizeof(board));
                board[0][0] = sizeof(board);
                for(int i = 0 ; i < 4 ; i++)
                {
                        scanf("%s", board[i]);
                }
 
                string winner = "Draw";
                full = true;
               
                for(int i = 0 ; i < 4 ; i++)
                {
                        for(int j = 0 ; j < 4 ; j++)
                        {
                                if(board[i][j] == '.') full = false;
                                else if(board[i][j] == 'X' || board[i][j] == 'O')
                                {
                                        bool iswin = judge(board[i][j], i, j);
                                        if(iswin)
                                        {
                                                winner = "";
                                                winner += board[i][j];
                                                break;
                                        }
                                }
                        }
                }
 
                printf("Case #%d: ", count++);
 
                if(winner == "X" || winner == "O") printf("%s won\n", winner.c_str());
                else if(winner == "Draw")
                {
                        if(full) puts("Draw");
                        else puts("Game has not completed");
                }
        }
        return 0;
}