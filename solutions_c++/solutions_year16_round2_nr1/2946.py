#include <vector>
#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

int main ()
{
    freopen ("1b.txt", "w", stdout);
    freopen ("A-large (2).in", "r", stdin);
    int q;
    cin >> q;
    for (int i = 1; i <= q; ++i)
    {
        vector <int> b(15);
        vector <int> c(0);
        string s;
        cin >> s;
        for (int x = 0; x < s.size(); ++x)
        {
            if (s[x] == 'E')
                ++b[0];
            else if (s[x] == 'F')
                ++b[1];
            else if (s[x] == 'G')
                ++b[2];
            else if (s[x] == 'H')
                ++b[3];
            else if (s[x] == 'I')
                ++b[4];
            else if (s[x] == 'N')
                ++b[5];
            else if (s[x] == 'O')
                ++b[6];
            else if (s[x] == 'R')
                ++b[7];
            else if (s[x] == 'S')
                ++b[8];
            else if (s[x] == 'T')
                ++b[9];
            else if (s[x] == 'U')
                ++b[10];
            else if (s[x] == 'V')
                ++b[11];
            else if (s[x] == 'W')
                ++b[12];
            else if (s[x] == 'X')
                ++b[13];
            else if (s[x] == 'Z')
                ++b[14];
        }
        for (int j = 1; j <= b[14]; ++j)
            c.push_back(0);
        b[0] -= b[14];
        b[7] -= b[14];
        b[6] -= b[14];
        for (int j = 1; j <= b[13]; ++j)
            c.push_back(6);
        b[4] -= b[13];
        b[8] -= b[13];
        for (int j = 1; j <= b[12]; ++j)
            c.push_back(2);
        b[9] -= b[12];
        b[6] -= b[12];
        for (int j = 1; j <= b[10]; ++j)
            c.push_back(4);
        b[1] -= b[10];
        b[6] -= b[10];
        b[7] -= b[10];
        for (int j = 1; j <= b[2]; ++j)
            c.push_back(8);
        b[0] -= b[2];
        b[4] -= b[2];
        b[3] -= b[2];
        b[9] -= b[2];
        for (int j = 1; j <= b[1]; ++j)
            c.push_back(5);
        b[4] -= b[1];
        b[11] -= b[1];
        b[0] -= b[1];
        for (int j = 1; j <= b[3]; ++j)
            c.push_back(3);
        b[0] -= b[3] * 2;
        for (int j = 1; j <= b[8]; ++j)
            c.push_back(7);
        b[0] -= b[8] * 2;
        b[5] -= b[8];
        for (int j = 1; j <= b[6]; ++j)
            c.push_back(1);
        for (int j = 1; j <= b[4]; ++j)
            c.push_back(9);
        sort (c.begin(), c.end());
        cout << "Case #" << i << ": ";
        for (int j = 0; j < c.size(); ++j)
            cout << c[j];
        cout << endl;
    }
}
