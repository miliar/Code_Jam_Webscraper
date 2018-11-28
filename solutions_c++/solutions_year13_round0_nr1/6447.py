#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char * argv[])
{
    int n;
    ifstream in;
    in.open(argv[1]);
    in >> n;
    ofstream out;
    out.open(argv[2]);
    for (int k = 0; k < n; k++)
    {
        string s[4];
        for (int i = 0; i < 4; i++)
            in >> s[i];
        out << "Case #" << k + 1 << ": ";
        bool winO = false;
        bool winX = false;
        for (int i = 0; i < 4; i++)
        {
            int countX = 0;
            int countO = 0;
            int countT = 0;
            for (int j = 0; j < 4; j++)
            {
                if (s[i][j] == 'T')
                    countT++;
                if (s[i][j] == 'X')
                    countX++;
                if (s[i][j] == 'O')
                    countO++;
            }
            if (countX == 4 || ((countX == 3) && countT == 1))
                winX = true;
            if (countO == 4 || ((countO == 3) && countT == 1))
                winO = true;
        }
        for (int i = 0; i < 4; i++)
        {
            int countX = 0;
            int countO = 0;
            int countT = 0;
            for (int j = 0; j < 4; j++)
            {
                if (s[j][i] == 'T')
                    countT++;
                if (s[j][i] == 'X')
                    countX++;
                if (s[j][i] == 'O')
                    countO++;
            }
            if (countX == 4 || ((countX == 3) && countT == 1))
                winX = true;
            if (countO == 4 || ((countO == 3) && countT == 1))
                winO = true;
        }

        int countX = 0;
        int countO = 0;
        int countT = 0;
        for (int i = 0; i < 4; i++)
        {
            if (s[i][i] == 'T')
                countT++;
            if (s[i][i] == 'X')
                countX++;
            if (s[i][i] == 'O')
                countO++;
        }
        if (countX == 4 || ((countX == 3) && countT == 1))
            winX = true;
        if (countO == 4 || ((countO == 3) && countT == 1))
            winO = true;

        countX = 0;
        countO = 0;
        countT = 0;
        for (int i = 0; i < 4; i++)
        {
            if (s[i][3 - i] == 'T')
                countT++;
            if (s[i][3 - i] == 'X')
                countX++;
            if (s[i][3 - i] == 'O')
                countO++;
        }
        if (countX == 4 || ((countX == 3) && countT == 1))
            winX = true;
        if (countO == 4 || ((countO == 3) && countT == 1))
            winO = true;
        bool incompleted = false;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (s[i][j] == '.')
                    incompleted = true;
        if (winX)
            out << "X won" << endl;
        else
            if (winO)
                out << "O won" << endl;
            else
                if (incompleted)
                    out << "Game has not completed" << endl;
                else
                    out << "Draw" << endl;
    }
    return 0;
}
