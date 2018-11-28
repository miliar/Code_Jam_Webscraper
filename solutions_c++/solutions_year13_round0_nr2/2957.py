#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("out.out", ios::out);
    int n, t;
    t = 0;
    cin >> n;
    while (t < n)
    {
        ++t;
        int r, c;
        cin >> r >> c;
        int g[101][101];
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                cin >> g[i][j];
            }
        }
        bool ok = true;
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                int k;
                bool cok = false;
                for (k = 0; k < c; ++k)
                {
                    if (g[i][k] > g[i][j])
                        break;
                }
                if (k == c)
                {
                    cok = true;
                    continue;
                }
                for (k = 0; k < r; ++k)
                {
                    if (g[k][j] > g[i][j])
                        break;
                }
                if (k == r)
                {
                    cok = true;
                    continue;
                }
                if (!cok)
                {
                    ok = false;
                    break;
                }
            }
            if (!ok)
                break;
        }
        fout << "Case #" << t << ": ";
        if (ok)
            fout << "YES" << endl;
        else
            fout << "NO" << endl;
    }
    return 0;
}
