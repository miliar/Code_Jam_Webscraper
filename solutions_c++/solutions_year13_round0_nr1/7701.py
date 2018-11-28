#include <iostream>
#include <cstdio>
#include <string>
#include <fstream>

using namespace std;

struct Board
{
    char table[4][4];
};

void checkBoard(Board &board, int caseNum,  ofstream &myfile)
{
    bool finished = false, dotFound = false;
    char c;
    int i = 0, j = 0;

    while(i < 4 && !finished)
    {
        if(board.table[i][0] != '.' && board.table[i][1] != '.')
        {
            c = board.table[i][0];
            if(c == 'T')
                c = board.table[i][1];

            finished = true;

            for(j = 0 ; j < 4 ; j++)
            {
                finished = finished && (board.table[i][j] == c || board.table[i][j] == 'T');
                dotFound = dotFound || board.table[i][j] == '.';
            }
        }
        else dotFound = true;

        i++;
    }

    if(finished)
    {
        myfile << "Case #" << caseNum << ": " << c << " won\n";
        return;
    }

    j = 0;
    finished = false;

    while(j < 4 && !finished)
    {
        if(board.table[0][j] != '.' && board.table[1][j] != '.')
        {
            c = board.table[0][j];
            if(c == 'T')
                c = board.table[1][j];

            finished = true;

            for(i = 0 ; i < 4 ; i++)
            {
                finished = finished && (board.table[i][j] == c || board.table[i][j] == 'T');
                dotFound = dotFound || board.table[i][j] == '.';
            }
        }
        else dotFound = true;

        j++;
    }

    if(finished)
    {
        myfile << "Case #" << caseNum << ": " << c << " won\n";
        return;
    }

    if(board.table[0][0] != '.' && board.table[1][1] != '.')
    {
        i = j = 0;
        finished = true;

        c = board.table[0][0];
        if(c == 'T')
            c = board.table[1][1];

        for(i = 0 ; i < 4 ; i++)
            finished = finished && (board.table[i][i] == c || board.table[i][i] == 'T');

        if(finished)
        {
            myfile << "Case #" << caseNum << ": " << c << " won\n";
            return;
        }
    }

    if(board.table[3][0] != '.' && board.table[2][1] != '.')
    {
        i = j = 0;
        finished = true;

        c = board.table[3][0];
        if(c == 'T')
            c = board.table[2][1];

        for(i = 0 ; i < 4 ; i++)
            finished = finished && (board.table[3-i][i] == c || board.table[3-i][i] == 'T');
    }

    if(finished)
        myfile << "Case #" << caseNum << ": " << c << " won\n";

    else if(dotFound)
        myfile << "Case #" << caseNum << ": Game has not completed\n";

    else myfile << "Case #" << caseNum << ": Draw\n";



}

int main()
{
    ofstream myfile;
    myfile.open ("output.txt");

    int testCases = 0;
    cin >> testCases;

    Board boards[testCases];

    for(int boardnum = 0 ; boardnum < testCases ; boardnum++)
    {
        for(int i = 0 ; i < 4 ; i++)
        {
            for(int j = 0 ; j < 4 ; j++)
            {
                cin >> boards[boardnum].table[i][j];
            }
        }
        cin.ignore();
    }

    for(int boardNum = 0 ; boardNum < testCases ; boardNum++)
        checkBoard(boards[boardNum], boardNum+1, myfile);

    myfile.close();


    return 0;
}

