#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

char checkLine(string line[])
{
    for (int i = 0; i < 4; i++)
    {
        if (
            (line[i][0] == 'X' || line[i][0] == 'T') &&
            (line[i][1] == 'X' || line[i][1] == 'T') &&
            (line[i][2] == 'X' || line[i][2] == 'T') &&
            (line[i][3] == 'X' || line[i][3] == 'T')
        )
        {
            return 'X';
        }

        if (
            (line[i][0] == 'O' || line[i][0] == 'T') &&
            (line[i][1] == 'O' || line[i][1] == 'T') &&
            (line[i][2] == 'O' || line[i][2] == 'T') &&
            (line[i][3] == 'O' || line[i][3] == 'T')
        )
        {
            return 'O';
        }
    }

    return '0';
}

char checkCol(string col[])
{
    for (int i = 0; i < 4; i++)
    {
        if (
            (col[0][i] == 'X' || col[0][i] == 'T') &&
            (col[1][i] == 'X' || col[1][i] == 'T') &&
            (col[2][i] == 'X' || col[2][i] == 'T') &&
            (col[3][i] == 'X' || col[3][i] == 'T')
        )
        {
            return 'X';
        }
        else if (
            (col[0][i] == 'O' || col[0][i] == 'T') &&
            (col[1][i] == 'O' || col[1][i] == 'T') &&
            (col[2][i] == 'O' || col[2][i] == 'T') &&
            (col[3][i] == 'O' || col[3][i] == 'T')
        )
        {
            return 'O';
        }
        else
        {
            return '0';
        }
    }
}

char checkIstr(string col[])
{
    if (
        (
            (col[0][0] == 'X' || col[0][0] == 'T') &&
            (col[1][1] == 'X' || col[1][1] == 'T') &&
            (col[2][2] == 'X' || col[2][2] == 'T') &&
            (col[3][3] == 'X' || col[3][3] == 'T')
        ) ||
        (
            (col[0][3] == 'X' || col[0][3] == 'T') &&
            (col[1][2] == 'X' || col[1][2] == 'T') &&
            (col[2][1] == 'X' || col[2][1] == 'T') &&
            (col[3][0] == 'X' || col[3][0] == 'T')
        )
    )
    {
        return 'X';
    }
    else if (
        (
            (col[0][0] == 'O' || col[0][0] == 'T') &&
            (col[1][1] == 'O' || col[1][1] == 'T') &&
            (col[2][2] == 'O' || col[2][2] == 'T') &&
            (col[3][3] == 'O' || col[3][3] == 'T')
        ) ||
        (
            (col[0][3] == 'O' || col[0][3] == 'T') &&
            (col[1][2] == 'O' || col[1][2] == 'T') &&
            (col[2][1] == 'O' || col[2][1] == 'T') &&
            (col[3][0] == 'O' || col[3][0] == 'T')
        )
    )
    {
        return 'O';
    }
    else
    {
        return '0';
    }
}

bool checkDots(string col[])
{
    for (int i = 0; i < 4; i++)
    {
        if (
            (col[0][i] == '.') ||
            (col[1][i] == '.') ||
            (col[2][i] == '.') ||
            (col[3][i] == '.')
        )
        {
            return true;
        }
    }
}

int main()
{
    ifstream failas("in.txt");
    ofstream file("A-small-attempt0.out");

    int cases;
    string temp;

    failas >> cases;

    string lines[cases][4];

    for (int i = 0; i < cases; i++)
    {
        for (int x=0; x<4; x++)
        {
            failas >> lines[i][x];
        }
    }

    for (int i = 0; i < cases; i++)
    {
        file << "Case #" << (i + 1) << ": ";
        string result;
        stringstream ss;

        if (checkLine(lines[i]) != '0')
        {
            ss << checkLine(lines[i]);
            ss >> result;
            result += " won";
        }
        else if (checkCol(lines[i]) != '0')
        {
            ss << checkCol(lines[i]);
            ss >> result;
            result += " won";
        }
        else if (checkIstr(lines[i]) != '0')
        {
            ss << checkIstr(lines[i]);
            ss >> result;
            result += " won";
        }
        else if (checkDots(lines[i]) == true)
        {
            result = "Game has not completed";
        }

        if (result == "")
            result = "Draw";

        file << result << endl;
    }

    return 0;
}
