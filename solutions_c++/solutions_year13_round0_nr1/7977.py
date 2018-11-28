#include <iostream>
#include <fstream>
#include <cstdlib>
#include <map>
#include <vector>
#include <stack>

using namespace std;

int game_status(string board);
bool check_str(string s, char side);

/*
 * Checks the board to see if someone has won.
 * Returns 1 if X wins
 * Returns 0 if draw
 * Returns -1 if O wins
 * Returns -2 if not finished
 */
int game_status(string board)
{
    // Check horizontal rows
    unsigned int r, c;
    string s;
    for (r = 0; r < 4; r++)
    {
        s = "";
        for (c = 0; c < 4; c++)
            s.push_back(board[4 * r + c]);

        if (check_str(s, 'X'))
            return 1;
        else if (check_str(s, 'O'))
            return -1;
    }

    // Check vertical rows
    for (c = 0; c < 4; c++)
    {
        s = "";
        for (r = 0; r < 4; r++)
            s.push_back(board[4 * r + c]);

        if (check_str(s, 'X'))
            return 1;
        else if (check_str(s, 'O'))
            return -1;
    }

    // Check diagonals
    unsigned i;
    s = "";
    for (i = 0; i < 4; i++)
    {
        s.push_back(board[4 * i + i]);
    }
    if (check_str(s, 'X'))
        return 1;
    else if (check_str(s, 'O'))
        return -1;

    s = "";
    for (i = 0; i < 4; i++)
    {
        c = 3 - i;
        s.push_back(board[4 * i + c]);
    }

    if (check_str(s, 'X'))
        return 1;

    else if (check_str(s, 'O'))
        return -1;

    // No winner
    for (i = 0; i < s.length(); i++)
    {
        // Not finished
        if (board[i] == '.')
            return -2;
    }
    return 0;
}

bool check_str(string s, char side)
{
    unsigned int i;

    for (i = 0; i < s.length(); i++)
    {
        if (s[i] != side && s[i] != 'T')
            return false;
    }
    return true;
}

int main(int argc, char *argv[])
{
    vector<string> lines;

    ifstream infile;
    ofstream outfile;

    infile.open(argv[1], fstream::in);
    outfile.open("tictactoe.out", fstream::out);

    int t; // Number of test cases
    infile >> t;

    string s;

    // Get input
    while (infile >> s)
        lines.push_back(s);

    // Process input
    int i, j, result;
    string outcome;
    for (i = 0; i < t; i++)
    {
        j = 4 * i;
        s = lines[j] + lines[j + 1] + lines[j + 2] + lines[j + 3];
        
        result = game_status(s);

        // Get the result string
        switch (result)
        {
            case 1:
                outcome = "X won";
                break;
            case 0:
                outcome = "Draw";
                break;
            case -1:
                outcome = "O won";
                break;
            case -2:
                outcome = "Game has not completed";
                break;
        }

        outfile << "Case #" << i + 1 << ": " << outcome;
        if (i != t - 1)
            outfile << '\n';
    }

    infile.close();
    outfile.close();
    return 0;
}
