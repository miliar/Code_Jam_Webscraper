#include <iostream>
#include <fstream>

using namespace std;

bool winning_col(char t, int j, char grid[][4])
{
    for(int i = 0; i < 4; i++)
    {
        if(grid[i][j] != t && grid[i][j] != 'T')
            return false;
    }
    return true;
}

bool winning_row(char t, int i, char grid[][4])
{
    for(int j = 0; j < 4; j++)
    {
        if(grid[i][j] != t && grid[i][j] != 'T')
            return false;
    }
    return true;
}

bool winning_diag(char t, char grid[][4])
{
    int i = 0;
    for(; i < 4; i++)
    {
        if(grid[i][i] != t && grid[i][i] != 'T')
            break;
    }
    if(i == 4)
        return true;
    i = 0;
    for(; i < 4; i++)
    {
        if(grid[i][3-i] != t && grid[i][3-i] != 'T')
            break;
    }
    if(i == 4)
        return true;

    return false;
}


void solve(char grid[][4], fstream &sortie)
{
    if(winning_diag('X', grid))
    {
        sortie << "X won" << endl;
        return;
    }
    for(int i = 0; i < 4; i++)
    {
        if(winning_col('X', i, grid) || winning_row('X', i, grid))
        {
            sortie << "X won" << endl;
            return;
        }
    }

    if(winning_diag('O', grid))
    {
        sortie << "O won" << endl;
        return;
    }
    for(int i = 0; i < 4; i++)
    {
        if(winning_col('O', i, grid) || winning_row('O', i, grid))
        {
            sortie << "O won" << endl;
            return;
        }
    }

    for(int i = 0; i < 4; i++)
    for(int j = 0; j < 4; j++)
    {
        if(grid[i][j] == '.')
        {
            sortie << "Game has not completed" << endl;
            return;
        }
    }

    sortie << "Draw" << endl;
}


int main(int argc, char *argv[])
{
    char grid[4][4];

    int t;

    fstream file("fichier.txt");
    fstream sortie("sortie.txt", ios::out);

    file >> t;
    for(int i = 0; i < t; i++)
    {
        for(int j = 0; j < 4; j++)
            for(int k = 0; k < 4;k++)
                file >> grid[j][k];

        sortie << "Case #" << i+1 << ": ";
        solve(grid, sortie);
    }
}
