#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;
    cin.ignore(1000,'\n');
    for (int i = 1; i <= t; i++)
    {
        string s[4];
        int flag = 0;
        int cx[4],rx[4],dx[2],co[4],ro[4],dO[2],ct[4],rt[4],dt[2],d = 0;
        for (int j = 0; j < 4; j++)
        {
            getline(cin,s[j]);
            rx[j] = count(s[j].begin(),s[j].end(),'X');
            ro[j] = count(s[j].begin(),s[j].end(),'O');
            rt[j] = count(s[j].begin(),s[j].end(),'T');
            d += count(s[j].begin(),s[j].end(),'.');
        }

        cin.ignore(1000,'\n');
        for (int j = 0; j < 4; j++)
        {
            cx[j] = 0;
            co[j] = 0;
            ct[j] = 0;
            for (int k = 0; k < 4; k++)
            {
                if (s[k][j] == 'X')
                    cx[j]++;
                else if (s[k][j] == 'O')
                    co[j]++;
                else if (s[k][j] == 'T')
                    ct[j]++;
            }
        }

        int x = 0;
        dx[0] = 0;
        dO[0] = 0;
        dt[0] = 0;
        while (x < 4)
        {
            if (s[x][x] == 'X')
                dx[0]++;
            else if (s[x][x] == 'O')
                dO[0]++;
            else if (s[x][x] == 'T')
                dt[0]++;
            x++;
        }

        x = 3;
        int y = 0;
        dx[1] = 0;
        dO[1] = 0;
        dt[1] = 0;
        while (x >= 0)
        {
            if (s[x][y] == 'X')
                dx[1]++;
            else if (s[x][y] == 'O')
                dO[1]++;
            else if (s[x][y] == 'T')
                dt[1]++;
            x--;
            y++;
        }

        cout << "Case #" <<i <<": ";
        for (int j = 0; j < 4; j++)
        {
            if (rx[j] + rt[j] > 3)
            {
                cout << "X won\n";
                flag = 1;
                break;
            }
            else if (cx[j] + ct[j] > 3)
            {
                cout << "X won\n";
                flag = 1;
                break;
            }
            else if (ro[j] + rt[j] > 3)
            {
                cout << "O won\n";
                flag = 1;
                break;
            }
            else if (co[j] + ct[j] > 3)
            {
                cout << "O won\n";
                flag = 1;
                break;
            }
        }
        if (flag == 1)
            continue;

        for (int j = 0; j < 2; j++)
        {
            if (dx[j] + dt[j] > 3)
            {
                cout << "X won\n";
                flag = 1;
                break;
            }
            else if (dO[j] + dt[j] > 3)
            {
                cout << "O won\n";
                flag = 1;
                break;
            }
        }
        if (flag == 1)
            continue;

        if (d == 0)
        {
            cout << "Draw\n";
        }
        else
        {
            cout << "Game has not completed\n";
        }
    }
}
