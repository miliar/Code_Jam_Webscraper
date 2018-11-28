#include <iostream>
#include <fstream>
#include <locale>
#include <cmath>
using namespace std;

bool won(char b[4][4], char p)
{
    int i, j, k;

    //Rows
    for(i=0;i<4;i++)
    {
        if(((b[0][i] == p)||(b[0][i] == 'T'))&&((b[1][i] == p)||(b[1][i] == 'T'))&&((b[2][i] == p)||(b[2][i] == 'T'))&&((b[3][i] == p)||(b[3][i] == 'T')))
            return true;
    }

    //Cols
    for(i=0;i<4;i++)
    {
        if(((b[i][0] == p)||(b[i][0] == 'T'))&&((b[i][1] == p)||(b[i][1] == 'T'))&&((b[i][2] == p)||(b[i][2] == 'T'))&&((b[i][3] == p)||(b[i][3] == 'T')))
            return true;
    }

    //Diaganol
    if(((b[0][0] == p)||(b[0][0] == 'T'))&&((b[1][1] == p)||(b[1][1] == 'T'))&&((b[2][2] == p)||(b[2][2] == 'T'))&&((b[3][3] == p)||(b[3][3] == 'T')))
            return true;

    if(((b[3][0] == p)||(b[3][0] == 'T'))&&((b[2][1] == p)||(b[2][1] == 'T'))&&((b[1][2] == p)||(b[1][2] == 'T'))&&((b[0][3] == p)||(b[0][3] == 'T')))
            return true;

    //Else
    return false;
}

bool Draw(char b[4][4])
{
    int i, j;

    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(b[j][i] == '.')
            {
                return false;
            }
        }
    }

    return true;
}

int main()
{
    //Variables
    ifstream infile("T4.in");
    ofstream outfile("T4.out");
    int i, j, k;
    int n;
    char board[4][4];

    infile >> n;

    //For each case
    for(i=0;i<n;i++)
    {
        outfile << "Case #" << i+1 << ": ";

        //INPUT
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                infile >> board[j][k];
            }
        }

        //X won, O won, Draw, or Not finished
        if(won(board, 'X'))
            outfile << "X won";
        else if(won(board, 'O'))
            outfile << "O won";
        else if(Draw(board))
            outfile << "Draw";
        else
            outfile << "Game has not completed";

        outfile << endl;
    }

    return 0;
}
