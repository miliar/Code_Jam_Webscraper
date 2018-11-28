#include <iostream>
#include <cstdio>

using namespace std;
char grid[4][4];
bool gagne[2];
int nbPts;
inline bool checkeCol(char player, int lin, int col)
{
    int nbCool = 0;
    int nbT = 0;
    if (lin > 0)
        return false;
    for (int i = 0;i< 4 && (grid[i+lin][col] == player || grid[i+lin][col] == 'T'); i++)
    {
        if (grid[i+lin][col] == 'T')
            nbT++;
        else
            nbCool++;
    }
    return (nbT <= 1 && nbT+nbCool == 4);
}

inline bool checkeLin(char player, int lin, int col)
{
    int nbCool = 0;
    int nbT = 0;
    if (col > 0)
        return false;
    for (int i = 0; i< 4 && (grid[lin][i+col] == player || grid[lin][i+col] == 'T'); i++)
    {
        if (grid[lin][i+col] == 'T')
            nbT++;
        else
            nbCool++;
    }
    return (nbT <= 1 && nbT+nbCool == 4);
}

inline bool checkeDiag1(char player, int lin, int col)
{
    if (lin > 0 || col > 0)
        return false;
    int nbCool = 0;
    int nbT = 0;
    for (int i = 0; i< 4 && (grid[i+lin][i+col] == player || grid[i+lin][i+col] == 'T'); i++)
    {
        if (grid[i+lin][i+col] == 'T')
            nbT++;
        else
            nbCool++;
    }
    return (nbT <= 1 && nbT+nbCool == 4);
}

inline bool checkeDiag2(char player, int lin, int col)
{
    int nbCool = 0;
    int nbT = 0;
    if (lin > 0 || col < 3)
        return false;
    for (int i = 0; i< 4 && (grid[i+lin][col-i] == player || grid[i+lin][col-i] == 'T'); i++)
    {
        if (grid[lin+i][col-i] == 'T')
            nbT++;
        else
            nbCool++;
    }
    return (nbT <= 1 && nbT+nbCool == 4);
}



void algo(void)
{
    for (int lin = 0; lin < 4; lin++)
    {
        for (int col = 0; col < 4; col++)
        {
            if (grid[lin][col] == 'X')
                gagne[0] = gagne[0] || checkeCol('X', lin, col) || checkeLin('X', lin, col) || checkeDiag1('X', lin, col) || checkeDiag2('X', lin, col);
            else if (grid[lin][col] == 'O')
                gagne[1] = gagne[1] || checkeCol('O', lin, col) || checkeLin('O', lin, col) || checkeDiag1('O', lin, col) || checkeDiag2('O', lin, col);
            else if (grid[lin][col] == 'T')
            {
                gagne[1] = gagne[1] || checkeCol('O', lin, col) || checkeLin('O', lin, col) || checkeDiag1('O', lin, col) || checkeDiag2('O', lin, col);
                gagne[0] = gagne[0] || checkeCol('X', lin, col) || checkeLin('X', lin, col) || checkeDiag1('X', lin, col) || checkeDiag2('X', lin, col);
            }
            else
                nbPts++;

        }
    }
}




int main()
{
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int nbT;
    cin >> nbT;

    for (int t = 1; t <= nbT; t++)
    {
        for (int lin = 0; lin < 4; lin++)
            for (int col = 0; col < 4; col++)
                cin >> grid[lin][col];
        getchar();
        gagne[0] = false;
        gagne[1] = false;
        nbPts = 0;
        algo();

        cout << "Case #" << t << ": ";
        if (gagne[0])
            cout << "X won\n";


        else if (gagne[1])
            cout << "O won\n";
        else
        {
            if (nbPts > 0)
                cout << "Game has not completed\n";
            else
                cout << "Draw\n";
        }
    }



    return 0;
}
