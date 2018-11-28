#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;
int p1,p2,cases;
bool isE=false, player1,player2;     // if the games is not done
char winner1, board[4][4];        // saves the winner's character

bool lines(char player, int x, int y)
{
    board[x][y]=player;
    for(int i=0; i<4; i++)
    {
        if(board[i][0]==player && board[i][1]==player && board[i][2]==player && board[i][3]==player)
            return true;
    }
    for(int i=0; i<4; i++)
    {
        if(board[0][i]==player && board[1][i]==player && board[2][i]==player && board[3][i]==player)
            return true;
    }
    if(board[0][0] == player && board[1][1] == player && board[2][2] == player && board[3][3] == player )
        return true;

    if(board[0][3] == player && board[1][2] == player && board[2][1] == player && board[3][0] == player )
        return true;

    return false; // no winner
}

bool check_empty()
{
    for(int i=0; i < 4; i++)
        for(int j=0; j<4 ; j++)
            if(board[i][j]=='.')
                return true;
    return false;
}
int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("tic.out");
    in >> cases;

    for(int k=0; k < cases; k++ )
    {
            for(int j=0; j < 4; j++)
                        for(int i=0; i < 4; i++)
                        {
                            in >> board[j][i];
                            if(board[j][i] == 'T')
                            {
                                p1=j;
                                p2=i;
                            }
                        }

            isE=check_empty();
            player1=lines('X',p1,p2);
            if(!player1)
                player2=lines('O',p1,p2);

            if(player1)
                out << "Case #" << k+1 << ": X won"<< endl;

            else if(player2)
                out << "Case #" << k+1 << ": O won"<< endl;

            else if((!isE) && !player1 && !player2)
                out << "Case #" << k+1 << ": Draw"<< endl;

            else out << "Case #" << k+1 << ": Game has not completed"<< endl;

    }
}
