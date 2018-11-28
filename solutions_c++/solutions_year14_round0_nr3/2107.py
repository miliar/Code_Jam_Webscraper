#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

const double eps = 1e-10;

int main()
{
   // freopen("C-small-attempt5.in", "r", stdin);
   // freopen("C-small-attempt5.out", "w", stdout);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int r, c, m;
        cin >> r >> c >> m;
        char a[r][c];
        cout << "Case #" << i + 1 << ":" << endl;
        if (r == 1)
        {
            for (int j = 0; j < m; j++)
                cout << "*";
            for (int j = m; j < c - 1; j++)
                cout << ".";
            cout << "c";
            cout << endl;
        }
        else
        if (c == 1)
        {
            for (int j = 0; j < m; j++)
                cout << "*" << endl;
            for (int j = m; j < r - 1; j++)
                cout << "." << endl;
            cout << "c" << endl;
        }
        else
        if (c == 2)
        {
            if (r * c - m == 1)
            {
                for (int j = 0; j < r; j++)
                    for (int k = 0; k < c; k++)
                        a[j][k] = '*';
                a[0][0] = 'c';
                for (int j = 0; j < r; j++)
                {
                    for (int k = 0; k < c; k++)
                        cout << a[j][k];
                    cout << endl;
                }
            }
            else
            if (m % 2 == 1 || (r * c - m) <= c)
                cout << "Impossible" << endl;
            else
            {
                for (int j = 0; j < (m + 1) / 2; j++)
                {
                    a[j][0] = '*';
                    a[j][1] = '*';
                }
                for (int j = (m + 1) / 2; j < r; j++)
                {
                    a[j][0] = '.';
                    a[j][1] = '.';
                }
                a[r - 1][0] = 'c';
                for (int j = 0; j < r; j++)
                {
                    for (int k = 0; k < c; k++)
                        cout << a[j][k];
                    cout << endl;
                }
            }
        }
        else
        if (r == 2)
        {
            if (r * c - m == 1)
            {
                for (int j = 0; j < r; j++)
                    for (int k = 0; k < c; k++)
                        a[j][k] = '*';
                a[0][0] = 'c';
                for (int j = 0; j < r; j++)
                {
                    for (int k = 0; k < c; k++)
                        cout << a[j][k];
                    cout << endl;
                }
            }
            else
            if (m % 2 == 1 || (r * c - m) <= r)
                cout << "Impossible" << endl;
            else
            {
                for (int j = 0; j < (m + 1) / 2; j++)
                {
                    a[0][j] = '*';
                    a[1][j] = '*';
                }
                for (int j = (m + 1) / 2; j < c; j++)
                {
                    a[0][j] = '.';
                    a[1][j] = '.';
                }
                a[1][c - 1] = 'c';
                for (int j = 0; j < r; j++)
                {
                    for (int k = 0; k < c; k++)
                        cout << a[j][k];
                    cout << endl;
                }
            }
        }
        else
        if (r == 3 && c == 3)
        {
            if (m == 0)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
            }
            else
            if (m == 1)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..*" << endl;
            }
            else
            if (m == 3)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "***" << endl;
            }
            else
            if (m == 5)
            {
                cout << "c.*" << endl;
                cout << "..*" << endl;
                cout << "***" << endl;
            }
            else
            if (m == 8)
            {
                cout << "c**" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
            }
            else
                cout << "Impossible" << endl;
        }
        else
        if (r == 3 && c == 4)
        {
            if (m == 0)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
            }
            else
            if (m == 1)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
            }
            else
            if (m == 2)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "..**" << endl;
            }
            else
            if (m == 3)
            {
                cout << "c..*" << endl;
                cout << "...*" << endl;
                cout << "...*" << endl;
            }
            else
            if (m == 4)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "****" << endl;
            }
            else
            if (m == 6)
            {
                cout << "c.**" << endl;
                cout << "..**" << endl;
                cout << "..**" << endl;
            }
            else
            if (m == 8)
            {
                cout << "c.**" << endl;
                cout << "..**" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 11)
            {
                cout << "c***" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
                cout << "Impossible" << endl;
        }
        else
        if (r == 4 && c == 3)
        {
            if (m == 0)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
            }
            else
            if (m == 1)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "..*" << endl;
            }
            else
            if (m == 2)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..*" << endl;
                cout << "..*" << endl;
            }
            else
            if (m == 3)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "***" << endl;
            }
            else
            if (m == 4)
            {
                cout << "c.*" << endl;
                cout << "..*" << endl;
                cout << "..*" << endl;
                cout << "..*" << endl;
            }
            else
            if (m == 6)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "***" << endl;
                cout << "***" << endl;
            }
            else
            if (m == 8)
            {
                cout << "c.*" << endl;
                cout << "..*" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
            }
            else
            if (m == 11)
            {
                cout << "c**" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
            }
            else
                cout << "Impossible" << endl;
        }
        else
        if (r == 4 && c == 4)
        {
           if (m == 0)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
            }
            else
           if (m == 1)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
            }
            else
            if (m == 2)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
                cout << "...*" << endl;
            }
            else
            if (m == 3)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
                cout << "..**" << endl;
            }
            else
            if (m == 4)
            {
                cout << "c..*" << endl;
                cout << "...*" << endl;
                cout << "...*" << endl;
                cout << "...*" << endl;
            }
            else
            if (m == 5)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 6)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "..**" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 7)
            {
                cout << "c..*" << endl;
                cout << "...*" << endl;
                cout << "...*" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 8)
            {
                cout << "c.**" << endl;
                cout << "..**" << endl;
                cout << "..**" << endl;
                cout << "..**" << endl;
            }
            else
            if (m == 10)
            {
                cout << "c..*" << endl;
                cout << "...*" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 12)
            {
                cout << "c.**" << endl;
                cout << "..**" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 15)
            {
                cout << "c***" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
                cout << "Impossible" << endl;
        }
        else
        if (r == 3 && c == 5)
        {
            if (m == 0)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
            }
            else
            if (m == 1)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....*" << endl;
            }
            else
            if (m == 2)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 3)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "....*" << endl;
            }
            else
            if (m == 4)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 5)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "..***" << endl;
            }
            else
            if (m == 6)
            {
                cout << "c..**" << endl;
                cout << "...**" << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 7)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 9)
            {
                cout << "c..**" << endl;
                cout << "...**" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 11)
            {
                cout << "c.***" << endl;
                cout << "..***" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 14)
            {
                cout << "c****" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
                cout << "Impossible" << endl;
        }
        else
        if (r == 5 && c == 3)
        {
            if (m == 0)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
            }
            else
            if (m == 1)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "..*" << endl;
            }
            else
            if (m == 2)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "..*" << endl;
                cout << "..*" << endl;
            }
            else
            if (m == 3)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "***" << endl;
            }
            else
            if (m == 4)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "..*" << endl;
                cout << "***" << endl;
            }
            else
            if (m == 5)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..*" << endl;
                cout << "..*" << endl;
                cout << "***" << endl;
            }
            else
            if (m == 6)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "..." << endl;
                cout << "***" << endl;
                cout << "***" << endl;
            }
            else
            if (m == 7)
            {
                cout << "c.*" << endl;
                cout << "..*" << endl;
                cout << "..*" << endl;
                cout << "..*" << endl;
                cout << "***" << endl;
            }
            else
            if (m == 9)
            {
                cout << "c.." << endl;
                cout << "..." << endl;
                cout << "***" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
            }
            else
            if (m == 11)
            {
                cout << "c.*" << endl;
                cout << "..*" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
            }
            else
            if (m == 14)
            {
                cout << "c**" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
                cout << "***" << endl;
            }
            else
                cout << "Impossible" << endl;
        }
        else
        if (r == 4 && c == 5)
        {
            if (m == 0)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
            }
            else
            if (m == 1)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....*" << endl;
            }
            else
            if (m == 2)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 3)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....*" << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 4)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "...**" << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 5)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "....*" << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 6)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "...**" << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 7)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "...**" << endl;
                cout << "..***" << endl;
            }
            else
            if (m == 8)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "..***" << endl;
                cout << "..***" << endl;
            }
            else
            if (m == 9)
            {
                cout << "c..**" << endl;
                cout << "...**" << endl;
                cout << "...**" << endl;
                cout << "..***" << endl;
            }
            else
            if (m == 10)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 11)
            {
                cout << "c..**" << endl;
                cout << "...**" << endl;
                cout << "...**" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 12)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 14)
            {
                cout << "c..**" << endl;
                cout << "...**" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 16)
            {
                cout << "c.***" << endl;
                cout << "..***" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 19)
            {
                cout << "c****" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
                cout << "Impossible" << endl;
        }
        else
        if (r == 5 && c == 4)
        {
            if (m == 0)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
            }
            else
            if (m == 1)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
            }
            else
            if (m == 2)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "..**" << endl;
            }
            else
            if (m == 3)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
                cout << "..**" << endl;
            }
            else
            if (m == 4)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "..**" << endl;
                cout << "..**" << endl;
            }
            else
            if (m == 5)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
                cout << "..**" << endl;
                cout << "..**" << endl;
            }
            else
            if (m == 6)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "..**" << endl;
                cout << "..**" << endl;
                cout << "..**" << endl;
            }
            else
            if (m == 7)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
                cout << "..**" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 8)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...." << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 9)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "...*" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 10)
            {
                cout << "c..." << endl;
                cout << "...." << endl;
                cout << "..**" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 11)
            {
                cout << "c..*" << endl;
                cout << "...*" << endl;
                cout << "...*" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 12)
            {
                cout << "c..*" << endl;
                cout << "...*" << endl;
                cout << "..**" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 14)
            {
                cout << "c..*" << endl;
                cout << "...*" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 16)
            {
                cout << "c.**" << endl;
                cout << "..**" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
            if (m == 19)
            {
                cout << "c***" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
                cout << "****" << endl;
            }
            else
                cout << "Impossible" << endl;
        }
        else
        if (r == 5 && c == 5)
        {
            if (m == 0)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
            }
            else
            if (m == 1)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....*" << endl;
            }
            else
            if (m == 2)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 3)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....*" << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 4)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "...**" << endl;
                cout << "...**" << endl;
            }
            else
            if (m == 5)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 6)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "....*" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 7)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "...**" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 8)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "..***" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 9)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "...**" << endl;
                cout << "...**" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 10)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....." << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 11)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "....*" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 12)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "...**" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 13)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "..***" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 14)
            {
                cout << "c...*" << endl;
                cout << "....*" << endl;
                cout << "...**" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 15)
            {
                cout << "c...." << endl;
                cout << "....." << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 16)
            {
                cout << "c..**" << endl;
                cout << "...**" << endl;
                cout << "...**" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 17)
            {
                cout << "c..**" << endl;
                cout << "...**" << endl;
                cout << "..***" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 19)
            {
                cout << "c..**" << endl;
                cout << "...**" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 21)
            {
                cout << "c.***" << endl;
                cout << "..***" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
            if (m == 24)
            {
                cout << "c****" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
                cout << "*****" << endl;
            }
            else
                cout << "Impossible" << endl;
        }
    }
}
