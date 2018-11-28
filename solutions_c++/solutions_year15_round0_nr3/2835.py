#include <iostream>
using namespace std;
int m[8][8];
int T;
int s[10003];
int f[10000][10000];
int main()
{
    m[0][0] = 0;
    m[0][1] = 1;
    m[0][2] = 2;
    m[0][3] = 3;
    m[1][0] = 1;
    m[1][1] = 4;
    m[1][2] = 3;
    m[1][3] = 6;
    m[2][0] = 2;
    m[2][1] = 7;
    m[2][2] = 4;
    m[2][3] = 1;
    m[3][0] = 3;
    m[3][1] = 2;
    m[3][2] = 5;
    m[3][3] = 4;
    
    for (int i = 4; i < 8; ++i)
        for (int j = 0; j < 4; ++j)
            m[i][j] = (m[i-4][j] + 4) % 8;
    for (int i = 4; i < 8; ++i)
        for (int j = 4; j < 8; ++j)
            m[i][j] = m[i-4][j-4];
    for (int i = 0; i < 4; ++i)
        for (int j = 4; j < 8; ++j)
            m[i][j] = (m[i][j-4] + 4) % 8;

    string ss;
    cin >> T;
    int l, x, t;
    for (int I = 1; I <= T; ++I)
    {
        cin >> l >> x >> ss;
        t = 0;
        for (int i = 0; i < ss.size(); ++i)
        {
            if (ss[i] == 'i') s[i] = 1;
            if (ss[i] == 'j') s[i] = 2;
            if (ss[i] == 'k') s[i] = 3;
            t = m[t][s[i]];
        }
        int n = 1, tt = t;
        while (tt != 0)
        {
            ++n;
            tt = m[tt][t];
        }
        x = min(x, x%n+2*n);
        
        for (int i = 0; i < x * l; ++i)
        {
            f[i][i] = s[i%l];
            for (int j = i+1; j < x * l; ++j)
                f[i][j] = m[f[i][j-1]][s[j%l]];
        }
        bool res = false;
        for (int i = 0; i < x*l; ++i)
        {
            if (f[0][i] == 1)
                for (int j = i+2; j < x*l; ++j)
                    if (f[j][x*l-1] == 3 && f[i+1][j-1] == 2)
                    {
                        res = true;
                        break;
                    }
            if (res) break;
        }
        if (res)
            cout << "Case #" << I << ": YES" << endl;
        else
            cout << "Case #" << I << ": NO" << endl;

    }
}
