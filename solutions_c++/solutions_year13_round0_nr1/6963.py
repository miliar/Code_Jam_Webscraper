#include <fstream>

using namespace std;

char a[4][4];

bool prov(int k, char s, char h)
{
    int m = 0;
    if (s == 'v')
        for (int i = 0; i < 4; ++i)
            if ((a[i][k] == h) || ((a[i][k] == 'T')))
                m++;

    if (s == 'g')
        for (int i = 0; i < 4; ++i)
            if ((a[k][i] == h) || ((a[k][i] == 'T')))
                m++;

    if (s == 'i')
        for (int i = 0; i < 4; ++i)
            if ((a[i][i] == h) || ((a[i][i] == 'T')))
                m++;

    if (s == 'j')
        for (int i = 0; i < 4; ++i)
            if ((a[i][3 - i] == h) || ((a[i][3 - i] == 'T')))
                m++;
    return m == 4;
}

int main()
{   ifstream cin("input.in");
    ofstream cout( "output.txt");
    int t;
    cin >> t;
    bool exit;
    int kol;
    for (int i = 0; i < t; ++i)
    {
        kol = 0;
        exit = false;
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
            {
                cin >> a[j][k];
                if ((a[j][k] == 'O') || (a[j][k] == 'X') || (a[j][k] == 'T'))
                    kol++;
            }
        for (int j = 0; j < 4; ++j)
        {
            if (prov(j, 'v', 'O') && !exit)
            {
                cout << "Case #" << i + 1 << ": O won" << endl;
                exit = true;
                break;
            }
            if (prov(j, 'v', 'X')&& !exit)
            {
                cout << "Case #" << i + 1 << ": X won" << endl;
                exit = true;
                break;
            }
        }
        for (int j = 0; j < 4; ++j)
        {
            if (prov(j, 'g', 'O')&& !exit)
            {
                cout << "Case #" << i + 1 << ": O won" << endl;
                exit = true;
                break;
            }
            if (prov(j, 'g','X')&& !exit)
            {
                cout << "Case #" << i + 1 << ": X won" << endl;
                exit = true;
                break;
            }
        }
       if (prov(0, 'i', 'O')&& !exit)
            {
                cout << "Case #" << i + 1 << ": O won" << endl;
                exit = true;
            }
        if (prov(0, 'j', 'O')&& !exit)
            {
                cout << "Case #" << i + 1 << ": O won" << endl;
                exit = true;
            }
        if (prov(0, 'i', 'X')&& !exit)
            {
                cout << "Case #" << i + 1 << ": X won" << endl;
                exit = true;
            }
        if (prov(0, 'j', 'X')&& !exit)
            {
                cout << "Case #" << i + 1 << ": X won" << endl;
                exit = true;
            }
        if (!exit && (kol == 16))
            cout << "Case #" << i + 1 << ": Draw" << endl;

        if (!exit && (kol != 16))
            cout << "Case #" << i + 1 << ": Game has not completed" << endl;
    }
}
