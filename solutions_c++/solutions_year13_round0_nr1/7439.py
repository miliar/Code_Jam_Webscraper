#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int over(vector <int> x, vector <int> o)
{
    //colum
    for (int i = 0 ; i < 4 ; i++)
    {
        if (x[i] == x[i+4] && x[i] == x[i+8] && x[i] == x[i+12] && x[i] == 1)
            return 1;
        if (o[i] == o[i+4] && o[i] == o[i+8] && o[i] == o[i+12] && o[i] == 1)
            return 2;
    }
    //row
    for (int i = 0 ; i <= 12 ; i += 4)
    {
        if (x[i] == x[i+1] && x[i] == x[i+2] && x[i] == x[i+3] && x[i] == 1)
            return 1;
        if (o[i] == o[i+1] && o[i] == o[i+2] && o[i] == o[i+3] && o[i] == 1)
            return 2;
    }
    if (x[0] == x[5] && x[0] == x[10] && x[0] == x[15] && x[0] == 1)
        return 1;
    if (o[0] == o[5] && o[0] == o[10] && o[0] == o[15] && o[0] == 1)
        return 2;
    if (x[3] == x[6] && x[3] == x[9] && x[9] == x[12] && x[3] == 1)
        return 1;
    if (o[3] == o[6] && o[3] == o[9] && o[9] == o[12] && o[3] == 1)
        return 2;
    return 0;
}

int main()
{
    ios_base::sync_with_stdio(false);

    int t;
    char in;
    int check;

    cin >> t;

    for (int i = 0 ; i < t ; i++)
    {
        bool draw = true;
        vector<int> x(16);
        vector<int> o(16);

        for (int j = 0 ; j < 16 ; j++)
        {
            cin >> in;

            if (in == 'X')
                x[j] = 1;
            else if (in == 'O')
                o[j] = 1;
            else if (in == 'T')
            {
                x[j] = 1;
                o[j] = 1;
            }
            else 
            {
                draw = false;
            }
        }

        check = over(x, o);
        cout << "Case #" << i+1 << ": ";
        if (check == 1)
            cout << "X won" << endl;
        else if (check == 2)
            cout << "O won" << endl;
        else if (draw)
            cout << "Draw" << endl;
        else
            cout << "Game has not completed" << endl;
    }

    exit(EXIT_SUCCESS);
}
