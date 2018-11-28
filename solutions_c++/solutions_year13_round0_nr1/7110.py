#include <iostream>
#include <vector>
#include <fstream>

using namespace std;


char getTile(int x, int y, vector<string>& tab)
{
    if(x<0 || y<0 || x>3 || y>3)
        return ' ';
    return tab[y][x];
}

char wonLine(int y, vector<string>& tab)
{
    char cc = getTile(0, y, tab);
    for(int i=0 ; i<4 ; i++)
    {
        char c = getTile(i, y, tab);
        if(cc == 'T')
            cc = c;

        if(cc != c && c != 'T')
            return ' ';
    }

    return cc;
}

char wonCol(int x, vector<string>& tab)
{
    char cc = getTile(x, 0, tab);
    for(int i=0 ; i<4 ; i++)
    {
        char c = getTile(x, i, tab);
        if(cc == 'T')
            cc = c;

        if(cc != c && c != 'T')
            return ' ';
    }

    return cc;
}

char wonDiagonal1(vector<string>& tab)
{
    char cc = getTile(0, 0, tab);
    for(int i=0 ; i<4 ; i++)
    {
        char c = getTile(i, i, tab);
        if(cc == 'T')
            cc = c;

        if(cc != c && c != 'T')
            return ' ';
    }

    return cc;
}

char wonDiagonal2(vector<string>& tab)
{
    char cc = getTile(3, 0, tab);
    for(int i=0 ; i<4 ; i++)
    {
        char c = getTile(4-1-i, i, tab);
        if(cc == 'T')
            cc = c;

        if(cc != c && c != 'T')
            return ' ';
    }

    return cc;
}



string gameState(vector<string>& tab)
{
    //test if any player won
    for(int i=0 ; i<4 ; i++)
    {
        char wonL = wonLine(i, tab);
        char wonC = wonCol(i, tab);
        if(wonC == 'X' || wonL == 'X')
            return "X won";
        if(wonC == 'O' || wonL == 'O')
            return "O won";
    }

    char wonD1 = wonDiagonal1(tab);
    char wonD2 = wonDiagonal2(tab);
    if(wonD1 == 'X' || wonD2 == 'X')
        return "X won";
    if(wonD1 == 'O' || wonD2 == 'O')
        return "O won";


    //if not, check if game ended or not
    for(int i=0 ; i<4 ; i++)
        for(int j=0 ; j<4 ; j++)
            if(getTile(i, j, tab) == '.')
                return "Game has not completed";

    return "Draw";
}


int main()
{
    ifstream file("in.txt", ios::in);
    ofstream fileOut("out.txt", ios::out | ios::trunc);

    int nb;
    file >> nb;

    for(int n=0 ; n<nb ; n++)
    {
        vector<string> tab(4, "");

        for(int i=0 ; i<4 ; i++)
        {
            string s = "";
            for(int j=0 ; j<4 ; j++)
            {
                char c;
                file >> c;
                s += c;
            }
            tab[i] = s;
        }

        fileOut << "Case #" << n+1 << ": " << gameState(tab) << endl;
    }

    fileOut.close();
    file.close();

    return 0;
}
